from ai_coding_agent.models import ProjectSpec, TestResult
from ai_coding_agent.providers import BaseLLMProvider
from ai_coding_agent.utils import write_text


class RepairAgent:
    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def run(self, spec: ProjectSpec, test_result: TestResult) -> str:
        if test_result.success:
            content = "# 修复建议\n\n测试已通过，当前不需要修复。\n"
            write_text(spec.project_dir / "repair_suggestions.md", content)
            return content

        prompt = f"""
请基于以下测试结果输出 repair 修复建议。

return_code:
{test_result.return_code}

stdout:
{test_result.stdout}

stderr:
{test_result.stderr}

输出要求：
1. 错误原因判断
2. 最小修复步骤
3. 后续预防规则
"""
        content = self.provider.generate(prompt)
        write_text(spec.project_dir / "repair_suggestions.md", content)
        return content
