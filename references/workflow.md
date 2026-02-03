---
description: 一个用于长篇小说写作的结构化工作流，管理上下文、记忆和反馈。
---

# 长篇小说写作工作流 (Long-Form Novel Writing Workflow)

此工作流指导 AI 完成小说章节写作的生命周期，确保一致性并遵守用户计划。

## 前置条件
确保您的工作区中存在以下文件结构：
- `novel_writer_system/config/instruction.md` (模型人格/系统指令)
- `novel_writer_system/references/` (风格指南、范文)
- `novel_writer_system/plans/global_plan.md` (整体故事线)
- `novel_writer_system/plans/chapters/` (具体章节大纲)
- `novel_writer_system/feedback/requirements.md` (累积的用户反馈)
- `novel_writer_system/memory/` (上下文压缩块)

## 工作流步骤

### 1. 初始化与上下文加载
1.  **读取规则**: 读取 `novel_writer_system/feedback/requirements.md` 以了解当前的约束和“禁忌”。
2.  **读取参考**: 读取 `novel_writer_system/references/` 目录下的所有文件（如 `style_guide.md`, `sample_text.md`）。
    -   **风格学习**: 依据 `novel_writer_system/rules/reference_usage.md`，分析范文的词汇密度、句式节奏和感官侧重，提取“当前写作风格指令”。
3.  **读取设定**: 读取 `novel_writer_system/plans/setting/` 目录下的所有文件 (例如 `blacksets`)，获取角色特质、内心动机及关系网络。
4.  **读取计划**: 
    -   读取 `novel_writer_system/plans/global_plan.md` 获取高层上下文。
    -   确定*当前*要写的章节和部分。
    -   **检查原子性 (Atomicity Check)**: 确认本次任务量是否适中（目标约 4000 字）。如果整章过长，必须在计划阶段拆分为多个部分（Part 1, Part 2...）。
    -   读取具体的章节计划 (例如 `novel_writer_system/plans/chapters/ch01_plan.md`)。

### 2. 记忆检索
1.  **识别前文上下文**: 定位*紧接前文*部分的 `novel_writer_system/memory/` 文件 (例如 `mem_ch01_sec01.md`)。
2.  **读取记忆**: 读取识别出的记忆块。
    -   *关键*: 除非为了检查特定细节有明确必要，否则不要读取以前章节的全文。依赖摘要。

### 3. 起草 (写作阶段)
1.  **目标**: 撰写目标部分 (例如 `novel_writer_system/drafts/ch01_sec02.md`)。
    -   **字数要求**: 单次输出正文应 ≥ 4000 汉字（不含摘要和状态块）。
2.  **执行**:
    -   基于章节计划步骤生成文本，保持风格指南中的基调和记忆块中的连贯性。
    -   **应用风格**: 强制使用“风格学习”步骤中提取的写作策略（如模仿范文的特定的比喻方式）。
    -   应用 `requirements.md` 中的约束。
3.  **输出**: 将生成的文本保存到 `novel_writer_system/drafts/`。

### 4. 审查与记忆压缩
**触发**: 起草完成后立即进行。
1.  **压缩**: 为刚刚写好的部分创建一个新的 Memory Block (例如 `novel_writer_system/memory/mem_ch01_sec02.md`)。
    -   遵循 `novel_writer_system/rules/memory_management.md` 中的规则。
    -   包含：剧情梗概、角色状态、情节线索、关键细节。
    -   **状态同步**: 确保记录任何“不可逆”的状态变化（受伤、物品消耗、承诺）。
2.  **自纠**: 对照 `requirements.md` 检查草稿。如果发现重大违规行为，重写或向用户注明。

### 5. 反馈循环
**触发**: 用户审查草稿后。
1.  **分析反馈**: 用户提供的具体评论。
2.  **更新要求**: 
    -   打开 `feedback/requirements.md`。
    -   添加新的负面约束或正面风格偏好。
    -   解决冲突（较新的反馈覆盖较旧的）。
    -   遵循 `rules/feedback_loop.md` 中的规则。
    -   **同步确认**: 在下一次 `notify_user` 中，明确列出已更新的 `requirements.md` 条目，供用户确认。

### 6. 持续优化
1.  **定期清理**: 每完成一个大章节（Chapter），检查 `requirements.md`，移除不再适用或已被内化的规则，保持文件精简。

## 示例命令序列
```bash
# 1. 开始写作第1章第2节
read_file novel_writer_system/config/instruction.md novel_writer_system/feedback/requirements.md novel_writer_system/plans/chapters/ch01_plan.md novel_writer_system/memory/mem_ch01_sec01.md

# 2. 撰写内容
write_to_file novel_writer_system/drafts/ch01_sec02.md ...

# 3. 创建记忆块
write_to_file novel_writer_system/memory/mem_ch01_sec02.md ...

# 4. 更新要求 (如果用户抱怨“对话太多”)
multi_replace_file_content novel_writer_system/feedback/requirements.md ...
```
