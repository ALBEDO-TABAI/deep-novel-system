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

一个专为 **Claude** 设计的高质量小说创作技能（Skill），特别擅长需要详细感官描述、复杂情节管理和一致角色心理的叙事类型。

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

- 📖 **结构化写作工作流** - 从大纲到章节的完整创作流程
- 🧠 **记忆管理系统** - 跨章节的角色状态、关系追踪
- 🔄 **反馈循环机制** - 迭代优化写作质量
- 📁 **项目模板** - 快速初始化新小说项目
- 🎭 **多类型支持** - 适用于色情小说、轻小说、深度叙事等

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
│   └── template/         # 项目模板
│       ├── config/       # 写作配置
│       ├── drafts/       # 章节草稿
│       ├── memory/       # 记忆文件
│       ├── plans/        # 大纲计划
│       ├── references/   # 参考资料
│       └── feedback/     # 反馈记录
├── references/           # 工作流参考文档
│   ├── workflow.md       # 长篇小说写作流程
│   ├── memory_management.md
│   ├── reference_usage.md
│   ├── feedback_loop.md
│   └── onboarding.md
└── scripts/
    └── init_novel.py     # 项目初始化脚本
```

## 📚 工作流

### 1. 长篇小说写作流程

详见 [workflow.md](references/workflow.md)

**关键阶段**：
1. **输入分析** - 阅读以前的章节、大纲和要求
2. **起草** - 分块编写内容（例如 `CH01 SEC01`）
3. **审查与润色** - 根据风格指南进行检查

### 2. 记忆管理

详见 [memory_management.md](references/memory_management.md)

- 在重大事件后更新 `memory/` 文件
- 维护角色状态和关系图

### 3. 反馈循环

详见 [feedback_loop.md](references/feedback_loop.md)

## 🛠️ 项目初始化

使用初始化脚本创建新项目：

```bash
python scripts/init_novel.py <目标目录>
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
