from ai_coding_agent.models import ProjectSpec
from ai_coding_agent.providers import BaseLLMProvider
from ai_coding_agent.utils import write_text


class ArchitectureAgent:
    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def run(self, spec: ProjectSpec, requirements: str) -> str:
        prompt = f"""
请基于以下需求输出 architecture 架构设计。

项目名称：{spec.name}
项目想法：{spec.idea}

需求文档：
{requirements}

输出要求：
1. 总体架构
2. 模块划分
3. 数据流
4. 目录结构
5. 后续扩展方向
"""
        result = self.provider.generate(prompt)
        write_text(spec.project_dir / "architecture.md", result)
        return result
