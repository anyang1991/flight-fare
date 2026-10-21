# 航司二字码 → 官网入口

> 使用约定:按航班号前两位字母查下表;未收录的航司用 WebSearch `"{航司名} 官网"` 找入口。
> "站点经验"只记录**实际操作验证过**的事实(URL 模式、选择器、陷阱),标注发现日期。按经验操作失败时回退通用 GUI 流程,并更新本文件。

## 航司速查表

| 二字码 | 航司 | 官网 | 备注 |
|--------|------|------|------|
| CA | 中国国航 | https://www.airchina.com.cn | |
| MU | 中国东航 | https://www.ceair.com | 东航系总入口 |
| FM | 上海航空 | https://www.ceair.com | 东航旗下,FM 航班在东航官网查 |
| KN | 中国联航 | https://www.flycua.com | 东航旗下,独立官网 |
| CZ | 中国南航 | https://www.csair.com | |
| HU | 海南航空 | https://www.hnair.com | 海航系总入口 |
| GS | 天津航空 | https://www.hnair.com | 海航系 |
| 8L | 祥鹏航空 | https://www.hnair.com | 海航系 |
| PN | 西部航空 | https://www.hnair.com | 海航系 LCC |
| UQ | 乌鲁木齐航空 | https://www.hnair.com | 海航系 |
| JD | 首都航空 | https://new.hnair.com | 海航系;无独立订票入口,走海航订票系统,航线用海航"航班动态"按航班号查 |
| ZH | 深圳航空 | https://www.shenzhenair.com | 国航系,独立官网 |
| SC | 山东航空 | https://www.shandongair.com.cn | 国航系,独立官网 |
| MF | 厦门航空 | https://www.xiamenair.com | 南航旗下,独立销售 |
| HO | 吉祥航空 | https://www.juneyaoair.com | |
| 9C | 春秋航空 | https://www.ch.com | LCC,可能无标准 Y 舱全价票,遇到要说明 |
| 3U | 四川航空 | https://www.sichuanair.com | |
| G5 | 华夏航空 | https://www.chinaexpressair.com | |
| GJ | 长龙航空 | https://www.loongair.com.cn | |
| EU | 成都航空 | https://www.chengduair.cc | |
| KY | 昆明航空 | https://www.airkunming.com | |
| TV | 西藏航空 | https://www.tibetairlines.com.cn | |
| BK | 奥凯航空 | https://www.okair.net | |
| DZ | 东海航空 | https://www.donghaiair.com | |

## 通用经验(2026-10-21 实测)

- **`el.click()` 在国航/东航的 React/Vue 页面上经常不生效,要用真实鼠标事件序列**;web-access 的 `/clickAt` 可用但有坐标漂移风险(内部先 scrollIntoView 再算坐标,时序差会点错位置),首选"单 eval 内 focus + mousedown→mouseup→click(带 clientX/Y)"——定位与点击同一次调用,无跨调用漂移。详见 SKILL.md「排障与稳定套路」。
- 输入框赋值:用原生 setter + `dispatchEvent(new Event("input", {bubbles:true}))`,城市类输入框要等下拉出现后**点选项**(点城市级或机场级均可)。
- 第三方航线查询现状(2026-10-21):飞常准 PC 站 502/强制跳 APP 下载页,m.variflight.com 连接关闭;百度搜索触发安全验证;Bing 对航班号几乎无结果。**不要依赖第三方查航线**——直接在航司官网按"城市对"搜索(如 上海→北京,城市级会覆盖虹桥/浦东、首都/大兴全部机场),在结果列表里确认目标航班号即可,航线就验证了。
- CDP proxy 视口锁定 800×513,用 CDP `Emulation.setDeviceMetricsOverride` 改视口会被 proxy 重置。构图手段:`document.documentElement.style.zoom` 缩放 + 滚动;同屏放不下时,可隐藏与目标航班无关的列表行(`display:none`,等价于裁剪,不动证据元素本身)。
- `body.innerText` 里航班号可能被拆成 "MU\n5137",找行时用 `/MU\s*\n?\s*5137/`。
- 传输层/点击类通用排障(eval 中文常量乱码、clickAt 漂移、遮罩假点击、控件回写、POST 整页跳转等)统一沉淀在 SKILL.md「排障与稳定套路」,此处不重复。

### domain: www.airchina.com.cn (2026-10-21 验证)

#### 入口/URL 模式
- 首页订票表单 → 结果页 URL 模式非常干净,**可直达**:`https://www.airchina.com.cn/flight/oneway/{出发三字码小写}-{到达三字码小写}/{YYYY-MM-DD}`,如 `/flight/oneway/pek-sha/2026-10-22`。
- 首页表单:出发/到达输入框 placeholder 为 `出发机场`/`到达机场`,选中后 placeholder 会变(到达框点击后变成"输入城市或机场三字码"),日期框 placeholder 会变成 `请选择日期`。

#### 全价经济舱位置
- 列表页每行 4 个价格格(头等/公务/超级经济/经济),class 含 `cabinContent_cabin`,按 x 坐标 648/780/912/1044 排列,显示的是"¥xxxx 起"。
- **点击经济舱价格格**,行下方展开预订条:显示 `经济全价(Y舱)`、退改费、行李额 20KG、里程累积、`¥xxxx`,以及关键证据行 **"无折扣公布运价:北京首都-上海虹桥经济舱Y舱 ¥ 2150"**。这就是报销截图要的同屏证据。

#### 已知陷阱
- 进结果页先弹 1~3 条公告,按钮是"确认,查看下一个提示",要连点到消失;停留久了还会弹"停留时间过长"提示(我知道了)。
- 点"预订"要登录,不需要——展开价格条就有全价证据,不要进订票流程。
- **当天的日期在日历上是禁选态**(class 含 `calendarCellDisabled`),顺延一天即可;双月日历点日期时注意别点到相邻月的同号(有 `calendarCellOther` class 的是邻月格)。
- 日期框/城市框点击后 placeholder 会变,选择器要用当前 placeholder 或坐标定位。

### domain: www.ceair.com (2026-10-21 验证)

#### 入口/URL 模式
- 首页 `https://www.ceair.com/zh/cny/home`,订票表单在 `.search-form`(出发/到达/日期 + 搜索按钮)。
- 结果页 URL 模式:`https://www.ceair.com/zh/cny/shopping/oneway/SHA,PVG-PEK,PKX,QIP(R).../2026-10-22`(城市对展开为全部机场组合,逗号分隔)。从首页 GUI 提交一次即可拿到;城市级选择(如"北京 BJS")会覆盖全部机场。
- 首页页面宽 1215px,视口 800px 放不下表单,先 `zoom 0.62` 再操作。

#### 全价经济舱位置
- 结果页每行右侧 3 个价格格(经济舱/超级经济舱/公务头等,class `cabin-level-item`,可点的带 `pointer`),显示最低价。
- **点击经济舱价格格**,行下方展开横向产品卡条(约 3300px 宽,可横向滚动):从 6.7 折到全价逐档排列,最后是 **"经济舱全价"** 卡(有座、退票/改升费、含20KG托运行李、不含税价 ¥xxxx、订购按钮)。报销证据 = 经济舱全价卡 + 航班行同屏。
- 卡条内定位全价卡:`[class*=fare-title-text]` 中文本为"经济舱全价"的元素,再向上爬到含"不含税价"的祖先即完整卡片。

#### 已知陷阱
- 首次进结果页弹"安心出行"公告(防诈骗+行李须知),点"我知道了"。
- 航班号在 DOM 里可能拆开(innerText 出现 "MU\n5137"),找行用 `/MU\s*\n?\s*5137/`;行容器 class 含 `shopping-parent-item-container`,61 个元素多对一(嵌套),隐藏无关行时对这些容器逐个判断,跳过目标行及其祖先/后代。
- 构图参考(已产出合格截图):zoom 0.58 + 隐藏无关航班行 + 滚动到页头,一屏 = "上海→北京 2026年10月22日" 日期条 + MU5137 行 + 经济舱全价卡。
- 东航的日期条**当天(10-21)可选**(国航当天禁选),但默认仍建议今天不可用就顺延。

### domain: b2c.csair.com / www.csair.com (2026-10-21 验证)

#### 入口/URL 模式
- 首页 `https://www.csair.com/cn/index.shtml`,订票表单字段有干净 ID:`#fDepCity` / `#fArrCity` / `#fDepDate`。
- **城市输入不能只靠 setter 赋值**——必须点击输入框弹出城市面板(`a.ui-city-link`,城市码如 `city-CAN`/`city-BJS`),点选面板里的城市,内部状态才算选中;否则点"立即查询"无反应。
- 结果页 URL 模式(GET 参数,可直达):`https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CAN&c2=BJS&d1=2026-10-22&at=1&ct=0&it=0&b1=CAN&b2=PEK-PKX&orderChannel=JPSS-YDXC`(c1/c2 城市码,d1 日期,b1/b2 机场组合,b2 可写 `PEK-PKX` 覆盖双机场)。

#### 全价经济舱位置
- 结果页每行 4 个价格格:`li.zls-cabin-cell`(头等/公务/明珠经济/经济,禁用带 `disabled` class),航班信息块 `div.zls-flight-cell`。
- **点击经济舱价格格**,行下展开产品列表:折扣经济舱(K舱 x折)→ 优选经济舱(H舱)→ **"全价经济舱 | Y 舱 | 全 价"**,每档含里程、退改、行李额和"立即选购"。全价档价格即 Y 舱公布运价(广州-北京 ¥3060)。

#### 已知陷阱
- 进结果页弹"温馨提示"(进京无人机管控等),点"继续"。
- "立即查询"是 `href="#"` 的 `<a>`(JS 绑定);城市面板没关会盖住按钮,点击无效(表现为"点了没反应")。
- 首页点"立即查询"可能不跳转也不开新 tab;稳定做法是走通一次拿到结果页 URL 模式,之后直接拼 URL 参数直达。
- 行结构:`div.zls-flight > div.zls-flightInfoShow > div.zls-common`;隐藏无关行时对 `li.zls-flight-cell`(注意有 DIV/LI 同名 class,LI 是行)整体 `display:none`。
- 当天日期可选(10-21 仍有报价),但目标航班当天可能已起飞,建议直接顺延一天。
- 弹窗的全屏遮罩没关时,点价格格照样报 "clicked:true" 但毫无反应——点击无反应先关弹窗、再截图确认遮罩已消失。
- 展开档位的线性文本顺序是"名称→详情→立即选购→**价格**"(价格在"立即选购"后面),按顺序对应档位别错位;可用 `折扣率 × 全价 ≈ 档位价` 交叉验证读数(如 6.2折 × ¥3060 ≈ ¥1900)。

### domain: new.hnair.com / www.hnair.com (2026-10-21 验证)

#### 入口/URL 模式
- **门户 www.hnair.com 在部分网络环境直接 403**(nginx WAF,清 cookie 无效;curl 直连却 200)。订票系统在另一子域,**直接开 `https://new.hnair.com/hainanair/ibe/common/flightSearch.do`**,不走门户。
- 查询表单:起飞/到达输入框 name 为 `Search/OriginDestinationInformation/Origin|Destination/location_input`,日期框 class `calendar-input`(id 动态),城市下拉选中项 class `city-tit li-on`(文本如"城市北京BJS")。
- 搜索按钮 `a.search-btn`。**按钮旁常年悬浮客服卡通(`div.ask-me`)和 cookie 弹窗,会盖住按钮**——点击前先隐藏 `[class*=ask-me]`、`[class*=crew-mask]`、`[class*=crew-dialog]`,再用 `elementFromPoint` 确认命中。海航是老式 jQuery 站,`el.click()` 有效。
- 结果页 `https://new.hnair.com/hainanair/ibe/air/searchResults.do?...`(参数复杂,从表单走一遍即可,不手拼)。

#### 全价经济舱位置
- 每行右侧 3 个价格列:公务舱 / 超级经济舱 / 经济舱,各是 `.ticket-price`("¥xxxx 起")+ ˅ 展开钮。
- **点经济舱列展开钮**,行下出舱位表(`.dis-cabin` 组):超值折扣(K舱)/ 选购权益 / 特惠折扣(E舱)/ 基础折扣(Q舱)/ **"全价经济舱 | Y舱 | 全价 | ¥xxxx(不含税费) | 立即预订"**。可能另有"仅限本人预定"实名全价产品(brandname=FULLPRICE_REA),报销以标准 Y 舱公布价为准(北京-上海 ¥2150)。
- 部分航司(如首都航空 JD)在海航系统内档位很少(可能只有 2 档),证据行形如"**首航全价 Y舱 全价 ¥xxxx(不含税费)**"——带"全价"字样即采信,不要因为档位少而怀疑没找对。

#### 已知陷阱
- **列表内容不在 `body.innerText`/`textContent`**(容器渲染属性导致,但 outerHTML 里有):航班卡 `.flight-info` / `.flight-list-item` 可直接 querySelectorAll 后逐个读 innerText;判断加载完成以卡片数量为准。
- 航班号文本带空格:`HU 7605`,匹配用 `/HU\s*7605/`。
- 客服悬浮层/cookie 弹窗/公告弹层(crew-dialog、crew-mask)会反复出现,每次点击前都要确认命中;隐藏会被重渲染还原,必要时隐藏+点击放同一个 eval。
- 舱位明细预渲染在隐藏 HTML 里(每行 `.dis-cabin` 可达 200KB),是否展开用 `offsetParent`/`offsetHeight` 判断。
- 海航系(HU/JD/GS/8L/PN/UQ)共用此订票系统。
- **新版城市面板把事件绑在 focus 上,合成点击不触发 focus,点哪个城市都会写进错误的框**(实测"北京"被写成"三亚")。兜底做法:直接填 form 隐藏字段(`Origin/location=CITY_XXX_CN`、`location_type=true`、`location_input=中文城市名`,到达侧为 `Destination/location=...`)后 `form.submit()`,一次直达结果页。
- 航班动态/订票是 **POST 整页跳转**(如 `flightDynamicResult.do`),没有 XHR——读 `form.action`/`form.method` 确认提交方式后直接 `form.submit()`,不要等异步结果容器出现。
- 程序化给日期框设值会被日历控件回写重置(设成 10-22 又变回今天):**设值与提交放同一个 eval**,设完立刻 submit。
