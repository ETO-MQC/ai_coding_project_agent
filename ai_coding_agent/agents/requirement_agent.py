from ai_coding_agent.models import ProjectSpec
from ai_coding_agent.providers import BaseLLMProvider
from ai_coding_agent.utils import write_text


class RequirementAgent:
    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def run(self, spec: ProjectSpec) -> str:
        prompt = f"""
请进行 requirements 需求分析。

项目名称：{spec.name}
项目想法：{spec.idea}

输出要求：
1. 核心痛点
2. 目标用户
3. MVP 功能
4. 非功能需求
5. 验收标准
"""
        result = self.provider.generate(prompt)
        write_text(spec.project_dir / "requirements.md", result)
        return result
