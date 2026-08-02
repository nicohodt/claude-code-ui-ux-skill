# Claude Code UI/UX 技能 — 面向 Claude、Cursor 与 Windsurf 的 AI 设计智能

**让 AI 生成的界面真正好看的开源 Claude 技能。** 与其指望模型猜出一个像样的设计，这个技能直接给它一个可检索的设计智能数据库 —— **84 种 UI 风格、192 套配色方案、74 组字体配对、99 条 UX 指南、161 条行业推理规则，以及覆盖 22 种技术栈的 25 种图表类型** —— 并用一个生成器把任意产品需求转化成完整、具体的设计系统。

专为 **[Claude Code](https://claude.com/product/claude-code)** 打造，同时兼容 Cursor、Windsurf、GitHub Copilot、Codex、Gemini CLI 等 19 款 AI 编程助手。

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/README.md">🇺🇸 English</a> |
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/README.zh.md">🇨🇳 简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/releases"><img src="https://img.shields.io/github/v/release/nicohodt/claude-code-ui-ux-skill?style=for-the-badge&color=blue" alt="最新版本"></a>
  <img src="https://img.shields.io/badge/推理规则-161-green?style=for-the-badge" alt="161 条推理规则">
  <img src="https://img.shields.io/badge/UI_风格-84-purple?style=for-the-badge" alt="84 种 UI 风格">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/nicohodt/claude-code-ui-ux-skill?style=for-the-badge&color=green" alt="MIT 许可证"></a>
</p>

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/nicohodt/claude-code-ui-ux-skill/tests.yml?branch=main&style=flat-square&label=tests" alt="测试状态"></a>
  <img src="https://img.shields.io/badge/自动化测试-192-brightgreen?style=flat-square" alt="192 个自动化测试">
  <img src="https://img.shields.io/badge/WCAG-CI_强制校验-success?style=flat-square" alt="CI 强制校验 WCAG 对比度">
  <img src="https://img.shields.io/badge/依赖-0-success?style=flat-square" alt="零 Python 运行时依赖">
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/ui-ux-pro-max-cli"><img src="https://img.shields.io/npm/v/ui-ux-pro-max-cli?style=flat-square&logo=npm&label=CLI" alt="npm 版本"></a>
  <a href="https://www.npmjs.com/package/ui-ux-pro-max-cli"><img src="https://img.shields.io/npm/dm/ui-ux-pro-max-cli?style=flat-square&label=downloads" alt="npm 月下载量"></a>
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22"><img src="https://img.shields.io/github/issues/nicohodt/claude-code-ui-ux-skill/good%20first%20issue?style=flat-square&color=7057ff&label=新手友好任务" alt="新手友好任务"></a>
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/graphs/contributors"><img src="https://img.shields.io/github/contributors/nicohodt/claude-code-ui-ux-skill?style=flat-square&label=贡献者" alt="贡献者"></a>
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/stargazers"><img src="https://img.shields.io/github/stars/nicohodt/claude-code-ui-ux-skill?style=flat-square&logo=github" alt="GitHub stars"></a>
</p>

---

## 🙌 我们期待你的 Pull Request

这个项目由贡献者共同构建 —— 每一种 UI 风格、每一套配色、每一条行业规则，都只是 CSV 文件里的一行。**不需要设计学位，不需要学习构建流程，不需要签署 CLA。**

**我们对贡献者的承诺：**

| | |
|---|---|
| ⚡ **快速回应** | 每个 PR 都会在 **48 小时内**得到首次回复。不会有 PR 石沉大海。 |
| 📝 **零手续** | MIT 进，MIT 出。提交 PR，就这么简单。 |
| 🧩 **一行 CSV 就是真正的贡献** | 新增一套配色或一条 UX 规则，就是值得合并并署名的 PR。 |
| 🏆 **人人有署名** | 所有贡献者都会列入 [CONTRIBUTORS.md](CONTRIBUTORS.md) 和发布说明。 |
| 💬 **欢迎提问** | 第一个 PR 卡住了？[开一个 Discussion](https://github.com/nicohodt/claude-code-ui-ux-skill/discussions) —— 我们宁愿帮你，也不想看你放弃。 |
| 🎁 **永久免费** | 没有付费版，没有付费数据，没有"企业版"。所有内容都在这个仓库里。 |

**从这里开始：**

- 🌱 [**新手友好任务**](https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) —— 范围明确的小任务
- 🆘 [**需要帮助**](https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) —— 我们暂时顾不上的大块工作
- 📖 [**CONTRIBUTING.md**](CONTRIBUTING.md) —— 从 fork 到合并的 5 分钟路径
- 💡 [**贡献方向清单**](#-我们现在最需要什么) —— 具体的心愿单

> **第一次参与开源？** 这是一个刻意设计得对新人友好的仓库。最有价值的贡献是 CSV 文件里的纯文本 —— 不需要写 TypeScript，不需要写 Python，不需要配置任何工具链。

---

## 这个技能解决什么问题

AI 编程助手很擅长写组件，却很不擅长决定这些组件应该长什么样。放任不管，它们会收敛到同一个结果：紫色渐变、到处 16px、没有焦点态 —— 也就是现在大家说的 *AI 味设计（AI slop）*。

这个技能补上了模型自身缺失的三件东西：

1. **一个可检索的设计知识库。** 84 种 UI 风格、192 套按行业匹配的配色、74 组字体配对、99 条 UX 指南、105 条图标条目，全部以 CSV 形式本地存储，用 BM25 + 正则混合搜索引擎查询。无 API 调用、无网络请求、无密钥。
2. **把产品映射到设计的推理规则。** 161 条行业规则，知道银行类应用不该用 AI 紫渐变，冥想类应用不该用数据密集的仪表板布局。
3. **交付前检查清单。** 对比度、焦点态、点击区域尺寸、减弱动效、响应式断点 —— 在 AI 说"完成了"之前逐项验证。

输入 *"给我的美容水疗做一个落地页"*，AI 会在写第一行 CSS **之前**先产出：

```
+----------------------------------------------------------------------------------------+
|  目标: Serenity Spa - 推荐设计系统                                                       |
+----------------------------------------------------------------------------------------+
|                                                                                         |
|  模式: 主视觉中心 + 社交证明                                                             |
|     转化策略: 情感驱动 + 信任元素                                                        |
|     CTA: 首屏之上，客户评价之后重复出现                                                  |
|     区块: 1. 主视觉  2. 服务  3. 客户评价  4. 预约  5. 联系                              |
|                                                                                         |
|  风格: 柔和 UI 进化版                                                                    |
|     关键词: 柔和阴影、微妙层次、舒缓、高级感、有机形状                                   |
|     适用于: 健康养生、美容、生活方式品牌、高端服务                                       |
|     性能: 优秀 | 无障碍: WCAG AA                                                         |
|                                                                                         |
|  配色:                                                                                  |
|     主色:    #E8B4B8 (柔粉)                                                             |
|     辅助色:  #A8D5BA (鼠尾草绿)                                                         |
|     CTA:     #D4AF37 (金色)                                                             |
|     背景:    #FFF5F5 (暖白)                                                             |
|     文字:    #2D3436 (炭灰)                                                             |
|                                                                                         |
|  字体: Cormorant Garamond / Montserrat                                                  |
|     气质: 优雅、舒缓、精致                                                               |
|                                                                                         |
|  关键效果:                                                                              |
|     柔和阴影 + 平滑过渡 (200-300ms) + 轻柔悬停态                                         |
|                                                                                         |
|  避免（反模式）:                                                                         |
|     鲜艳霓虹色 + 生硬动画 + 深色模式 + AI 紫/粉渐变                                      |
|                                                                                         |
|  交付前检查清单:                                                                         |
|     [ ] 不用 emoji 当图标（使用 SVG: Heroicons/Lucide）                                  |
|     [ ] 所有可点击元素带 cursor-pointer                                                  |
|     [ ] 悬停态带平滑过渡 (150-300ms)                                                     |
|     [ ] 浅色模式：文字对比度至少 4.5:1                                                   |
|     [ ] 键盘导航焦点态可见                                                               |
|     [ ] 遵守 prefers-reduced-motion                                                     |
|     [ ] 响应式: 375px, 768px, 1024px, 1440px                                            |
|                                                                                         |
+-----------------------------------------------------------------------------------------+
```

---

## 快速开始

### 在 Claude Code 中安装（插件市场）

```
/plugin marketplace add nicohodt/claude-code-ui-ux-skill
/plugin install ui-ux-pro-max@claude-code-ui-ux-skill
```

### 使用 CLI 安装（支持所有助手）

```bash
npm install -g ui-ux-pro-max-cli

cd /path/to/your/project
uipro init --ai claude      # Claude Code
```

然后用自然语言提出需求即可：

```
给我的 SaaS 产品做一个落地页
```

技能会自动激活 —— 不需要斜杠命令，不需要额外提示词。

### 安装到其他助手

```bash
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai copilot     # GitHub Copilot
uipro init --ai codex       # Codex CLI
uipro init --ai gemini      # Gemini CLI
uipro init --ai antigravity # Antigravity
uipro init --ai kiro        # Kiro
uipro init --ai qoder       # Qoder
uipro init --ai roocode     # Roo Code
uipro init --ai kilocode    # KiloCode
uipro init --ai trae        # Trae
uipro init --ai opencode    # OpenCode
uipro init --ai continue    # Continue
uipro init --ai codebuddy   # CodeBuddy
uipro init --ai droid       # Droid (Factory)
uipro init --ai warp        # Warp
uipro init --ai augment     # Augment
uipro init --ai codewhale   # CodeWhale
uipro init --ai all         # 一次性安装到所有助手
```

用 `--global` 一次安装、所有项目可用：

```bash
uipro init --ai claude --global   # → ~/.claude/skills/
```

其他命令：

```bash
uipro versions              # 列出可用版本
uipro update                # 从已安装的 CLI 包刷新技能文件
uipro uninstall             # 卸载技能（自动检测平台）
uipro uninstall --global    # 卸载全局安装
```

**前置要求：** Python 3.x，仅使用标准库 —— 搜索脚本不安装任何东西，也不发起网络请求。用 `python3 --version` 检查；如果缺失，请从 [python.org](https://www.python.org/downloads/) 或系统包管理器安装。这些步骤是给**你（真人用户）**的 —— 使用本技能的 AI 被明确要求绝不在你的机器上安装软件。

---

## 为什么要用设计技能，而不是直接写提示词？

| | 纯提示词 | 使用本技能 |
|---|---|---|
| **风格选择** | 训练数据的平均值 —— 通常又是紫色渐变 | 从 84 种有据可查的风格中按行业匹配 |
| **配色** | 每次现编，文件之间不一致 | 192 套配色与产品类型 1:1 对应，全项目复用 |
| **字体** | 永远是 "Inter, sans-serif" | 74 组精选配对，附 Google Fonts 导入代码 |
| **无障碍** | 你不提就不管 | 强制执行 99 条 UX 规则，交付前校验 WCAG AA 对比度 |
| **反模式** | 照抄不误 | 161 条行业规则明确写出**不该做什么** |
| **跨会话一致性** | 每次从零开始 | `--persist` 写入 `design-system/MASTER.md`，下次会话直接读取 |
| **成本** | 反复用 token 解释你的审美 | 本地 CSV 查询，零 API 调用 |

---

## 无障碍是被验证的，不只是声称的

很多设计工具都"声称"支持无障碍。在这里，它是一个会让构建失败的测试。

全部 192 套配色在每次 push 时都会在 CI 中校验：

| 校验项 | 阈值 | 状态 |
|---|---|---|
| 正文文字（`Background`/`Foreground`） | 4.5:1 — WCAG AA | ✅ 全部 192 套 |
| 卡片文字（`Card`/`Card Foreground`） | 4.5:1 — WCAG AA | ✅ 全部 192 套 |
| 组件文字（`On Primary`、`On Secondary`、`On Accent`、`On Destructive`） | 3:1 — WCAG 1.4.11 | ✅ 全部 192 套 |
| 每个颜色都是合法的 hex 或 `rgba()` | — | ✅ 已强制 |
| 边框绝不会与背景融为一体 | — | ✅ 已强制 |

这项校验发现了 14 套在中间色调上使用白色文字的配色，最低对比度仅 **2.28:1** —— 低于大号文字的底线。它们已被修复，测试也确保不会再次退化。

完整测试套件共 **192 个测试**，还覆盖 CSV 结构完整性（残缺行、重复列、序号连续性、技术栈统一 schema）、全部 12 个检索域与 22 个技术栈的搜索行为、设计系统生成，以及文档中的数字与实际数据库的一致性。

```bash
pip install pytest && pytest        # 你可以自己运行
```

把所有组件文字对比度提升到完整的 4.5:1 是[路线图的首要事项](ROADMAP.md)，也是一个很好的贡献方向。

---

## 设计系统生成器如何工作

```
┌─────────────────────────────────────────────────────────────────┐
│  1. 用户请求                                                     │
│     "给我的美容水疗做一个落地页"                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. 多域检索（5 路并行）                                          │
│     • 产品类型匹配 (192 类)                                      │
│     • 风格推荐 (84 种)                                           │
│     • 配色方案选择 (192 套)                                       │
│     • 落地页模式 (34 种)                                          │
│     • 字体配对 (74 组)                                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. 推理引擎                                                     │
│     • 产品 → UI 类别规则匹配                                      │
│     • 应用风格优先级 (BM25 排序)                                  │
│     • 过滤该行业的反模式                                          │
│     • 处理决策规则 (JSON 条件)                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. 完整设计系统输出                                              │
│     模式 + 风格 + 配色 + 字体 + 效果                              │
│     + 需避免的反模式 + 交付前检查清单                              │
└─────────────────────────────────────────────────────────────────┘
```

### 161 条行业专属推理规则

| 类别 | 示例 |
|------|------|
| **科技 & SaaS** | SaaS、微型 SaaS、B2B 服务、开发者工具/IDE、AI/聊天机器人平台、网络安全平台 |
| **金融** | 金融科技/加密货币、银行、保险、个人财务追踪、发票与账单工具 |
| **医疗健康** | 医疗诊所、药房、牙科、兽医、心理健康、用药提醒 |
| **电子商务** | 综合电商、奢侈品、二手交易平台 (P2P)、订阅盒、外卖配送 |
| **服务** | 美容/水疗、餐饮、酒店、法律、家政服务、预约与预订 |
| **创意** | 作品集、代理公司、摄影、游戏、音乐流媒体、照片/视频编辑器 |
| **生活方式** | 习惯追踪、食谱与烹饪、冥想、天气、日记、情绪追踪 |
| **新兴技术** | Web3/NFT、空间计算、量子计算、自动驾驶无人机编队 |

每条规则包含：推荐布局模式、风格优先级、配色氛围、字体氛围、关键效果，以及明确的反模式。

> **没有你所在的行业？** 那就[只差一行 CSV](CONTRIBUTING.md) —— 这是最有价值的 PR 类型之一。

---

## 功能特性

- **84 种 UI 风格** —— 玻璃拟态、粘土拟态、极简主义、粗野主义、新拟态、便当盒网格、深色模式、AI 原生 UI 等
- **192 套配色方案** —— 行业专属，与 192 种产品类型 1:1 对齐
- **74 组字体配对** —— 精选组合，含 Google Fonts 导入代码
- **25 种图表类型** —— 面向仪表板与分析场景，附图表库推荐
- **22 种技术栈** —— 各栈专属实现指南
- **99 条 UX 指南** —— 最佳实践、反模式与无障碍规则
- **161 条推理规则** —— 行业特定的设计系统生成
- **16 组 GSAP 动效预设** —— 悬停、滚动揭示、错落入场、页面转场、视差、加载
- **105 条图标条目** —— Phosphor、Heroicons、Lucide 推荐，附导入代码
- **设计旋钮** —— 用 `--variance`、`--motion`、`--density` 调节输出倾向
- **完全离线** —— CSV 数据 + Python 标准库。无 API 密钥、无遥测、无网络请求。

<details>
<summary><b>通用风格 (49)</b></summary>

| # | 风格 | 最适用于 |
|---|------|---------|
| 1 | 极简主义 & 瑞士风格 | 企业应用、仪表板、文档 |
| 2 | 新拟态 (Neumorphism) | 健康/养生应用、冥想平台 |
| 3 | 玻璃拟态 (Glassmorphism) | 现代 SaaS、金融仪表板 |
| 4 | 粗野主义 (Brutalism) | 设计作品集、艺术项目 |
| 5 | 3D & 超写实主义 | 游戏、产品展示、沉浸式体验 |
| 6 | 活力 & 块状 | 创业公司、创意机构、游戏 |
| 7 | 深色模式 (OLED) | 夜间模式应用、编程平台 |
| 8 | 无障碍 & 伦理设计 | 政府、医疗、教育 |
| 9 | 粘土拟态 (Claymorphism) | 教育应用、儿童应用、SaaS |
| 10 | 极光 UI (Aurora UI) | 现代 SaaS、创意机构 |
| 11 | 复古未来主义 | 游戏、娱乐、音乐平台 |
| 12 | 扁平设计 | Web 应用、移动应用、初创 MVP |
| 13 | 拟物化 | 传统应用、游戏、高端产品 |
| 14 | 液态玻璃 | 高端 SaaS、高端电商 |
| 15 | 动效驱动 | 作品集网站、叙事平台 |
| 16 | 微交互 | 移动应用、触摸屏 UI |
| 17 | 包容性设计 | 公共服务、教育、医疗 |
| 18 | 零界面 | 语音助手、AI 平台 |
| 19 | 柔和 UI 进化版 | 现代企业应用、SaaS |
| 20 | 新粗野主义 | Z 世代品牌、创业公司、Figma 风格 |
| 21 | 便当盒网格 | 仪表板、产品页面、作品集 |
| 22 | Y2K 美学 | 时尚品牌、音乐、Z 世代 |
| 23 | 赛博朋克 UI | 游戏、科技产品、加密货币应用 |
| 24 | 有机亲生物 | 健康应用、可持续品牌 |
| 25 | AI 原生 UI | AI 产品、聊天机器人、Copilot |
| 26 | 孟菲斯设计 | 创意机构、音乐、年轻品牌 |
| 27 | 蒸汽波 | 音乐平台、游戏、作品集 |
| 28 | 维度分层 | 仪表板、卡片布局、模态框 |
| 29 | 夸张极简主义 | 时尚、建筑、作品集 |
| 30 | 动态字体 | 主视觉区、营销网站 |
| 31 | 视差叙事 | 品牌故事、产品发布 |
| 32 | 瑞士现代主义 2.0 | 企业网站、建筑、编辑类 |
| 33 | HUD / 科幻 FUI | 科幻游戏、太空科技、网络安全 |
| 34 | 像素艺术 | 独立游戏、复古工具、创意 |
| 35 | 便当网格 | 产品特性、仪表板、个人 |
| 36 | 空间 UI (VisionOS) | 空间计算应用、VR/AR |
| 37 | 电子墨水 / 纸张 | 阅读应用、数字报纸 |
| 38 | Z 世代混沌 / 极繁主义 | Z 世代生活方式、音乐艺术家 |
| 39 | 仿生 / 有机 2.0 | 可持续科技、生物科技、健康 |
| 40 | 反精致 / 原始美学 | 创意作品集、艺术家网站 |
| 41 | 触感数字 / 可变形 UI | 现代移动应用、趣味品牌 |
| 42 | 自然提炼 | 健康品牌、可持续产品 |
| 43 | 交互式光标设计 | 创意作品集、交互式 |
| 44 | 语音优先多模态 | 语音助手、无障碍应用 |
| 45 | 3D 产品预览 | 电商、家具、时尚 |
| 46 | 渐变网格 / 极光进化 | 主视觉区、背景、创意 |
| 47 | 编辑网格 / 杂志 | 新闻网站、博客、杂志 |
| 48 | 色差 / RGB 分离 | 音乐平台、游戏、科技 |
| 49 | 复古模拟 / 胶片 | 摄影、音乐/黑胶品牌 |

</details>

<details>
<summary><b>落地页风格 (8)</b></summary>

| # | 风格 | 最适用于 |
|---|------|---------|
| 1 | 主视觉中心设计 | 具有强烈视觉识别度的产品 |
| 2 | 转化优化型 | 潜在客户生成、销售页面 |
| 3 | 功能丰富展示 | SaaS、复杂产品 |
| 4 | 极简直接型 | 简单产品、应用 |
| 5 | 社交证明聚焦 | 服务、B2C 产品 |
| 6 | 交互产品演示 | 软件、工具 |
| 7 | 信任与权威型 | B2B、企业、咨询 |
| 8 | 叙事驱动型 | 品牌、代理公司、非营利 |

</details>

<details>
<summary><b>BI / 分析仪表板风格 (10)</b></summary>

| # | 风格 | 最适用于 |
|---|------|---------|
| 1 | 密集数据仪表板 | 复杂数据分析 |
| 2 | 热力图风格 | 地理/行为数据 |
| 3 | 高管仪表板 | 高管摘要 |
| 4 | 实时监控 | 运维、DevOps |
| 5 | 钻取分析 | 详细探索 |
| 6 | 对比分析仪表板 | 并排对比 |
| 7 | 预测分析 | 预测、机器学习洞察 |
| 8 | 用户行为分析 | UX 研究、产品分析 |
| 9 | 财务仪表板 | 财务、会计 |
| 10 | 销售智能仪表板 | 销售团队、CRM |

</details>

> 上面的表格收录了 67 种命名风格；完整的 `styles.csv` 数据库共有 84 种。[补齐其余部分](CONTRIBUTING.md)是一个对新手友好的公开任务。

---

## 支持的 AI 助手

**技能模式（自动激活，无需命令）：** Claude Code、Cursor、Windsurf、Antigravity、Codex CLI、Continue、Gemini CLI、OpenCode、Qoder、CodeBuddy、Droid (Factory)、KiloCode、Warp、Augment、CodeWhale

**工作流模式（斜杠命令调用）：** Kiro、GitHub Copilot、Roo Code、KiloCode

```
/ui-ux-pro-max 给我的 SaaS 产品做一个落地页
```

> **Trae：** 请先切换到 **SOLO** 模式，技能才会在 UI/UX 请求时激活。

---

## 支持的技术栈

| 类别 | 技术栈 |
|------|--------|
| **Web (HTML)** | HTML + Tailwind（默认） |
| **React 生态** | React、Next.js、shadcn/ui |
| **Vue 生态** | Vue、Nuxt.js、Nuxt UI |
| **Angular** | Angular |
| **PHP** | Laravel (Blade、Livewire、Inertia.js) |
| **其他 Web** | Svelte、Astro、Three.js |
| **桌面端** | JavaFX、WPF、WinUI 3、Avalonia、Uno Platform、UWP |
| **iOS** | SwiftUI |
| **Android** | Jetpack Compose |
| **跨平台** | React Native、Flutter |

在提示词中说明你的技术栈即可，不说则默认使用 HTML + Tailwind。

> **缺少你的技术栈？** 新增一个技术栈就是一个独立的 CSV 文件，非常适合作为第一个 PR —— 见 [新增技术栈](CONTRIBUTING.md#add-a-tech-stack)。

---

## 用法与示例提示词

```
给我的 SaaS 产品做一个落地页

做一个医疗分析仪表板

设计一个深色模式的作品集网站

做一个电商移动端 App UI

做一个深色主题的金融科技银行 App

审查这个页面的无障碍与 UX 问题
```

**背后发生了什么：**

1. **你提出需求** —— 任何 UI/UX 任务：构建、设计、创建、实现、审查、修复、改进
2. **先生成设计系统** —— 推理引擎在写任何代码之前先输出设计系统
3. **匹配推荐** —— 根据你的产品类型匹配风格、配色、字体、动效
4. **生成代码** —— 使用正确的设计令牌、间距和技术栈专属模式
5. **交付前检查** —— 对照 UX 反模式清单逐项验证

---

## 进阶：搜索 CLI

这个技能本质上就是数据加一个 Python 脚本，所以你可以直接查询它。

> 通过 Continue 安装的，请把下面的 `.claude/skills/` 替换为 `.continue/skills/`；Droid (Factory) 用 `.factory/skills/`。

```bash
# 生成完整设计系统（ASCII 输出）
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"

# 改为 Markdown 输出
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech banking" --design-system -f markdown

# 单域检索
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# 技术栈专属指南
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --stack react
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind

# 完整、不截断的数据
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS" --domain style --json
```

**检索域：** `product`、`style`、`typography`、`color`、`landing`、`chart`、`ux`、`icons`、`react`、`web`、`google-fonts`、`gsap`

**设计旋钮**（仅配合 `--design-system` 使用）：

```bash
python3 .../search.py "SaaS dashboard" --design-system --variance 8 --motion 6 --density 9
```

`--variance` 调节风格选择倾向（居中/极简 → 大胆/非对称），`--motion` 附带匹配的 GSAP 代码片段，`--density` 覆盖间距刻度（宽松 → 密集/仪表板）。

### 跨会话持久化设计系统

```bash
# 写入 design-system/MASTER.md
python3 .../search.py "SaaS dashboard" --design-system --persist -p "MyApp"

# 追加页面级覆盖文件
python3 .../search.py "SaaS dashboard" --design-system --persist -p "MyApp" --page "dashboard"
```

```
design-system/
├── MASTER.md           # 全局唯一真源（配色、字体、间距、组件）
└── pages/
    └── dashboard.md    # 页面级覆盖 —— 只写与主文件的差异
```

页面文件覆盖主文件。在新会话中这样引导 AI：

```
我正在开发 [页面名] 页面。请阅读 design-system/MASTER.md。
同时检查 design-system/pages/[page-name].md 是否存在。
如果页面文件存在，优先采用它的规则；如果不存在，仅使用 Master 规则。
现在开始生成代码……
```

---

## 🤝 参与贡献

**每一份贡献都算数，越小的越受欢迎。** 设计数据库是 CSV —— 价值最高的 PR 就是纯文本。

```bash
# 1. 在 GitHub 上 fork，然后：
git clone https://github.com/YOUR_USERNAME/claude-code-ui-ux-skill.git
cd claude-code-ui-ux-skill

# 2. 编辑唯一真源
#    src/ui-ux-pro-max/data/*.csv     ← 风格、配色、字体、规则
#    src/ui-ux-pro-max/scripts/*.py   ← 搜索引擎与生成器
#    src/ui-ux-pro-max/templates/     ← 各助手模板

# 3. 同步 + 校验（仅当你改动了 data/scripts/templates）
cd cli && npm install
npm run sync:assets && npm run check:assets
npm run validate:csv && npm run smoke:domains

# 4. 建分支、提交、开 PR
git checkout -b feat/your-feature
git commit -m "feat: add Bauhaus Revival style"
git push -u origin feat/your-feature
gh pr create
```

完整指南：**[CONTRIBUTING.md](CONTRIBUTING.md)** · 架构说明：**[CLAUDE.md](CLAUDE.md)** · 社区规范：**[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)**

### 💡 我们现在最需要什么

从下面任选一项直接开 PR —— 不需要事先征得同意。

| 方向 | 需要什么 | 难度 |
|------|---------|------|
| 🎨 **UI 风格** | 补齐 `styles.csv` 中尚未写入 README 表格的 17 种风格 | 🟢 新手 |
| 🌈 **配色方案** | 覆盖不足的行业：农业、物流、公共部门、教育 | 🟢 新手 |
| 🔤 **字体配对** | 非拉丁文字配对 —— 中日韩、阿拉伯语、天城文、西里尔 | 🟢 新手 |
| 🏭 **行业规则** | 161 条之外的任何行业：非营利、政务、交易平台、硬件 | 🟢 新手 |
| ♿ **UX 指南** | WCAG 2.2 补充、认知无障碍、屏幕阅读器模式 | 🟡 中级 |
| 🌍 **翻译** | 你的语言版本 `README.[lang].md` —— 西、法、德、日、葡、印地语 | 🟢 新手 |
| 📚 **文档与示例** | 技能改进页面的真实前后对比案例 | 🟢 新手 |
| 🧱 **新技术栈** | Solid、Qwik、Remix、Blazor、Ionic、Lit、Kotlin Multiplatform | 🟡 中级 |
| ✨ **GSAP 预设** | 更多动效层级，Framer Motion / Motion One 等价实现 | 🟡 中级 |
| 🔍 **搜索引擎** | `core.py` 的排序质量、同义词处理、容错匹配 | 🔴 高级 |
| 🖥️ **CLI** | 新增助手目标平台、改进 `uipro init` 诊断信息 | 🟡 中级 |
| 🧪 **测试** | `search.py` 各检索域与 CLI e2e 路径的覆盖率 | 🟡 中级 |

没找到你的想法？[开一个 issue](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) —— 欢迎提案，并且一定会得到回复。

### 贡献者

所有在此提交过改动的人都列在 **[CONTRIBUTORS.md](CONTRIBUTORS.md)**。

<a href="https://github.com/nicohodt/claude-code-ui-ux-skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=nicohodt/claude-code-ui-ux-skill" alt="Claude Code UI/UX 技能的贡献者" />
</a>

---

## 常见问题

### 什么是 Claude 技能（Skill）？

技能是一个包含指令和数据的文件夹，[Claude Code](https://claude.com/product/claude-code) 会在与你的请求相关时自动加载它。和每次粘贴的提示词不同，技能常驻在你的项目里（或全局的 `~/.claude/skills/`），并自动激活。这个技能会在你提出 UI、UX、设计、布局、配色、字体或无障碍相关需求时触发。

### 哪个 Claude 技能最适合做 UI/UX 设计？

本项目是目前最完整的开源选项：84 种 UI 风格、192 套配色、74 组字体配对、99 条 UX 指南、161 条行业推理规则，全部可离线检索。MIT 许可、没有付费版，并且支持 19 款 AI 编程助手 —— 不只是 Claude Code。

### 支持 Cursor 和 Windsurf 吗？

支持。运行 `uipro init --ai cursor` 或 `uipro init --ai windsurf` 即可。此外还支持 GitHub Copilot、Codex CLI、Gemini CLI、Antigravity、Kiro、Qoder、Roo Code、KiloCode、Trae、OpenCode、Continue、CodeBuddy、Droid、Warp、Augment 和 CodeWhale。

### 需要 API 密钥吗？会上传数据吗？

不需要，也不会。数据库是本地 CSV，搜索引擎只用 Python 标准库。无网络请求、无密钥、无遥测。唯一可选的联网行为是 CLI 检查 GitHub 上的新版本。

### 这和直接让 Claude"做得好看点"有什么区别？

"做得好看点"得到的是模型训练数据的平均值 —— 同样的紫色渐变、同样的字体、没有焦点态。这个技能用一个明确的、按行业匹配的设计系统加上一份反模式清单取代那个平均值，然后在交付前对照 WCAG AA 对比度、点击区域尺寸和减弱动效规则进行校验。

### 可以商用吗？

可以。MIT 许可 —— 可用于商业产品、可 fork、可分发。见 [LICENSE](LICENSE)。

### 真的免费吗？有付费版吗？

完全免费，且没有付费版。数据库中的全部内容都以 MIT 许可包含在这个仓库里。

### 如何贡献一种新的 UI 风格或配色？

在 `src/ui-ux-pro-max/data/` 下对应的 CSV 里加一行，在 `cli/` 里运行 `npm run sync:assets`，然后开 PR。完整说明见 [CONTRIBUTING.md](CONTRIBUTING.md) —— 大约五分钟，不需要事先了解这个代码库。

### 必须是设计师才能贡献吗？

不必。大多数贡献只是把业界已有的风格、配色或规则记录下来。如果你能说清为什么金融仪表板不该用粉彩渐变，你就能贡献。

---

## 故障排查

### `uipro: unknown command 'uninstall'` / `'update'`

你的 CLI 版本过旧：

```bash
npm install -g ui-ux-pro-max-cli@latest
uipro uninstall
```

### `uipro uninstall` 提示 "No installed AI skill directories detected"

技能安装在了别的目录。可以：

```bash
cd /path/to/your/project && uipro uninstall   # 回到当初安装的位置运行
uipro uninstall --global                      # 卸载全局安装

# 或手动删除
rm -rf .claude/skills/ui-ux-pro-max     # Claude Code
rm -rf .cursor/skills/ui-ux-pro-max     # Cursor
rm -rf .windsurf/skills/ui-ux-pro-max   # Windsurf
rm -rf .agents/skills/ui-ux-pro-max     # Antigravity / Codex
```

### 插件市场安装报错 "Zip file contains a symbolic link"

这是 v2.5.1 之前版本的已知问题 —— 旧版本内部使用了符号链接。本仓库不含任何符号链接；请升级，或改用 CLI 安装：

```bash
npm install -g ui-ux-pro-max-cli && uipro init --ai claude
```

### `npm install -g` 报权限错误

使用 Node 版本管理器，或跳过全局安装：

```bash
npx ui-ux-pro-max-cli init --ai claude
```

### 找不到 Python

搜索脚本需要 Python 3.x。请从 [python.org](https://www.python.org/downloads/) 或系统包管理器安装。AI 被要求向你询问，而不是自行安装。

### 设计系统输出被截断

可读输出会在 300 字符处截断长字段。使用 `--json` 获取完整数据：

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS" --domain style --json
```

---

## 自动化发布

发布流程基于 semantic-release 和 [Conventional Commits](https://www.conventionalcommits.org/)：

- `dev` 分支 → beta 预发布（`2.6.0-beta.1`）
- `main` 分支 → 正式发布（`2.6.0`）

`fix:` 触发补丁版本，`feat:` 触发次版本，`feat!:` 或 `BREAKING CHANGE:` 触发主版本。版本号会在 `skill.json`、`.claude-plugin/plugin.json`、`.claude-plugin/marketplace.json` 和 `cli/package.json` 之间保持同步。

---

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=nicohodt/claude-code-ui-ux-skill&type=Date)](https://star-history.com/#nicohodt/claude-code-ui-ux-skill&Date)

---

## 许可证

[MIT](LICENSE) —— 个人与商业用途均免费。

## 兼容的 AI 代理

- [Claude Code](https://claude.com/product/claude-code) —— 主要目标平台
- [AdaL](https://sylph.ai/) —— 自进化 AI 编程代理（[文档](https://docs.sylph.ai/) · [GitHub](https://github.com/SylphAI-Inc/adal-cli)）

---

<p align="center">
  <b>由 <a href="https://github.com/nicohodt">@nicohodt</a> 与<a href="https://github.com/nicohodt/claude-code-ui-ux-skill/graphs/contributors">每一位提交 PR 的人</a>共同维护。</b><br>
  <sub>如果它让你用 AI 做出的界面变好了，点个 ⭐ 能帮更多开发者找到它。</sub>
</p>
