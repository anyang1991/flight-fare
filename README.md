# flight-fare ✈️

给支持浏览器操作的 AI agent 使用的 [Agent Skill](https://agentskills.io/specification)：在航空公司官网查询指定航班的全价经济舱价格，保存原始截图和查询记录，供报销比价参考。

**需要能操作网页并保存截图的浏览器工具。** 这是一套可复用的查询流程，不是独立爬虫，也不承诺绕过验证码、登录或官网限制。只有搜索能力的 agent 无法完成截图取证。

## 快速安装

安装目录名保持 `flight-fullfare-screenshot`，与 `SKILL.md` 中的 `name` 一致。以下命令选择一种执行；已有目录请先检查本地修改，不要直接覆盖。

### Codex（个人使用）

macOS / Linux：

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/anyang1991/flight-fare.git ~/.agents/skills/flight-fullfare-screenshot
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME/.agents/skills" | Out-Null
git clone https://github.com/anyang1991/flight-fare.git "$HOME/.agents/skills/flight-fullfare-screenshot"
```

目录依据 [OpenAI 官方本地 skill 文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。也可以让 Codex 自带的 skill-installer 从本仓库安装。安装后在技能列表中检查；未出现时重启宿主。浏览器能力由宿主提供，skill 本身不会安装插件或连接你的日常浏览器。

### Claude Code

```sh
mkdir -p ~/.claude/skills
git clone https://github.com/anyang1991/flight-fare.git ~/.claude/skills/flight-fullfare-screenshot
```

Windows PowerShell 将上面的目标改为 `"$HOME/.claude/skills/flight-fullfare-screenshot"`。在宿主中另行配置其支持的浏览器工具，例如官方 [Playwright MCP](https://github.com/microsoft/playwright-mcp)；安装 skill 不会自动获得浏览器权限。

### 其他 agent

将仓库放入该工具文档规定的 skills 目录，保留根目录的 `SKILL.md` 和 `references/`。不支持 skills 的工具可以显式读取这两个文件。遵守各宿主的工具限制，不需要固定的 proxy、端口或浏览器配置。ZCode 等工具的具体安装位置以各自文档为准。

## 开始使用

```text
帮我查 CA1501，2026-10-22，北京首都到上海虹桥的全价经济舱价格，报销用，要官网截图。
```

```text
查 MU5137、HU7605 的全价经济舱，未指定日期时用最近可查日期，并注明替代日期。
```

支持 `3U8886`、`8L…`、`9C…`、`G5…` 等含数字的航司代码，也支持 `mu 5137` 这样的空格和小写输入。无法从官网确定航线时会询问，不会猜航线。

默认输出到当前任务的 `报销截图/查询_YYYYMMDD_HHMMSS/`（或用户/宿主指定的交付目录）：原始 PNG 和 `汇总.md`。汇总包含成功与失败项、航班/承运人、请求及实际查询日期、机场、产品原文、价格/币种/税费口径、官网链接、带时区采集时间和截图链接。重复运行不覆盖旧记录。

## 价格与截图规则

- **指定日期就查指定日期。** 没有日期时，从出发地今天起最多查 14 个日期，并标“替代日期参考”。未来报价不能证明过去价格。
- **不假设全价在不同日期、航司、机场间一致。** 国航[国内运价规则](https://webresource.airchina.com.cn/zh-CN/content/c/2026-04-20/28994.shtml)要求以销售系统计算的价格为准；本工具只记录本次页面展示。
- **有明确证据才确认全价。** “¥…起”、最高档、升级产品或按折扣倒算都不算。只显示“经济舱全价”时不会自行补写 Y 舱；税费未标注时会明确记录。
- **保留原始页面。** 不修改价格、日期、DOM/CSS，不隐藏航班行、不拼图；同屏放不下就交付同次查询的多张截图。完整年份、航班、航段和产品价格均须可核对。
- **只查询，不下单。** 不填写旅客信息、不创建订单、不支付。验证码或登录由用户在官方页面处理。
- **可追溯，不保证报销通过。** 具体截图要求由用户所在单位决定；失败或证据不完整会明确标注，不换第三方价格冒充官网结果。

## 覆盖与测试状态

[航司入口表](references/airlines.md)收录 24 个航司代码；收录入口不等于当前完整流程已验证。

| 范围 | 当前证据 |
|---|---|
| CA / MU / CZ / HU | 保留作者原始版本的操作笔记和历史截图；本次未完成官网端到端复测 |
| GS / 8L / PN / UQ / JD | 本次核对独立官方入口；未验证全价查询链路 |
| 其他入口 | 从原版继承，使用时核验当前官网和页面 |
| 包结构与本地引用 | 提供跨平台自动验证及 GitHub Actions |
| 日期、全价识别、失败降级等行为 | 提供可重复的场景检查表；不将静态检查算作浏览器测试 |

维护记录、测试范围和限制见 [tests/README.md](tests/README.md)。官网改版、风控、未开售、售罄、共享航班或无标准全价产品都可能导致查询失败。

## 历史示例

以下是原仓库留存的截图，**不是本次新查询结果，也不应当作当前报价或其他日期的报销凭证**。部分截图没有显示完整年份，原版流程曾允许改动页面布局，未保存可审计的原始页面记录；新流程要求不改页面并补齐证据。

| 航班 | 文件所标日期 | 原图 | 局限 |
|---|---|---|---|
| CA1501 | 2026-10-22 | [查看](examples/CA1501_20261022_全价经济舱.png) | 历史结果，不能推定其他日期价格 |
| MU5137 | 2026-10-22 | [查看](examples/MU5137_20261022_全价经济舱.png) | 显示全价产品，未直接展示 Y 代码 |
| CZ3099 | 2026-10-22 | [查看](examples/CZ3099_20261022_全价经济舱.png) | 图片未显示完整年份 |
| HU7605 | 2026-10-22 | [查看](examples/HU7605_20261022_全价经济舱.png) | 图片未显示完整年份 |

## 开发与贡献

查询使用本身不需要 Python。维护者可用 Python 3.10+ 运行离线检查：

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

CI 在 Windows 和 Linux 检查技能元数据、安装包目录名、相对链接和测试。离线检查不访问航司，也不能证明价格查询成功。

提交站点经验时附测试日期、入口、航司/航段、浏览器环境、实际结果和已脱敏的原始截图；区分“入口可访问”和“全价截图已成功”。先报告或提交修改，不让普通查询自动改写已安装文件。不要提交个人行程、账户信息、cookie 或查询输出。

许可证：[MIT](LICENSE)。代码和文档允许复用、修改和分发；示例中的航司标识、网页内容等第三方材料不因此获得额外授权。
