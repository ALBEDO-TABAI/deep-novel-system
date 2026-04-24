# Deep Novel System (深度小说系统)

<p align="center">
  <a href="README.md">English</a> | <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Type-Claude%20Skill-8A2BE2" alt="Type">
  <img src="https://img.shields.io/badge/Tested%20on-Antigravity-blue" alt="Tested">
  <img src="https://img.shields.io/badge/Language-中文-red" alt="Language">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

一个专为 **Claude** 设计的高质量长篇小说创作技能（Skill），擅长复杂叙事、感官描写、跨章节记忆管理与反馈循环，支持多种类型与成人主题（在用户授权范围内）。

## 🎯 关于本项目

这是一个 **Claude Skill**，遵循 [Agent Skills](https://github.com/anthropics/agent-skills) 开放标准。Skill 是一种可复用的 AI 代理能力模块，通过结构化的指令和工作流扩展 AI 的专业能力。

### 推荐使用环境

本技能已在 **Antigravity** 中测试，效果理想。推荐配置：

| IDE / 客户端 | 推荐模型 |
|-------------|---------|
| **Antigravity** (Google DeepMind) | Gemini 3 Pro |
| **Cursor** | Claude 4.5 Opus |
| **Claude Code** | Claude 4.5 Opus |

> 💡 **提示**：使用更强大的模型可以获得更好的长篇叙事连贯性和细节描写效果。

## ✨ 特性

- 📖 **结构化写作工作流** - 从大纲到章节的完整创作流程，含截断检测与续写恢复
- 🧠 **记忆管理系统** - 跨章节状态追踪，记忆块带 YAML schema
- 🔄 **反馈循环机制** - 规则带 id/时间戳元数据，配套归档流程
- 📁 **项目模板** - 幂等初始化（默认跳过已存在文件，支持 `--dry-run` / `--force`）
- 🗂️ **项目状态机** - `state.yaml` 记录当前章节/段落，跨会话连续创作不会跳号
- 🎭 **多类型支持** - 适用于深度叙事、恐怖、成人/情色、轻小说等

## 🚀 快速开始

### 安装

将此仓库克隆到你的 `.agent/skills/` 目录：

```bash
cd /path/to/your/project/.agent/skills/
git clone https://github.com/ALBEDO-TABAI/deep-novel-system.git
```

### 使用

在 AI 对话中说：

> "我想开始写小说"

或

> "继续写作 `<项目路径>`"

## 📂 目录结构

```
deep-novel-system/
├── SKILL.md              # 主技能入口文件
├── README.md             # 英文版说明
├── README_zh.md          # 中文版说明（本文件）
├── LICENSE               # MIT 许可证
├── assets/
│   └── template/         # 项目模板（init_novel.py 复制源）
│       ├── config/instruction.md
│       ├── drafts/
│       ├── memory/
│       ├── plans/{chapters,setting}/
│       ├── references/
│       ├── feedback/{requirements.md,archive/}
│       └── state.yaml
├── docs/                 # 技能自身的规则手册（不要作为风格范文使用）
│   ├── workflow.md       # 长篇小说写作流程
│   ├── memory_management.md
│   ├── reference_usage.md
│   ├── feedback_loop.md
│   └── onboarding.md
├── references/           # 用户提供的范文与风格素材
└── scripts/
    └── init_novel.py     # 项目初始化脚本
```

## 📚 工作流

### 1. 长篇小说写作流程

详见 [docs/workflow.md](docs/workflow.md)

**关键阶段**：
1. **输入分析** - 阅读以前的章节、大纲和要求
2. **起草** - 分块编写内容（例如 `CH01 SEC01`），含截断检测与追加续写
3. **审查与润色** - 根据风格指南进行检查
4. **状态机更新** - 推进 `state.yaml`

### 2. 记忆管理

详见 [docs/memory_management.md](docs/memory_management.md)

- 在重大事件后更新 `memory/` 文件
- 每块带 YAML front-matter（章节/段落/不可逆变化等机读字段）
- 后续可用脚本对 front-matter 做一致性校验

### 3. 反馈循环

详见 [docs/feedback_loop.md](docs/feedback_loop.md)

- 每条规则带 `id` / `added` / `last_hit` 元数据
- 配套定期归档流程，长跑项目下 `requirements.md` 不会无限膨胀

## 🛠️ 项目初始化

使用初始化脚本创建新项目：

```bash
python scripts/init_novel.py <目标目录>           # 默认：仅创建缺失文件
python scripts/init_novel.py <目标目录> --dry-run # 仅预览
python scripts/init_novel.py <目标目录> --force   # 显式确认覆盖（用于重置）
```

## 🤝 兼容性

此技能遵循 [Agent Skills](https://github.com/anthropics/agent-skills) 开放标准，理论上兼容所有支持该标准的 AI 代理：

- **Antigravity** (Google DeepMind) ✅ 已测试
- Claude Code
- Cursor
- GitHub Copilot
- 其他支持 Agent Skills 的客户端

## 📄 许可证

[MIT License](LICENSE)

## 🙏 致谢

灵感来自 [obra/superpowers](https://github.com/obra/superpowers) 框架。
