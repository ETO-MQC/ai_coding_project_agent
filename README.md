# AI Coding 项目自动开发 Agent

这是一个面向科研竞赛、课程设计、AI Coding 辅助开发的完整可运行原型。

它的目标不是“完全替代程序员”，而是把一个项目从想法到 Demo 的过程拆成标准流程：

```text
项目想法
  ↓
需求分析 Agent
  ↓
架构设计 Agent
  ↓
任务拆解 Agent
  ↓
代码生成 Agent
  ↓
测试执行 Agent
  ↓
错误修复建议 Agent
  ↓
最终报告生成 Agent
```

默认使用本地 Mock 模式，不需要 API Key，也能完整跑通。

---

## 一、快速运行

### 1. 解压

```bash
unzip ai_coding_project_agent.zip
cd ai_coding_project_agent
```

### 2. 创建虚拟环境

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行完整流程

```bash
python -m ai_coding_agent.cli run --idea "开发一个云边协同小模型训练与部署Demo" --name cloud_edge_demo
```

运行后会生成：

```text
workspace/cloud_edge_demo/
├── requirements.md
├── architecture.md
├── tasks.json
├── generated_app/
├── test_result.json
├── repair_suggestions.md
└── final_report.md
```

---

## 二、常用命令

### 只生成需求、架构和任务

```bash
python -m ai_coding_agent.cli plan --idea "开发一个AI Coding项目自动开发Agent" --name my_agent
```

### 完整运行

```bash
python -m ai_coding_agent.cli run --idea "开发一个AI Coding项目自动开发Agent" --name my_agent
```

### 只重新测试

```bash
python -m ai_coding_agent.cli test --name my_agent
```

### 查看报告路径

```bash
python -m ai_coding_agent.cli report --name my_agent
```

---

## 三、接入真实 OpenAI API，可选

默认不需要 API。

如需真实大模型：

```bash
pip install openai
```

设置环境变量：

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="你的key"
```

macOS / Linux:

```bash
export OPENAI_API_KEY="你的key"
```

运行：

```bash
python -m ai_coding_agent.cli run --idea "开发一个AI Coding Agent" --name real_demo --provider openai
```

---

## 四、这个项目适合怎么写进申请材料？

可以写：

> 我构建了一个面向科研竞赛和 AI Coding 场景的项目自动开发 Agent。系统将项目开发过程拆分为需求分析、架构设计、任务拆解、代码生成、测试执行、错误分析和报告输出七个阶段，降低初学者完成复杂 AI 项目的门槛。该系统默认支持本地规则模式，也预留真实大模型接口，后续可接入 OpenAI 或本地大模型，实现更强的自动代码生成、自动测试和自动维护能力。

---

## 五、项目定位

这是一个“完整可运行原型”，适合：

1. 作为竞赛申报材料中的技术 Demo；
2. 作为 AI Coding 工作流展示；
3. 继续扩展成 Web 系统；
4. 继续扩展成多 Agent 自动开发平台。
