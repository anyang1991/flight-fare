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

## HU：海南航空（作者历史笔记，2026-10-21）

- 官方订票站点曾使用 `https://new.hnair.com/hainanair/ibe/common/flightSearch.do`，结果页曾为 `/hainanair/ibe/air/searchResults.do`；使用时核对官网当前链接。
- 经济舱展开钮曾在 `.ticket-price` 旁，明细容器曾含 `.dis-cabin`。
- 普通全价行曾显示“全价经济舱 | Y舱 | 全价 | ¥…（不含税费）”。另有“仅限本人预定”等条件产品，不能混用。
- 航班号可能带空格；明细可能预渲染但尚隐藏，必须展开并确认可见后截图。
- 客服浮层或 cookie 提示使用正常关闭控件处理。表单回写日期或写错城市时的 **UI 纯路径**:点日期框弹日历 → 真实点击日期格 → 核对输入框值已变 → 点查询(2026-10-21 复测未尝试此路径,下轮优先补测)。
- 控件仍阻塞时,允许**等价程序化提交**:填写用户请求的值后,设值与 `form.submit()` 必须在同一 eval 内完成(不给日历回写窗口)。结果页为站点真实响应,取证效力不变;须在汇总注明提交方式。禁的是篡改证据与替用户做未请求的选择,不是提交方式本身。
- 403/风控时记录阻塞；不要为了取价关闭证书校验或擅自更改代理。此笔记不证明其他海航系航司使用相同库存或产品。
