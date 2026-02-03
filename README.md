# Deep Novel System

<p align="center">
  <a href="README.md">English</a> | <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Type-Claude%20Skill-8A2BE2" alt="Type">
  <img src="https://img.shields.io/badge/Tested%20on-Antigravity-blue" alt="Tested">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

A high-quality novel writing skill designed for **Claude**, specializing in narratives that require detailed sensory descriptions, complex plot management, and consistent character psychology.

## 🎯 About

This is a **Claude Skill** following the [Agent Skills](https://github.com/anthropics/agent-skills) open standard. Skills are reusable AI agent capability modules that extend AI's professional abilities through structured instructions and workflows.

### Recommended Environment

This skill has been tested on **Antigravity** with excellent results. Recommended configurations:

| IDE / Client | Recommended Model |
|-------------|-------------------|
| **Antigravity** (Google DeepMind) | Gemini 3 Pro |
| **Cursor** | Claude 4.5 Opus |
| **Claude Code** | Claude 4.5 Opus |

> 💡 **Tip**: Using more powerful models yields better long-form narrative coherence and detailed descriptions.

## ✨ Features

- 📖 **Structured Writing Workflow** - Complete creation process from outline to chapters
- 🧠 **Memory Management System** - Cross-chapter character state and relationship tracking
- 🔄 **Feedback Loop Mechanism** - Iterative quality optimization
- 📁 **Project Templates** - Quick initialization for new novel projects
- 🎭 **Multi-genre Support** - Suitable for Horror fiction, erotic fiction, light novels, deep narratives, etc.

## 🚀 Quick Start

### Installation

Clone this repository to your `.agent/skills/` directory:

```bash
cd /path/to/your/project/.agent/skills/
git clone https://github.com/ALBEDO-TABAI/deep-novel-system.git
```

### Usage

In your AI conversation, say:

> "I want to start writing a novel"

or

> "Continue writing `<project path>`"

## 📂 Directory Structure

```
deep-novel-system/
├── SKILL.md              # Main skill entry file
├── README.md             # This file (English)
├── README_zh.md          # Chinese version
├── LICENSE               # MIT License
├── assets/
│   └── template/         # Project template
│       ├── config/       # Writing configuration
│       ├── drafts/       # Chapter drafts
│       ├── memory/       # Memory files
│       ├── plans/        # Outline plans
│       ├── references/   # Reference materials
│       └── feedback/     # Feedback records
├── references/           # Workflow reference docs
│   ├── workflow.md       # Long novel writing process
│   ├── memory_management.md
│   ├── reference_usage.md
│   ├── feedback_loop.md
│   └── onboarding.md
└── scripts/
    └── init_novel.py     # Project initialization script
```

## 📚 Workflows

### 1. Long Novel Writing Process

See [workflow.md](references/workflow.md)

**Key Stages**:
1. **Input Analysis** - Read previous chapters, outlines, and requirements
2. **Drafting** - Write content in blocks (e.g., `CH01 SEC01`)
3. **Review & Polish** - Check against style guidelines

### 2. Memory Management

See [memory_management.md](references/memory_management.md)

- Update `memory/` files after major events
- Maintain character states and relationship maps

### 3. Feedback Loop

See [feedback_loop.md](references/feedback_loop.md)

## 🛠️ Project Initialization

Create a new project using the initialization script:

```bash
python scripts/init_novel.py <target_directory>
```

## 🤝 Compatibility

This skill follows the [Agent Skills](https://github.com/anthropics/agent-skills) open standard and is theoretically compatible with all AI agents supporting this standard:

- **Antigravity** (Google DeepMind) ✅ Tested
- Claude Code
- Cursor
- GitHub Copilot
- Other Agent Skills compatible clients

## 📄 License

[MIT License](LICENSE)

## 🙏 Acknowledgments

Inspired by the [obra/superpowers](https://github.com/obra/superpowers) framework.
