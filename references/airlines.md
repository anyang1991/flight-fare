# 航司入口与站点经验

按航班号前两位**字母或数字**查入口。未收录的航司先搜索其官网并核对身份，不依赖搜索广告。跨域订票入口须由官网链接确认，不因域名相似就输入账户信息。

入口收录不等于完整查询通过。2026-10-21 已逐家访问 24 个入口并尝试可进行的查询，详见 [本轮实测报告和原始截图](live-tests-20261021.md)。下方保留作者历史操作笔记；本轮新证据与失败原因以报告为准。选择器、URL、库存和日期可选状态都会变化，失败就回到当前官网表单，不循环套用旧脚本。

## 入口表

| 二字码 | 航司 | 官网入口 | 说明 |
|---|---|---|---|
| CA | 中国国航 | https://www.airchina.com.cn | 明确全价(10-23);[复测](live-tests-retest-20261021.md) |
| MU | 中国东航 | https://www.ceair.com | 明确全价·两轮一致 ¥2150;[复测](live-tests-retest-20261021.md) |
| FM | 上海航空 | https://www.ceair.com | 明确全价 ¥1490(上轮仅列表);[复测](live-tests-retest-20261021.md) |
| KN | 中国联航 | https://www.flycua.com | 未确认全价·仅航段公布价 ¥1630;[复测](live-tests-retest-20261021.md) |
| CZ | 中国南航 | https://www.csair.com | 明确全价·两轮一致 ¥3060;[复测](live-tests-retest-20261021.md) |
| HU | 海南航空 | https://www.hnair.com | 明确全价·两轮一致 ¥4190;[复测](live-tests-retest-20261021.md) |
| GS | 天津航空 | https://www.tianjin-air.com | 明确全价·两轮一致 ¥2170;[复测](live-tests-retest-20261021.md) |
| 8L | 祥鹏航空 | https://www.luckyair.net | 明确全价·两轮一致 ¥3380;[复测](live-tests-retest-20261021.md) |
| PN | 西部航空 | https://www.westair.cn | 明确全价·两轮一致 ¥2180;[复测](live-tests-retest-20261021.md) |
| UQ | 乌鲁木齐航空 | https://www.urumqi-air.com | 明确全价 ¥2810(上轮受阻,10-23 经停);[复测](live-tests-retest-20261021.md) |
| JD | 首都航空 | https://www.jdair.net | 受阻·官网403+航班动态校验异常;UI 纯路径待补测,程序化兜底见 hnair 条目;[阻塞类别与复试策略](live-tests-retest-20261021.md#阻塞类别与复试策略) |
| ZH | 深圳航空 | https://www.shenzhenair.com | 未确认全价 ¥3650 无全价标签(上轮 418 未复现);[复测](live-tests-retest-20261021.md) |
| SC | 山东航空 | https://www.sda.cn | 明确全价·两轮一致 ¥1437(带优惠标签);[复测](live-tests-retest-20261021.md) |
| MF | 厦门航空 | https://www.xiamenair.com | 未确认全价·仅Y舱报价 ¥3090;[复测](live-tests-retest-20261021.md) |
| HO | 吉祥航空 | https://www.juneyaoair.com | 未确认全价·公布价/Y售价双口径;[复测](live-tests-retest-20261021.md) |
| 9C | 春秋航空 | https://www.ch.com | 未确认全价·仅航段公布价(LCC);[复测](live-tests-retest-20261021.md) |
| 3U | 四川航空 | https://www.sichuanair.com | 明确全价 ¥2950(上轮仅列表);[复测](live-tests-retest-20261021.md) |
| G5 | 华夏航空 | https://www.chinaexpressair.com | 受阻·登录墙,需登录接续;[阻塞类别与复试策略](live-tests-retest-20261021.md#阻塞类别与复试策略) |
| GJ | 长龙航空 | https://www.loongair.cn | 受阻·登录墙,需登录接续;[阻塞类别与复试策略](live-tests-retest-20261021.md#阻塞类别与复试策略) |
| EU | 成都航空 | https://www.cdal.com.cn/stdair/homepage | 未确认全价 Y ¥2450(上轮 500 未复现);[复测](live-tests-retest-20261021.md) |
| KY | 昆明航空 | https://www.airkunming.com | 受阻·KMG→PEK 无该司航班(查询已通,需真实鼠标事件,[tooling-notes](tooling-notes.md));[阻塞类别](live-tests-retest-20261021.md#阻塞类别与复试策略) |
| TV | 西藏航空 | https://www.tibetairlines.com.cn | 受阻·工具不响应([tooling-notes](tooling-notes.md));第一轮 Playwright 获 Y ¥2810;[阻塞类别](live-tests-retest-20261021.md#阻塞类别与复试策略) |
| BK | 奥凯航空 | https://www.okair.net | 受阻·登录墙,需登录接续;[阻塞类别与复试策略](live-tests-retest-20261021.md#阻塞类别与复试策略) |
| DZ | 东海航空 | https://www.donghaiair.com | 受阻·会话过期,疑似接口强制登录;[阻塞类别与复试策略](live-tests-retest-20261021.md#阻塞类别与复试策略) |

全部入口均有本轮浏览器记录；只有表中抽查航线的相应证据得到确认。JD 入口另由[首都航空官方文件](https://www.jdair.net/fecms.pub.bucket.jd/YZJD0310.pdf)核对，本轮访问为 403。需要登录或本次未完成的入口仍可保留，但不能标成全价查询通过。

## 通用操作

- 城市输入要在下拉中点选，提交后重新核对城市、机场和完整日期。城市码不保证覆盖该城市所有机场。
- 使用浏览器工具自带的点击/填写，不把 DOM `dispatchEvent()` 当作真实用户事件；合成事件不具有相同的信任状态，也不能解决所有前端状态问题。
- 航班号可能带空白或换行，按“完整二字码 + 完整数值部分”匹配，避免 `CA1501` 命中 `CA15010`。
- 弹窗用页面提供的关闭/确认控件处理，关闭后读取状态再点击价格。不要隐藏弹层、航班行或改写页面来取证。
- 页面发生导航后读取新页面，同时检查新打开的标签页；山航本轮从首页打开独立结果页。不把“没出现 XHR”当作未提交，只保存实际可见、展开的明细。
- 单站点内连续完成城市、日期和提交；跨页操作可能关闭候选框。同名输入可能有隐藏副本，定位当前可见控件，提交后再核对完整日期和实际机场。
- 明确分开记录航段公布价、Y 舱售价和优惠后产品售价。本轮 HO 公布价与 Y 售价不同，SC 全价产品同时有“已减3元”；MF/TV 仅见 Y 标签，未提升为全价确认。

## CA：中国国航（作者历史笔记，2026-10-21）

- 曾使用结果页路径：`https://www.airchina.com.cn/flight/oneway/pek-sha/2026-10-22`。此为历史示例，实际航段和日期以用户请求为准。
- 表单曾使用 `出发机场`、`到达机场` 等 placeholder；聚焦后提示文字可能改变。
- 目标行的经济舱价格格展开后曾显示“经济全价(Y舱)”和“无折扣公布运价:…经济舱Y舱 ¥…”；同时核对对应航班行。
- 公告可能多条，曾有“确认,查看下一个提示”和“我知道了”；停留过久可能需重新查询。
- 某次当天日期禁选不代表该站永远不能查当天。日历相邻月份的同号日期要核对年月。

## MU：中国东航（作者历史笔记，2026-10-21）

- 曾使用首页：`https://www.ceair.com/zh/cny/home`，表单 `.search-form`；结果页路径曾含 `/zh/cny/shopping/oneway/`。不手拼省略号或不完整的机场组合。
- 航班行容器 class 曾含 `shopping-parent-item-container`，经济舱价格格曾含 `cabin-level-item`。
- 展开后产品卡横向排列，全价卡曾标“经济舱全价”“不含税价”；卡片标题 class 曾含 `fare-title-text`。使用页面横向滚动或箭头找到卡片，不重排卡片。
- 同价的“升舱优享”不是全价经济舱证据；标题、价格与航班行要对应。
- 历史示例未直接展示 Y 代码，记录时只写页面出现的舱位信息。

## CZ：中国南航（作者历史笔记，2026-10-21）

- 曾使用首页：`https://www.csair.com/cn/index.shtml`；输入框 ID 曾为 `fDepCity`、`fArrCity`、`fDepDate`。
- 结果页曾在 `https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html`，参数含城市、机场、日期、成人/儿童/婴儿人数；应从官网当前表单生成，不照搬历史参数。
- 经济舱格 class 曾含 `zls-cabin-cell`；展开后曾显示“全价经济舱 | Y 舱 | 全价”。核对价格所在档位，不用页面文本顺序猜归属。
- 初始提示可能遮挡价格格，先用可见按钮关闭；缺少税费标签时记“税费口径未展示”，不默认含税。

## HU：海南航空

整合 2026-10-21 历史笔记与用户提供的 2026-11-02 hnair / ego-browser 经验；后者未在本次维护复测。选择器须在当前页面核对，不推广到其他海航系航司或所有 JSP 站点。工具进程、快照与窗口恢复见 [工具笔记](tooling-notes.md)。

- **入口与航线**：官方订票页曾为 `https://new.hnair.com/hainanair/ibe/common/flightSearch.do`，结果页为 `/hainanair/ibe/air/searchResults.do`；从当前官网链接进入。用户已给出航段时直接使用；需查航线时进入 `flightDynamic.do`，核对请求日期和实际返回的航段/时刻。动态只给城市时先不确定机场码，订票结果确认机场后再命名文件。
- **航班号查询**：页面曾同时含隐藏 `#searchForm` 与可见 `#searchFlightNoForm`，泛文本“查询”会误命中。限定可见表单，用 `.select-show` 选择 `dd[data-value="HU"]`，再填 `input.flight-number` 的数字部分，点击表单内 `.flight-number-search-btn`。值已填仍报空时，检查航司是否经下拉绑定；隐藏字段曾名为 `Search/AirLineInformation$1$/airLine`，可只读核对，不直接改写绕过校验。
- **城市与日期**：选成人单程；城市先用 `fill("")` 或等价方式清空，再聚焦并在当前 `.location-component.focus` 内点选候选，读回输入和选中状态，避免全选失效后追加文字。日期从 `input.depart-input` 打开日历，对 `#datepicker-div td.date-td` 核对**所属面板年月 + 日期**后点击；双月日历不能只按数字匹配，“今天2¥1550”也不会命中 `^2¥`。提交前和结果页都核对完整年月日与机场。
- **弹窗与假点击**：报错提到 `crew-mask` 等拦截元素时，先读当前弹窗，再用其正常关闭/确认按钮处理并验证消失。cookie 提示曾挡住经济舱格，使点击报成功却无变化；无标签的关闭按钮可依据当前截图定位，不复用坐标，也不盲点涉及条款或授权的“确定”。允许 DOM 时以可见性、`getClientRects()`、尺寸和样式辅助排查，不只靠 `offsetParent`。
- **展开经济舱**：精确匹配完整航班号和实际机场，在目标行范围内点击 `.flight-cabin[cabincode="Y"]`，单点 `.ticket-price` 曾无效。明细容器曾为 `.dis-cabin`，可能预渲染但隐藏，必须实际展开可见。
- **动画与面板归属**：结果页可同时展开多个航班，展开/收起后等待状态和布局稳定再重新定位，固定等 1.2 秒或复用旧坐标不可靠。优先用目标行容器、关联 ID 或相邻结构确认明细；“祖先含航班号”可能命中整个列表。缺少关联时，用当前航班行、面板及下一航班行的纵向范围交叉核对；仍有歧义就正常收起其他明细再展开目标，不能确认则记“证据不完整”。
- **读价与全价判定**：仅从可见、归属已确认的 `.dis-cabin[cabincode="Y"]` 读取产品和价格原文；Y 属性本身不证明全价。普通全价行曾显示“全价经济舱 | Y舱 | 全价 | ¥…（不含税费）”，另有“仅限本人预定”等条件产品，不能混用。`全价￥(\d+)（不含税费）` 只是一次文本形式，币符、空格、逗号及小数变化时核对原文，不匹配就不能静默改取其他数字。
- **截图与复用**：完成主流程的视口、遮挡、tooltip 三查；鼠标移到当前画面的中性区域，不固定照抄 `(900,150)`。允许 DOM 时检查 `.hover-con` 中实际可见数为 0，再按需保存概览、航班行与明细、价格特写并目检，不固定三张。反向查询可用 `.icon-exchange` 对调城市再点 `.search-btn`，仍重新核对日期、人数、机场与目标航班。
- **减少重复调用**：同一页面合并动作、可观察状态等待及局部读回；失败立即停下批次，再输出目标表单或航班的最小诊断。优先读表单值、匹配数、可见产品原文和位置，不整页 dump；DOM 核对数字可省重复 OCR，但不能代替原图与目检。同一步连续两次无进展后，按主流程诊断并最多做一次有依据的修正，仍失败就记录阻塞。
- **提交兜底与访问限制**：控件仍回写时，宿主允许的等价程序化提交须将用户请求值的设值与 `form.submit()` 放在同一 eval，并在汇总注明；优先走真实候选选择和日历点击。403/风控时记录阻塞，不关闭证书校验或擅自更改代理。
