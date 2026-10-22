# 宿主工具层注意事项(tooling notes)

> **适用范围**:仅适用于 CDP proxy/合成事件类宿主(web-access、chrome-devtools MCP 等),与具体航司站点无关。站点事实见 [airlines.md](airlines.md),方法论与证据政策见 [SKILL.md](../SKILL.md)。Playwright/原生驱动类宿主大多不存在下列问题。

## 1. eval 中文常量乱码(最隐蔽)

- **症状**:`innerText` 明明包含"按航班号查询",`includes('按航班号')` 却恒为 false;按中文文本找元素永远失败。输出里中文显示正常,极易误判为 shadow DOM/反爬零宽字符。
- **原因**:eval 的 POST body 里 UTF-8 中文常量可能被传输层按 GBK 类编码解码损坏,`\uXXXX` 转义一并损坏。
- **解法**:eval 内用码点构造中文:`String.fromCharCode(0x6309,0x73ED)` 拼"按班"。10 秒验证:字面量不中、码点能中 → 传输层问题实锤,改写全部中文常量,别再怀疑 DOM。

## 2. clickAt 坐标漂移

- **症状**:eval 量得元素在 (700,560),clickAt 报 "clicked at (713,330)",点到隔壁选项/输入框(实测"北京"点成"三亚")。页面越长越易触发。
- **原因**:clickAt 内部先 scrollIntoView 再算坐标,两次滚动时序差导致落点错位。
- **解法**:定位与点击放**同一个 eval**:重新取 `getBoundingClientRect()` → `el.focus()` → 依次派发 mousedown→mouseup→click(带正确 clientX/Y)。clickAt 返回坐标与 eval 量取不一致时,弃用 clickAt。
- **边界**:仅用于点击已确认的目标元素;不得借此规避控件校验(SKILL.md 证据政策)。

## 3. "clicked:true" ≠ 命中目标

全屏弹窗遮罩未关时,点哪都报成功但无反应。点击无反应的第一步:**截图看遮罩**,用页面正常关闭控件处理后再操作。

## 4. 后台 tab 截图超时

`Page.captureScreenshot` 对后台页偶发超时(浏览器后台节流):直接重试即可,不必换方案。

## 5. 框架对 CDP 事件不响应(个案)

- **TV 西藏航空**:城市候选面板对 CDP 真实鼠标(clickAt)、合成 click/pointer/touch、回车均不写入值;第一轮用 Playwright 原生点击查通。此类站点换 Playwright 类宿主,不硬刚。
- **KY 昆明航空**:提交按钮需真实鼠标事件才生效(合成提交无反应);生效后流程正常。

## 6. 稳定操作顺序

1. `check-deps` → 打开页面 → 先截初始图确认真实状态;
2. 中文匹配一律码点构造;
3. 点击优先"单 eval 内 focus + 事件序列",工具原生 click 其次,clickAt 慎用;
4. 点击无反应 → 查遮罩 → 仍不行读 `form.action` 判断提交方式;
5. 控件改值不受控时按 SKILL.md 证据政策如实记录控件最终值;
6. 每步产出物交付前先目检。
