# Changelog

本文件记录方法论与证据政策的变更;站点经验变更见 [references/airlines.md](references/airlines.md) 与各实测报告,不在此逐条列出。

## [1.1.0] - 2026-10-22

- 第二轮 24 家航司全量复测(11 家明确全价,4 家较第一轮升级),新增 [复测报告](references/live-tests-retest-20261021.md) 与阻塞类别/复试策略索引。
- 明确"禁止篡改证据"与"提交方式"的边界:控件状态机阻塞时允许等价程序化提交(设值+submit 同 eval,注明提交方式);UI 纯路径优先。
- 宿主工具层经验独立成 [references/tooling-notes.md](references/tooling-notes.md),与站点事实(airlines.md)、方法论(SKILL.md)三层分离。
- 登录墙航司(G5/GJ/BK/DZ)写明接续要求与官方登录入口。
- SKILL.md frontmatter 增加 version/updated 字段;新增 README CI badge。

## [1.0.0] - 2026-10-21

- 首个公开版本:查询流程与证据规则、24 家航司入口与站点经验、两轮实测中的第一轮、离线校验与 CI。
