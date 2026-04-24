# Deep Novel System

<p align="center">
  <a href="README.md">English</a> | <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Type-Claude%20Skill-8A2BE2" alt="Type">
  <img src="https://img.shields.io/badge/Tested%20on-Antigravity-blue" alt="Tested">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

A high-quality long-form novel writing skill designed for **Claude**, specializing in complex narratives, sensory descriptions, cross-chapter memory management, and feedback loops. Supports multiple genres and mature themes when authorized by the user.

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

- 📖 **Structured Writing Workflow** - Complete creation process from outline to chapters, with truncation detection and recovery
- 🧠 **Memory Management System** - Cross-chapter state tracking with YAML-schema'd memory blocks
- 🔄 **Feedback Loop Mechanism** - Versioned rules with archive flow for long-running projects
- 📁 **Project Templates** - Idempotent init script (default: skip-existing; supports `--dry-run` / `--force`)
- 🗂️ **Project State Machine** - `state.yaml` tracks current chapter/section so multi-session work stays consistent
- 🎭 **Multi-genre Support** - Suitable for horror, mature/erotic, light novels, deep narratives, etc.

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
│   └── template/         # Project template (copied by init_novel.py)
│       ├── config/instruction.md
│       ├── drafts/
│       ├── memory/
│       ├── plans/{chapters,setting}/
│       ├── references/
│       ├── feedback/{requirements.md,archive/}
│       └── state.yaml
├── docs/                 # Skill's own rule docs (do NOT use as style references)
│   ├── workflow.md       # Long novel writing process
│   ├── memory_management.md
│   ├── reference_usage.md
│   ├── feedback_loop.md
│   └── onboarding.md
├── references/           # User-supplied style samples / analyses
└── scripts/
    └── init_novel.py     # Project initialization script
```

## 📚 Workflows

### 1. Long Novel Writing Process

See [docs/workflow.md](docs/workflow.md)

**Key Stages**:
1. **Input Analysis** - Read previous chapters, outlines, and requirements
2. **Drafting** - Write content in blocks (e.g., `CH01 SEC01`), with truncation detection and append-style continuation
3. **Review & Polish** - Check against style guidelines
4. **State Update** - Advance `state.yaml`

### 2. Memory Management

See [docs/memory_management.md](docs/memory_management.md)

- Update `memory/` files after major events
- Each block uses YAML front-matter (chapter / section / irreversible_changes / ...)
- Future scripts can validate consistency from these structured fields

### 3. Feedback Loop

See [docs/feedback_loop.md](docs/feedback_loop.md)

- Each rule carries `id` / `added` / `last_hit` metadata
- Periodic archive flow keeps `requirements.md` lean for long-running projects

## 🛠️ Project Initialization

Create a new project using the initialization script:

```bash
python scripts/init_novel.py <target_directory>           # default: skip-existing
python scripts/init_novel.py <target_directory> --dry-run # preview only
python scripts/init_novel.py <target_directory> --force   # overwrite existing files
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
