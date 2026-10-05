# easy-output

一套让 Agent 写出的文档**几分钟内可读、同时密到能直接开工**的 agent skill。一条法条，五个文档形态，两个渲染器。

法条是 [Karpathy 那句话](https://x.com/karpathy/status/2105819303471976479)的压缩：我们往后花在读模型产出上的
时间，会多于写给模型的时间。一份文档只有在短到能读完、清楚到能照着做的时候，才配得上这段时间。十二条，每条
一个能数的阈值：[`RULES.md`](RULES.md)。

遵循 [Agent Skills](https://agentskills.io/) 格式。纯 Markdown，运行时不带任何依赖。

[English →](README.md)

## 安装

```bash
npx skills add yejianqin61-cell/easy-output -g
```

这就是 [Vercel Labs 的 `skills` CLI](https://github.com/vercel-labs/skills)。它解析仓库，找出 `skills/` 下的
每一个 `SKILL.md`。然后装到它检测到的所有 agent：Claude Code、Codex、Cursor、OpenCode 等约 75 种。

```bash
npx skills add yejianqin61-cell/easy-output --list                 # 先预览
npx skills add yejianqin61-cell/easy-output -g -a claude-code -y   # 只装一个 agent
npx skills use yejianqin61-cell/easy-output --skill easy-audit --agent claude-code
```

`-g` 装到全局，也就是所有项目。去掉则装进当前项目的 `./.claude/skills/`。安装走软链接，clone 里 `git pull`
就等于更新；环境不支持软链接时加 `--copy`。

手动安装：clone 仓库，把 `skills/<bucket>/<name>` 软链到你的 agent skills 目录。

## 有哪些 skill

| skill | 做什么 |
|---|---|
| [easy-audit](skills/documents/easy-audit/SKILL.md) | 完成度、缺陷、一缺陷一计划 |
| [easy-summary](skills/documents/easy-summary/SKILL.md) | 变的是什么、意味着什么、还开着什么 |
| [easy-plan](skills/documents/easy-plan/SKILL.md) | 需求排成 phase，每个结束在能演示的地方 |
| [easy-task-act](skills/documents/easy-task-act/SKILL.md) | 一条任务一份简报，一条任务一次提交 |
| [easy-registry](skills/documents/easy-registry/SKILL.md) | 一条事项一行，反复修改中保持当前 |
| [easy-diagram](skills/render/easy-diagram/SKILL.md) | 一句判断一张图：ASCII、Mermaid 或 SVG |
| [easy-report](skills/render/easy-report/SKILL.md) | 文档渲染成单文件 HTML 页 |

完整的约定在各自的 `SKILL.md` 里，这张表只是目录。

链路是审计、计划、任务与执行。`easy-audit` 点出缺陷与计划，`easy-plan` 把需求排成 phase，
`easy-task-act` 写简报并落地。`easy-summary` 收口这一轮，`easy-registry` 存着还没人动手的那些。

每个会产出文档的形态，都在开写前问一次：要 Markdown 还是单文件 HTML 报告。渲染交给 `easy-report`。

调研文档不在本仓范围内，那个形态已经由 Matt Pocock 的 `research` skill 承担。

## 阶梯

Karpathy 那篇帖子的骨架是四级阶梯，每一级都用同一句话衔接："But even better"。介质是一个变量，**最便宜的、
能完全打开内容所需通道的那一档**胜出。

| 档 | 在本仓 |
|---|---|
| 1. 受约束、砍过的散文 | 法条本身：[`RULES.md`](RULES.md)，每个形态 skill 自带一份。 |
| 2. 图 | [easy-diagram](skills/render/easy-diagram/SKILL.md)，放进文档，或本身即产物。 |
| 3. 网页 | [easy-report](skills/render/easy-report/SKILL.md)，文档渲染进一张固定模板。 |
| 4. 解说视频 | 主动出界：本仓的读者是在审批文档，不是在看看解。 |

原文作者最看好第 4 档，本仓不承载它。需要读者引用、检索、核对精度的地方，文字仍是最合适的介质。

## 语言

skill 一律用英语写。每个 skill 和每份根目录文档都有并列的中文对照，命名 `<name>.zh-CN.md`，例如
[`RULES.zh-CN.md`](RULES.zh-CN.md) 和
[`SKILL.zh-CN.md`](skills/documents/easy-audit/SKILL.zh-CN.md)。对照供人阅读，运行时不起作用。

这些 skill 产出的文档，用你正在用的语言写。skill 把固定下来的词用英语给出，并交代 agent 翻译一次、全篇统一。

## 检查本仓

```bash
python tools/check.py            # 全部门
python tools/check.py prose      # 只跑一门
python tools/check.py --report   # 打印指标表
```

四道门守住本仓做出的承诺：法条有六份副本，必须一致；每条相对链接必须能解析；每份文档必须守住能数字数的条款；
每个 skill 必须可安装。见 [`tools/README.md`](tools/README.md)。

## 目录结构

```
easy-output/
├── RULES.md                      # 可读性法条：十二条与各自阈值
├── RULES.zh-CN.md                # 同一份法条的中文对照
├── CLAUDE.md                     # 本仓的 skill 写作约定
├── tools/                        # check 命令与它的指标库
├── parked/                       # 已退役材料，不进安装
└── skills/
    ├── documents/                # 一种文档形态一个 skill
    │   ├── easy-audit/           SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   ├── easy-summary/         SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   ├── easy-plan/            SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   ├── easy-task-act/        SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   └── easy-registry/        SKILL.md + SKILL.zh-CN.md + agents/ + references/
    └── render/                   # 把文档变成另一种介质
        ├── easy-diagram/         SKILL.md + SKILL.zh-CN.md + agents/ + references/
        └── easy-report/          SKILL.md + SKILL.zh-CN.md + agents/ + references/
```

五个文档 skill 各自在 `references/readability-law.md` 自带一份法条，因为 skill 是各自独立安装的。两个渲染
skill 不带：它们渲染的文档本来就已经守了法条。`easy-report` 拥有 `references/report-template.html`、
填写规范和渲染闸门；`easy-diagram` 拥有载体规则。

## 出处

法条来自 Andrej Karpathy 2026 年 10 月 2 日关于 LLM 输出的帖子：
<https://x.com/karpathy/status/2105819303471976479>，全文见 [`parked/spirit.md`](parked/spirit.md)。
文档形态建立在 Matt Pocock 的 [`to-spec`](https://github.com/mattpocock/skills) 之上，`easy-audit` 改写自
他的 `code-review`（MIT）。两位作者均未审阅或背书本仓库。

## 许可证

[MIT](LICENSE)。

## 参与贡献

小改动最容易落地：法条里更利落的对照改写、一个真正扛得住评审的文档形态、一个真抓到过问题的检查步骤、
或修正某个事实或许可证细节。请保持零依赖、每个 `SKILL.md` 精简，以及这份 README 简短。
