---
description: 一个用于长篇小说写作的结构化工作流，管理上下文、记忆、状态与反馈。
---

# 长篇小说写作工作流 (Long-Form Novel Writing Workflow)

此工作流指导 AI 完成小说章节写作的生命周期，确保一致性并遵守用户计划。

> **路径约定**：本文档中所有 `./xxx` 路径都相对于**用户项目根目录**（由 `scripts/init_novel.py <目标目录>` 生成，或用户手动指定）。`docs/` 下的规则文件住在 skill 目录,并**不在**用户项目根目录下,读取规则时请按 skill 安装路径解析。

## 前置条件
用户项目根目录下应存在以下文件结构（由 `init_novel.py` 从 `assets/template/` 拷出）：
- `./config/instruction.md` (SillyTavern Chat Completion 预设；其他客户端可忽略或删除)
- `./references/` (用户提供的风格指南、范文、分析素材)
- `./plans/global_plan.md` (整体故事线)
- `./plans/chapters/` (具体章节大纲，如 `ch01_plan.md`)
- `./plans/setting/` (世界观 `world.md`、角色 `characters.md`)
- `./feedback/requirements.md` (累积的用户反馈)
- `./feedback/archive/` (过期规则归档)
- `./drafts/` (生成的章节草稿)
- `./memory/` (上下文压缩块)
- `./state.yaml` (项目进度状态机；首次写作时若不存在则按本文末尾模板创建)

> `docs/` 下的工作流/记忆/反馈规则文档是 AI 自身的规则手册,读取时请从 skill 安装目录读,**不要**拷到用户项目,也**不要**把它们当作 `references/` 里的风格范文去模仿。

## 工作流步骤

### 1. 初始化与上下文加载
1.  **读取状态机**: 读取 `./state.yaml` 确认 `current.chapter` / `current.section` 与 `last_completed`，明确"这次该写哪一节"。如果文件不存在，按 `state.yaml` 模板创建一个，初始化为 ch01 sec01。
2.  **读取规则**: 读取 `./feedback/requirements.md` 以了解当前的约束和"禁忌"。
3.  **读取参考**: 读取 `./references/` 目录下的所有用户范文与分析素材。
    -   **重要**：`./references/` 现在只包含用户提供的范文、风格分析、人物素材等创作输入。**不要**把 `./docs/` 下的工作流规则文档当作范文模仿。
    -   **风格学习**: 依据 `./docs/reference_usage.md`，分析范文的词汇密度、句式节奏和感官侧重，提取"当前写作风格指令"。
4.  **读取设定**: 读取 `./plans/setting/` 目录下的所有文件 (例如 `blacksets`、`newsets`)，获取角色特质、内心动机及关系网络。
5.  **读取计划**:
    -   读取 `./plans/global_plan.md` 获取高层上下文（如不存在，使用 `./plans/` 下相关的 `*-plan*.md`）。
    -   根据 step 1 的状态机定位*当前*要写的章节和部分。
    -   **检查原子性 (Atomicity Check)**: 确认本次任务量是否适中（目标约 4000 字）。如果整章过长，必须在计划阶段拆分为多个部分（Part 1, Part 2...）。
    -   读取具体的章节计划 (例如 `./plans/chapters/ch01_plan.md`)。

### 2. 记忆检索
1.  **识别前文上下文**: 根据 `state.yaml.last_completed` 定位*紧接前文*部分的 `./memory/` 文件 (例如 `mem_ch01_sec01.md`)。
2.  **读取记忆**: 读取识别出的记忆块。
    -   *关键*: 除非为了检查特定细节有明确必要，否则不要读取以前章节的全文。依赖摘要。

### 3. 起草 (写作阶段)
1.  **目标**: 撰写目标部分 (例如 `./drafts/ch01_sec02.md`)。
    -   **字数要求**: 单次输出正文应 ≥ 4000 汉字（不含摘要和状态块）。
2.  **执行**:
    -   基于章节计划步骤生成文本，保持风格指南中的基调和记忆块中的连贯性。
    -   **应用风格**: 强制使用"风格学习"步骤中提取的写作策略（如模仿范文的特定的比喻方式）。
    -   应用 `requirements.md` 中的约束。
3.  **输出**: 将生成的文本保存到 `./drafts/`。

### 3.5 截断检测与续写
**触发**: 起草输出完成后立即执行。
1.  **字数检查**: 统计正文汉字数。若 < 4000 汉字 **或** 末尾不在自然段尾（例如停在句中、未完整收束场景），进入续写模式。
2.  **续写规则**:
    -   使用追加（append）写入同一份草稿文件，**不要**重新生成已有内容。
    -   续写前需先读取已写部分的最后 200 字作为上下文锚点，保证语气与情节衔接。
    -   单节最多续写 3 次；若 3 次后仍未达成字数或自然收束，写入 `./drafts/ch??_sec??.partial.md`，并在 `state.yaml.notes` 字段标注 `partial: ch??_sec??`，等待用户介入。
3.  **过滤/拒绝处理**: 若模型触发内容过滤导致输出截断，记录到 `state.yaml.notes`，不要静默重试以免丢失用户指令上下文。

### 4. 审查与记忆压缩
**触发**: 起草完成（且通过 3.5 检查）后立即进行。
1.  **压缩**: 为刚刚写好的部分创建一个新的 Memory Block (例如 `./memory/mem_ch01_sec02.md`)。
    -   遵循 `./docs/memory_management.md` 中的规则（含 YAML front-matter schema）。
    -   包含：剧情梗概、角色状态、情节线索、关键细节。
    -   **状态同步**: 确保记录任何"不可逆"的状态变化（受伤、物品消耗、承诺）。
2.  **自纠**: 对照 `requirements.md` 检查草稿。如果发现重大违规行为，重写或向用户注明。
3.  **更新状态机**: 把 `state.yaml.current` 推进到下一节，把 `last_completed` 更新为本节，写入 `completed_at` 时间戳。

### 5. 反馈循环
**触发**: 用户审查草稿后。
1.  **分析反馈**: 用户提供的具体评论。
2.  **更新要求**:
    -   打开 `./feedback/requirements.md`。
    -   按 `./docs/feedback_loop.md` 的元数据格式添加新的负面约束或正面风格偏好（含 `id` / `added` 时间戳）。
    -   解决冲突（按时间戳比较，新覆盖旧，并标注被覆盖的 `id`）。
    -   **同步确认**: 在下一次回复中，明确列出已更新的 `requirements.md` 条目，供用户确认。
3.  **更新状态机**: 把 `state.yaml.requirements_version` 更新为本次修改的时间戳。

### 6. 持续优化
1.  **定期清理**: 每完成一个大章节（Chapter），按 `./docs/feedback_loop.md` 的归档流程，把连续多章未触发的规则移到 `./feedback/archive/<日期>.md`，保持 `requirements.md` 精简。

## state.yaml 模板

```yaml
project: <小说标题>
current:
  chapter: 1
  section: 1
last_completed:
  chapter: 0
  section: 0
  draft: ""
  memory: ""
  completed_at: ""
requirements_version: ""
notes: ""
```

## 示例命令序列
```bash
# 1. 开始写作第1章第2节
read_file ./state.yaml ./feedback/requirements.md ./plans/chapters/ch01_plan.md ./memory/mem_ch01_sec01.md

# 2. 撰写内容（输出后跑 3.5 字数检查；不足则追加）
write_to_file ./drafts/ch01_sec02.md ...

# 3. 创建记忆块
write_to_file ./memory/mem_ch01_sec02.md ...

# 4. 推进状态机
write_to_file ./state.yaml ...

# 5. 更新要求 (如果用户抱怨"对话太多")
multi_replace_file_content ./feedback/requirements.md ...
```
