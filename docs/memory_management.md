# Memory Block 管理规则

## 目的
为了在长篇写作中保持连贯性和一致性，将已完成的内容压缩成易于管理的“Memory Blocks (记忆块)”，以便模型在未来的步骤中引用，而无需读取完整的历史记录。

## 文件结构
- **位置**: `./memory/` 目录（相对于项目根）。
- **命名**: `mem_ch[XX]_sec[YY].md` 或 `mem_ch[XX]_summary.md`（XX/YY 为两位零填充，例如 `mem_ch01_sec02.md`）。

## Memory Block 文件格式

每个记忆块以 YAML front-matter 开头存放机读字段，正文用 Markdown 存放叙述性字段。这样未来可以用脚本做一致性校验，同时不破坏可读性。

### 必填 front-matter schema

```yaml
---
chapter: 1                              # 整数
section: 2                              # 整数
created_at: 2026-04-22T11:00:00+08:00   # ISO 8601
prev_memory: memory/mem_ch01_sec01.md   # 上一节记忆块的路径，没有则填 ""
draft: drafts/ch01_sec02.md             # 本块对应的草稿
characters_present:                     # 本节出场的角色名（必须与 plans/setting/ 一致）
  - 角色A
  - 角色B
location: ""                            # 本节主要发生地
irreversible_changes:                   # 不可逆状态变化，必须列全
  - "角色A 左手腕骨折"
  - "角色B 获得密码 '青鸟'"
active_threads:                         # 本节结束时仍未结束的情节线
  - "角色A 在追查神秘信件来源"
foreshadowing:                          # 本节埋下的伏笔
  - "镜中倒影一闪而过的红色"
---
```

### 正文 Markdown 结构

每个记忆块必须包含以下章节：

1.  **剧情梗概 (Detailed Synopsis)**:
    -   按时间顺序总结所引用的部分的事件。
    -   角色采取的关键行动。
2.  **角色状态更新 (Character State Updates)**:
    -   生理状态（受伤、物品清单、位置、体力消耗）。 *[现实性原则]*
    -   情绪状态（当前心情、态度变化）。
    -   信息状态（角色获知了什么新信息，来源是什么）。 *[信息来源追踪]*
    -   关系动态（联盟或冲突的转变）。
3.  **情节线索 (Plot Threads)**:
    -   **已解决 (Resolved)**: 得到解答的问题或结束的冲突。
    -   **活跃中 (Active)**: 正在进行的谜团，当前的目标。
    -   **伏笔 (Foreshadowing)**: 留下的暗示，稍后通过需要呼应。
4.  **关键细节与一致性锚点 (Key Details & Consistency Anchors)**:
    -   必须保持一致的具体短语、物体描述或场景细节（例如，“他左脸颊上的伤疤”，“密码是‘青鸟’”）。
5.  **基调与风格参考 (Tone & Style Reference)**:
    -   关于主要氛围的简要说明（例如，“紧张、幽闭恐惧”或“轻松、喜剧”）。

## 创建流程 (压缩规则)
当一个部分的写作任务完成时：
1.  **输入**: 刚刚写完的章节全文 + 上一个 Memory Block。
2.  **行动**: 总结新文本，并在必要时将其与上一个块的上下文合并（或链接到它）。
3.  **输出**: 一个新的 Memory Block 文件，front-matter 字段必须填全（无值的列表填空数组 `[]`，无值的字符串填 `””`）。
4.  **联动**: 写完后按 `./docs/workflow.md` step 4.3 推进 `./state.yaml`。

## 使用规则
-   **读取**: 在撰写新内容之前，模型必须读取紧接的前一部分的 Memory Block 以及”全局大纲 (Global Plan)”或相关的”章节大纲 (Chapter Plan)”。
-   **无冗余**: 除非为了调试连贯性错误而特别需要，否则不要重新读取以前章节的完整原始文本。请依赖 Memory Blocks。
-   **一致性校验**: 写新章节前，扫描历史 Memory Block 的 `irreversible_changes` 字段，确保新内容不与任何已发生的不可逆事件矛盾（例如不能让左手腕骨折的角色立刻徒手开锁）。
