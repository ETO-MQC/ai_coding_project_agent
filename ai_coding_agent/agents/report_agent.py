from typing import List
from ai_coding_agent.models import ProjectSpec, Task, TestResult
from ai_coding_agent.providers import BaseLLMProvider
from ai_coding_agent.utils import write_text


class ReportAgent:
    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def run(
        self,
        spec: ProjectSpec,
        requirements: str,
        architecture: str,
        tasks: List[Task],
        test_result: TestResult,
        repair_suggestions: str,
    ) -> str:
        task_lines = "\n".join(
            f"- {task.id}: {task.title} / {task.status} / {task.description}"
            for task in tasks
        )

        content = f"""# {spec.name} 最终开发报告

## 1. 项目想法

{spec.idea}

## 2. 需求分析摘要

{requirements}

## 3. 架构设计摘要

{architecture}

## 4. 任务列表

{task_lines}

## 5. 测试结果

- 是否通过：{test_result.success}
- 返回码：{test_result.return_code}

### stdout

```text
{test_result.stdout}
```

### stderr

```text
{test_result.stderr}
```

## 6. 修复建议

{repair_suggestions}

## 7. 后续扩展

1. 接入真实 LLM Provider。
2. 增加自动代码修改能力。
3. 增加多轮测试与自动回归。
4. 增加 Web 可视化界面。
5. 支持读取已有 Git 项目并自动分析技术债。
"""
        write_text(spec.project_dir / "final_report.md", content)
        return content
