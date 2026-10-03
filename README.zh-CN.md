# easy-output

一个 Agent Skill，用来提升 Agent 输出的可读性：先砍水分，再用受控英语写清楚，最后挑一个能承载
内容的最便宜介质——表格、图表、单文件网页或视频。面向解释、总结、设计文档、交接说明和 PR 描述。

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

## 工作机制

三道工序，按顺序走。前两道免费，且扛住大部分收益。

| 工序 | 做什么 | 成本 |
|---|---|---|
| **砍** | 删开场白、复述问题、结尾总结、模糊限定词；结论放第一句；并行项换成表格或列表。 | 无 |
| **写清** | 一句一个意思、主动语态、一词一义、不用名词化。ASD-STE100 开 ~80%：用它的写作规则、日常词汇、一个明确标注的比喻。 | 无 |
| **换介质** | 在这个信息密度下挑最合适的介质。 | 分钟到小时 |

可选介质：

| 档位 | 输出 | 增加什么 | 成本 |
|---|---|---|---|
| 0 | 聊天文字 | 快、可 diff、可 grep | 秒 |
| 1 | 受控且精简的文字 | 清晰与简洁同时到位 | 无 |
| 2 | 图表 | 结构、压缩 | 分钟 |
| 3 | 单文件可交互 HTML | 探索、调参、自控节奏的动画 | 数十分钟 |
| 4 | 定制讲解视频 | 叙事、运动、节奏 | 小时级，外加 TTS |

0–2 档覆盖大部分请求。第 3 档适合读者需要动手探索的内容。第 4 档为选装：当内容本身是"随时间展开
的隐形机制"时，Agent 才会提议，并先问成本。

## 用法

请求解释、或者指出输出难读时，skill 自动触发；它也会在 Agent 把过长的草稿发出去之前主动介入。

```
解释一下 TCP 慢启动。                          → 第 1 档：狠砍，加一张图
这份文档四页了，我还是没看懂。                  → 砍掉三分之一，重新组织结构
把我们的重试/退避逻辑做成能动手玩的网页。        → 第 3 档
做一个 90 秒 3b1b 风格的特征值讲解视频。        → 第 4 档，先问成本
健康检查用哪个端口？                          → 一行
```

每档的可复制提示词在 [`references/prompt-templates.md`](references/prompt-templates.md)，
第 1 条就是"砍"这一道。

## 目录结构

```
easy-output/
├── SKILL.md                    # 阶梯、10 条规则、5 个选档问题、路由表
└── references/
    ├── conciseness.md          # 砍：结论先行、长度预算、手法、反模式
    ├── writing.md              # ASD-STE100 规则、80% 旋钮、改写对照
    ├── diagrams.md             # 关系 → 图型；ASCII、Mermaid、SVG
    ├── html-pages.md           # 单文件契约、交互模式
    ├── video-explainers.md     # 拆解 3b1b、音频优先的时序、TTS 方案与许可证
    ├── prompt-templates.md     # 每档提示词，"砍"放第一条
    ├── checklist.md            # 每档交付前的验收清单
    └── spirit.md               # 原始帖子、10 条原则、护栏
```

`SKILL.md` 负责路由，只在对应档位需要时才引入某个 `references/` 文件。

## 常驻规则

- 先砍。150 字能说清却写了 900 字，问题在文字本身；图表很难救回来。
- 交付前验证。拿规则回读草稿；打开 HTML、渲染 Mermaid、看粗剪、对齐音频与分镜时长。环境验证不了
  的格式，就交付更朴素、能验证的那个。
- 贵的工序先问。第 4 档是分钟到小时级，由用户拍板成本。
- 产物保持诚实。数字带单位和来源，坐标轴标注，引用回到一手来源核对。
- 凭据从环境变量读（`ELEVENLABS_API_KEY`）。
- 专门的图表/文档 skill 改变某一档*怎么做*；档位本身不动。

## 出处

提炼自 Andrej Karpathy 2026 年 10 月 2 日关于理解 LLM 输出的帖子：
<https://x.com/karpathy/status/2105819303471976479>，全文见
[`references/spirit.md`](references/spirit.md)。本仓库是一份独立解读，作者未审阅、未背书。
可读性与简洁优先的取向、以及第 4 档的选装定位，是本仓库自己的编辑判断。

ASD-STE100 由 ASD 在 <https://www.asd-ste100.org/> 发布；
[`references/writing.md`](references/writing.md) 为实用目的转述了其中广为人知的规则。

3Blue1Brown、Manim、ElevenLabs、Kokoro、Piper、XTTS、Remotion 均为各自所有者财产，此处为描述性引用。

## 许可证

[MIT](LICENSE)。

## 参与贡献

欢迎 issue 和 PR，做小一点。比较受欢迎的贡献：一条实践验证过的精简手法、更利落的 STE 改写对照、
一个真抓到过问题的验收步骤、或修正某个工具/许可证细节。请保持零依赖、`SKILL.md` 精简，以及这份
README 简短——它是最先被读到的东西。
