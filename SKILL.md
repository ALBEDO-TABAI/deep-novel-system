---
name: deep-novel-system
description: 一个用于撰写高质量小说的综合系统，特别擅长色情或复杂的叙事。提供大纲、章节写作、记忆管理和反馈循环的工作流。当用户想要开始写新小说、继续写现有小说或需要结构化的长篇叙事指导时使用此技能。
---

# Deep Novel System (深度小说系统)

## 概览 (Overview)
**Deep Novel System** 是一个专为创作复杂、高质量小说而设计的框架。它特别擅长需要详细感官描述、复杂情节管理和一致角色心理的类型，如色情小说、轻小说和深度叙事作品。

## 何时使用此技能 (When to Use This Skill)
- **开始新小说 (Starting a New Novel)**: 当用户想要构建具有稳健结构的新项目时。
- **撰写章节 (Writing Chapters)**: 当用户需要按照严格的工作流撰写特定部分（如 `CHxx SECxx`）时。
- **管理长篇叙事 (Managing Long Narratives)**: 当上下文管理、记忆更新和情节一致性至关重要时。
- **色情/感官描写 (Erotic/Sensory Writing)**: 当用户要求"深度"或"沉浸式"描述时。

---

## 首次使用指南 (First-Time Setup)

使用本技能前，需要先确定您的写作项目目录。

### 交互式引导

当您说"我想开始写小说"或激活此技能时，我会进行以下流程：

### 步骤 1：询问项目路径

> 您想把小说项目放在哪里？请提供一个目录路径。
> 
> 示例：`F:\我的小说\项目A` 或 `D:\Writing\新作品`

### 步骤 2：检查现有文件

- **如果目录已存在内容**：识别现有文件结构，询问是继续现有项目还是覆盖
- **如果是空目录或新目录**：进入引导问答

### 步骤 3：引导问答（如果没有基础文件）

我会询问以下问题来帮助建立项目基础：

1. **小说类型/风格**：例如色情、轻小说、现代言情、玄幻等
2. **主要角色**：简单描述 2-3 个核心角色
3. **核心冲突/主题**：故事的核心驱动力是什么？
4. **预计篇幅**：短篇（< 5万字）/ 中篇（5-20万字）/ 长篇（> 20万字）
5. **特殊要求**：是否有特定的写作风格或禁忌词汇要求

### 步骤 4：生成基础文件

根据您的回答，我会在项目目录下创建：

```
<您的项目目录>/
├── config/
│   └── instruction.md    # 写作配置与风格指令
├── drafts/               # 存放生成的章节
├── plans/
│   └── outline.md        # 初步大纲
├── memory/
│   └── characters.md     # 角色设定
├── references/           # 参考资料
└── feedback/             # 反馈记录
```

---

## 继续现有项目

如果您已有项目目录，只需告诉我：

> "继续写作 `<项目路径>`"

我会自动读取项目结构，加载上下文，并准备好从上次中断处继续。

---

## 工作流 (Workflows)

### 1. 长篇小说写作流程 (Long Novel Writing Process)
有关撰写章节的详细分步指南，请参阅 **长篇小说写作工作流**。

-   **参考文档**: [workflow.md](references/workflow.md)
-   **关键阶段**:
    1.  **输入分析 (Input Analysis)**: 阅读以前的章节、大纲和要求。
    2.  **起草 (Drafting)**: 分块编写内容（例如 `CH01 SEC01`）。
    3.  **审查与润色 (Review & Refine)**: 根据"禁词表"和风格指南进行检查。

### 2. 记忆与上下文管理 (Memory & Context Management)
跨长篇小说管理状态至关重要。

-   **参考文档**: [memory_management.md](references/memory_management.md)
-   **参考文档**: [reference_usage.md](references/reference_usage.md)
-   **原则**:
    -   在重大事件后更新 `memory/` 文件。
    -   维护角色状态和关系图。

### 3. 反馈循环 (Feedback Loop)
通过迭代反馈改进写作。

-   **参考文档**: [feedback_loop.md](references/feedback_loop.md)

---

## 项目模板结构 (`assets/template`)

该技能包含一个空白项目模板，使用初始化脚本复制到您的项目目录：

```bash
python scripts/init_novel.py <目标目录>
```

模板结构：
-   `config/`: 系统提示词和模型指令
-   `plans/`: 大纲、章节细分
-   `memory/`: 全局记忆、角色卡、世界观信息
-   `drafts/`: 存放生成文本的地方
-   `references/`: 参考资料
-   `feedback/`: 反馈记录

---

## 使用技巧 (Usage Tips)
-   **项目隔离**: 每个小说项目应有独立的目录，便于管理多个作品
-   **配置继承**: 可以从现有项目复制 `config/instruction.md` 到新项目
-   **风格**: 该系统推崇"展示，不要讲述 (Show, Don't Tell)"和沉浸式、感官丰富的描述
-   **安全**: 虽然能够处理 NSFW 内容（如果用户规则允许），但始终遵守 `instruction.md` 中配置的边界
