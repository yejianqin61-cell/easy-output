# easy-output

**先保证好读。图表和网页在需要时才上场。视频要你开口才做。**

一个 Agent Skill，让编码 Agent 产出人能真正读得下去的内容：**先砍，再写清楚**（ASD-STE100，
可用更软的"80% 强度"设置），只有当图表或单文件网页比它替代的文字读起来更快时，才换介质。

纯 Markdown。没有脚本、没有依赖、不需要构建。

[English →](README.md)

---

## 问题在哪

模型输出很少是错的，问题是**不清楚**和**太长**。两个毛病，而提示词通常一个都没管：

- **清晰度** —— 句子过长、一句里塞三个意思、同义词在段落中途换了含义。
- **简洁度** —— 开场白、复述问题、结尾总结、模糊限定词，以及 150 字能说清却写了 900 字。

换介质有帮助（一张图能替掉两段话），但那是**第三步，不是第一步**。这个 skill 强制这个顺序：
**先砍，再写清楚，最后才考虑换介质。**

## 输出阶梯

| 档位 | 介质 | 换来什么 | 成本 | 定位 |
|---|---|---|---|---|
| 0 | 聊天文字 | 快、可 diff、可 grep | 秒 | 一句话事实 |
| 1 | 受控且精简的文字（ASD-STE100） | 清晰**加上**简洁，一词一义 | 几乎为零 | **本体** |
| 2 | 图表 | 并行结构、关系、压缩 | 分钟 | 辅佐 |
| 3 | 单文件可交互 HTML | 探索、调参 | 数十分钟 | 辅佐 |
| 4 | 定制讲解视频 | 叙事、运动、节奏 | 小时级，需要音频 | **仅在你主动要求时** |

0–2 档覆盖了几乎所有请求。第 3 档留给读者必须动手探索的内容。**第 4 档是刻意的例外**——
只有当内容本身是"随时间展开的隐形机制"，且用户同意成本时才提。见[视频的定位](#视频的定位)。

---

## 安装

### 一行指令（推荐）

```bash
npx skills add yejianqin61-cell/easy-output -g
```

这就是 [Vercel Labs 的 `skills` CLI](https://github.com/vercel-labs/skills)，agent skill 生态的包管理器。
它会解析仓库、读取仓库根目录的 `SKILL.md`，并安装到它检测到的所有 agent —— Claude Code、Codex、
Cursor、OpenCode 等 75+ 种。

```bash
# 全局（所有项目）——就是上面这条；去掉 -g 则装进当前项目的 ./.claude/skills/
npx skills add yejianqin61-cell/easy-output -g

# 指定 agent，非交互
npx skills add yejianqin61-cell/easy-output -g -a claude-code -y

# 只预览仓库里有什么，不安装
npx skills add yejianqin61-cell/easy-output --list

# 不安装，直接用一次
npx skills use yejianqin61-cell/easy-output --skill easy-output --agent claude-code

# 之后
npx skills update easy-output
npx skills remove easy-output
```

默认用**软链接**安装，所以更新仓库就等于更新 skill；如果你的环境不支持软链接，加 `--copy`。

> 本仓库地址：<https://github.com/yejianqin61-cell/easy-output>。

### 手动安装

```bash
git clone https://github.com/yejianqin61-cell/easy-output.git ~/.claude/skills/easy-output   # 全局
git clone https://github.com/yejianqin61-cell/easy-output.git .claude/skills/easy-output     # 项目级
```

Windows 下对应 `%USERPROFILE%\.claude\skills\easy-output` 和 `.claude\skills\easy-output`。
任何遵循 Agent Skills 约定的 harness（一个含 `SKILL.md`、frontmatter 带 `name` 和 `description`
的文件夹）都一样能用。

验证：问你的 Agent *"你有哪些 skill？"*；然后试 *"解释一下 TCP 慢启动"*，
或者 *"这份文档太长了，帮我改成能读的"*。

### 需要自己发一个 npm 包吗？

**不需要。** `npx skills add` 直接读公开仓库，所以"发布"就是一次 `git push`——没有包要维护版本，
没有 `bin` 脚本要伺候，也不会出现仓库和 npm 版本不一致。

如果你以后想要更短的 `npx easy-output`，或者想在 npmjs.com 上有个页面：`easy-output` 这个名字在
npm 上**没被占用**。那需要加一个 `package.json` 和一个小的安装脚本 `bin`，并且每次改动都重新发布。
可行，但对大多数人来说是重复建设——上面那个 CLI 才是生态标准。

---

## 用法

当你要求"讲明白"或者抱怨"读不下去"时，skill 会自动触发；它也被有意写成会**主动**触发——
在 Agent 把一份冗长、堆砌的草稿发出去之前先自己收拾一遍。

```
解释一下 TCP 慢启动。                        → 第 1 档，狠砍，加一张图
这份文档四页了，我还是没看懂。                → 第 1 档：砍掉三分之一，重新组织结构
把我们的重试/退避逻辑讲清楚，做成能动手玩的网页。 → 第 3 档
做一个 90 秒 3b1b 风格的特征值讲解视频。        → 第 4 档，且只因为你主动要
健康检查用哪个端口？                          → 第 0 档：一行
```

每一档都有可直接复制粘贴的提示词模板，包括"先只给脚本、不渲染"这种省成本的闸门：
[`references/prompt-templates.md`](references/prompt-templates.md)。

---

## 目录结构

```
easy-output/
├── SKILL.md                        # 阶梯、10 条规则、5 个选档问题、路由表
└── references/
    ├── conciseness.md              # 先砍：结论先行、长度预算、手法、反模式
    ├── writing.md                  # 清晰度：ASD-STE100 规则、80% 旋钮、改写对照
    ├── diagrams.md                 # 关系→图型，ASCII / Mermaid / SVG
    ├── html-pages.md               # 单文件契约、交互模式
    ├── video-explainers.md         # 选装档：拆解 3b1b、音频优先、TTS 许可证
    ├── prompt-templates.md         # 可复制提示词（第一条就是"先砍"）
    ├── checklist.md                # 每档的交付前验收清单
    └── spirit.md                   # 原始帖子 + 10 条原则 + 护栏
```

采用渐进式加载：`SKILL.md` 只放选档逻辑，并路由到 `references/`，
Agent 只加载当下需要的那部分深度。

---

## 视频的定位

视频是第 4 档：最贵、最难改、最容易过度生产。它在这个 skill 里，是因为 Karpathy 的原帖看好它，
也因为它有时确实是对的答案。**但它不是这个 skill 的目的。**
如果你发现自己在用第 4 档去解决"删掉 30% 文字就能解决"的问题，那就是读错了这个 skill。

## 设计原则

- **先砍，再装饰。** 如果 150 字能说清的事写了 900 字，问题从来不在介质。
- **没验证就不交付。** 交付前先拿规则回头读自己的草稿；打开 HTML、渲染 Mermaid、看粗剪、量音频时长。
  验证不了的格式，就换一个能验证的、更朴素的格式。
- **贵的那一档要先问。** 视频是分钟到小时级成本，由用户决定。
- **拒绝过度产出。** 为一句事实做 90 秒视频，比那一句话更糟。专门的图表/文档 skill 只改变*怎么做*，
  永远不改变*选哪一档*。
- **介质不能说谎。** 数字要带单位和来源，坐标轴要标注，生成画面不能伪装成真实影像，
  引用要在交付前回到一手来源核对。
- **绝不把密钥写进产物。** 运行时从环境变量读 `ELEVENLABS_API_KEY`。

---

## 出处与致谢

这里压缩的思想来自 Andrej Karpathy 于 2026 年 10 月 2 日发布的单条帖子：
<https://x.com/karpathy/status/2105819303471976479>（全文引用见
[`references/spirit.md`](references/spirit.md)，因 x.com 需要登录，文本取自公开的第三方 unroll）。
本 skill 本身是一份独立的解读——尝试把一位人类专家的经验变成 Agent 可重复执行的流程——
**并非由他撰写、审阅或背书**。其中的编辑取向（可读性与简洁优先、视频放最后且需主动选装）是本
skill 自己的判断，见 [spirit.md 的"本 skill 如何权衡四档"](references/spirit.md)。

ASD-STE100 是由 ASD 发布的标准，可在 <https://www.asd-ste100.org/> 免费下载。
本仓库不转载其正文；`references/writing.md` 只是为实用目的转述了其中广为人知的规则。

3Blue1Brown、Manim、ElevenLabs、Kokoro、Piper、XTTS、Remotion 等均为各自所有者的财产，此处仅为描述性引用。

## 许可证

[MIT](LICENSE)。发布前请把版权持有者替换为你自己的名字或 ID。

## 参与贡献

欢迎 issue 和 PR——**并且请把 PR 做小**。有价值的贡献包括：一条真的管用的精简手法、更好的 STE 改写对照、
一个真的抓到过问题的验收步骤、或修正某个工具/许可证细节。请保持零依赖、保持 `SKILL.md` 精简，
也请保持仓库自己的文字简短：README 是读者看到的第一样东西，所以它就是我们第一个被检验的地方。
