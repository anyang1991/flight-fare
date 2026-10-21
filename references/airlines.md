# 航司入口与站点经验

按航班号前两位**字母或数字**查入口。未收录的航司先搜索其官网并核对身份，不依赖搜索广告。跨域订票入口须由官网链接确认，不因域名相似就输入账户信息。

入口收录不等于完整查询通过。以下 CA/MU/CZ/HU 操作笔记继承自作者 2026-10-21 的记录；本次维护未重新完成端到端查询。选择器、URL、库存和日期可选状态都会变化，失败就回到当前官网表单，不循环套用旧脚本。

## 入口表

| 二字码 | 航司 | 官网入口 | 说明 |
|---|---|---|---|
| CA | 中国国航 | https://www.airchina.com.cn | 有历史查询笔记 |
| MU | 中国东航 | https://www.ceair.com | 有历史查询笔记 |
| FM | 上海航空 | https://www.ceair.com | 从东航官方入口核对 FM 航班 |
| KN | 中国联航 | https://www.flycua.com | 独立入口 |
| CZ | 中国南航 | https://www.csair.com | 官方结果页曾在 b2c.csair.com |
| HU | 海南航空 | https://www.hnair.com | 官方订票入口曾在 new.hnair.com |
| GS | 天津航空 | https://www.tianjin-air.com | 独立入口，未完成价格查询复测 |
| 8L | 祥鹏航空 | https://www.luckyair.net | 独立入口，未完成价格查询复测 |
| PN | 西部航空 | https://www.westair.cn | 独立入口，未完成价格查询复测 |
| UQ | 乌鲁木齐航空 | https://www.urumqi-air.com | 独立入口，未完成价格查询复测 |
| JD | 首都航空 | https://www.jdair.net | 独立入口；不能假设只能在海航查 |
| ZH | 深圳航空 | https://www.shenzhenair.com | 仅收录入口 |
| SC | 山东航空 | https://www.shandongair.com.cn | 仅收录入口 |
| MF | 厦门航空 | https://www.xiamenair.com | 仅收录入口 |
| HO | 吉祥航空 | https://www.juneyaoair.com | 仅收录入口 |
| 9C | 春秋航空 | https://www.ch.com | 不假设有标准 Y 舱全价 |
| 3U | 四川航空 | https://www.sichuanair.com | 仅收录入口 |
| G5 | 华夏航空 | https://www.chinaexpressair.com | 仅收录入口 |
| GJ | 长龙航空 | https://www.loongair.com.cn | 仅收录入口 |
| EU | 成都航空 | https://www.chengduair.cc | 仅收录入口 |
| KY | 昆明航空 | https://www.airkunming.com | 仅收录入口 |
| TV | 西藏航空 | https://www.tibetairlines.com.cn | 仅收录入口 |
| BK | 奥凯航空 | https://www.okair.net | 仅收录入口 |
| DZ | 东海航空 | https://www.donghaiair.com | 仅收录入口 |

GS/8L/PN/UQ 的独立入口由各航司官网页面核对（2026-10-21）；JD 入口由[首都航空官方文件](https://www.jdair.net/fecms.pub.bucket.jd/YZJD0310.pdf)核对。这只确认入口，不确认当前订票链路或 Y 舱库存。其他入口继承自原版，使用时继续验证。

## 通用操作

- 城市输入要在下拉中点选，提交后重新核对城市、机场和完整日期。城市码不保证覆盖该城市所有机场。
- 使用浏览器工具自带的点击/填写，不把 DOM `dispatchEvent()` 当作真实用户事件；合成事件不具有相同的信任状态，也不能解决所有前端状态问题。
- 航班号可能带空白或换行，按“完整二字码 + 完整数值部分”匹配，避免 `CA1501` 命中 `CA15010`。
- 弹窗用页面提供的关闭/确认控件处理，关闭后读取状态再点击价格。不要隐藏弹层、航班行或改写页面来取证。
- 页面发生导航后读取新页面，不把“没出现 XHR”当作未提交。只保存实际可见、展开的明细。

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
- 客服浮层或 cookie 提示使用正常关闭控件处理。表单若回写日期或写错城市，重新选择并核对；不要强填隐藏字段或抢在控件更新前提交。
- 403/风控时记录阻塞；不要为了取价关闭证书校验或擅自更改代理。此笔记不证明其他海航系航司使用相同库存或产品。
