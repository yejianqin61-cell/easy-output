# easy-output

让 Agent 产出的工程文档**几分钟内可读，同时密到能直接开工**：项目分析、评估、施工计划、规格、ADR、
操作手册。结论先行，标题就是读者的问题，给出明确的 scope 边界，写作按 ASD-STE100 约 80% 强度执行。

底座是 Andrej Karpathy 关于 LLM 输出的建议，落在"人要审批的文档"上；在 Matt Pocock 的
[`to-spec`](https://github.com/mattpocock/skills) 之上加一层可读性。

遵循 [Agent Skills](https://agentskills.io/) 格式。纯 Markdown，无脚本、无依赖。

[English →](README.md)

## 安装

```bash
npx skills add yejianqin61-cell/easy-output -g
```

这就是 [Vercel Labs 的 `skills` CLI](https://github.com/vercel-labs/skills)：解析仓库、读取根目录的
`SKILL.md`，并装到它检测到的所有 agent——Claude Code、Codex、Cursor、OpenCode 等 75+ 种。

```bash
npx skills add yejianqin61-cell/easy-output -g -a claude-code -y    # 指定 agent，非交互
npx skills add yejianqin61-cell/easy-output --list                  # 预览仓库内容
npx skills use yejianqin61-cell/easy-output --skill easy-output --agent claude-code
npx skills update easy-output
npx skills remove easy-output
```

`-g` 装到全局（所有项目）；去掉则装进当前项目的 `./.claude/skills/`。安装走软链接，所以 clone 里
`git pull` 就等于更新 skill；环境不支持软链接时加 `--copy`。

手动安装：

```bash
git clone https://github.com/yejianqin61-cell/easy-output.git ~/.claude/skills/easy-output   # 全局
git clone https://github.com/yejianqin61-cell/easy-output.git .claude/skills/easy-output     # 项目级
```

## 产出什么

| 文档 | 读者 | 回答什么问题 |
|---|---|---|
| **项目分析** | 决定投入资源的人 | 现状如何、代价多少、建议怎么办 |
| **评估** | 决策者 | 哪个方案胜出、按什么标准、什么条件下结论翻转 |
| **施工计划** | 执行者与审批者 | 做什么、按什么顺序、怎么算完成 |
| **规格** | 实现它的 agent，以及评审的人 | 什么问题、什么方案、哪些决策已锁 |
| **ADR** | 未来的维护者 | 为什么是现在这样 |
| **操作手册** | 在时间压力下操作的人 | 怎么执行、怎么回滚、怎么判断坏了 |

六种文档的骨架、章节清单和长度预算都在 [`references/documents.md`](references/documents.md)。

## 文档契约

八条，所有类型通用。第一条决定这份文档能不能被批：

1. **结论先行。** 建议、代价、主要风险、需要读者做什么，全部落在前 ≤150 字里。评审者看到这里
   停下，也知道文档站在哪一边。
2. 标题就是读者的问题，顺序按读者提问的顺序排。
3. 一屏一个意思。
4. 有明确的 out of scope 章节，写清主动放弃的东西。
5. 假设标注为假设；未决问题各配一条解决路径。
6. 数字带单位、来源和日期。
7. 顶部一行状态：类型、日期、状态、本文档锁定哪些决策。
8. 正文密，表面可导航——摘要和标题就是给人用的接口。

## 工作机制

四步，按顺序。前三步免费。

| 工序 | 做什么 |
|---|---|
| **砍** | 删开场白、复述问题、结尾总结、模糊限定词；并行项用表格替掉段落。 |
| **写清** | 一句一个意思、主动语态、一词一义、不用名词化。ASD-STE100 开 ~80%：写作规则、日常词汇、一个明确标注的比喻。 |
| **定形** | 选文档类型、写结论、把标题排成读者的问题、划出 scope 边界。 |
| **呈现** | 用表格和一到两张图替掉段落；文档会被反复读或转发时，渲染成单文件 HTML 报告。 |

档位共 0–3：几句话、砍过的文档、文档加结构、文档加 HTML 报告。第 1 档扛住主要价值。
**停在读者能批准这份文档的那一档。**

## 用法

请求写文档、或者指出某份文档读不下去时，skill 自动触发；它也会在 Agent 把过长的草稿发出去之前主动介入。

```
写一份我们认证层的分析，并给出建议。            → 项目分析，结论先行
评估这三个消息队列服务，看哪个适合我们。          → 评估：标准与权重先于打分
写一份从 RabbitMQ 迁移的施工计划。              → 分阶段、每阶段验证、回滚前置
把我们刚定的东西写成规格。                     → 规格 + 决策摘要
当初为什么选 Postgres？写下来。                 → ADR，一个决策
这份文档四页了，我还是没法批。                  → 砍掉三分之一，结论提到最前
解释一下 TCP 慢启动。                         → 次要场景：结论 + 一张图
```

每种文档的提示词在 [`references/prompt-templates.md`](references/prompt-templates.md)。

## 目录结构

```
easy-output/
├── SKILL.md                    # 阶梯、10 条规则、5 个选档问题、路由表
└── references/
    ├── documents.md            # 文档契约 + 六种文档形态
    ├── conciseness.md          # 砍：结论先行、长度预算、手法、反模式
    ├── writing.md              # ASD-STE100 规则、80% 旋钮、改写对照
    ├── diagrams.md             # 关系 → 图型；ASCII、Mermaid、SVG
    ├── html-report.md          # 单文件报告契约、打印样式、交互
    ├── prompt-templates.md     # 每种文档的提示词，"砍"放第一条
    ├── checklist.md            # 评审者的第一遍通读清单
    └── spirit.md               # 原始帖子、原则、本仓库从中取用了什么
```

`SKILL.md` 负责路由，只在对应档位需要时才引入某个 `references/` 文件。

## 常驻规则

- 结论先行。结论躺在最后一页的文档，会被退回来。
- 先砍再装饰。150 字能说清却写了 900 字，问题在文字本身。
- 标准先于打分。没有翻转条件的评估，是伪装成表格的游说。
- 回滚先于开工。没有逐阶段验证的计划，别人照着执行不了。
- 假设要标注，数字要带来源，scope 要有边界。
- 交付前自己走一遍"评审者第一遍通读"，报告要先打开看过。
- 超过几分钟的渲染先问一声；凭据从环境变量读。

## 出处

两个来源。写作标准来自 Andrej Karpathy 2026 年 10 月 2 日关于 LLM 输出的帖子：
<https://x.com/karpathy/status/2105819303471976479>，全文见
[`references/spirit.md`](references/spirit.md)。文档形态建立在 Matt Pocock 的
[`to-spec`](https://github.com/mattpocock/skills)（MIT）之上——它把对话变成给实现 agent 用的规格，
本仓库补上"让同一份文档对人可审计"这一层。两位作者均未审阅或背书本仓库。

ASD-STE100 由 ASD 在 <https://www.asd-ste100.org/> 发布；
[`references/writing.md`](references/writing.md) 为实用目的转述了其中广为人知的规则。

## 许可证

[MIT](LICENSE)。

## 参与贡献

欢迎 issue 和 PR，做小一点。比较受欢迎的贡献：更利落的 STE 改写对照、一个真正扛得住评审的文档形态、
一个真抓到过问题的验收步骤、或修正某个事实或许可证细节。请保持零依赖、`SKILL.md` 精简，以及这份
README 简短——它是最先被读到的东西。
