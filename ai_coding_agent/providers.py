from abc import ABC, abstractmethod
import os
from typing import Optional


class BaseLLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class MockLLMProvider(BaseLLMProvider):
    """
    本地模拟 Provider。
    不需要任何 API Key，用于跑通完整流程。
    """

    def generate(self, prompt: str) -> str:
        lower = prompt.lower()

        if "requirements" in lower or "需求" in prompt:
            return (
                "# 需求分析\n\n"
                "## 核心痛点\n"
                "1. 初学者不知道如何把项目想法拆成可执行模块。\n"
                "2. AI Coding 一次性生成代码时容易结构混乱。\n"
                "3. 缺少测试、错误分析和最终报告。\n\n"
                "## 目标用户\n"
                "科研竞赛参与者、课程设计学生、AI Coding 初学者。\n\n"
                "## MVP 功能\n"
                "1. 输入项目名称和项目想法。\n"
                "2. 自动生成需求文档。\n"
                "3. 自动生成架构文档。\n"
                "4. 自动拆分任务。\n"
                "5. 自动生成示例代码。\n"
                "6. 自动运行测试。\n"
                "7. 自动输出最终报告。\n\n"
                "## 验收标准\n"
                "运行一条命令后，workspace 中出现完整项目资料，并且示例代码测试通过。\n"
            )

        if "architecture" in lower or "架构" in prompt:
            return (
                "# 架构设计\n\n"
                "## 总体架构\n"
                "系统采用 CLI + Orchestrator + 多 Agent 模块架构。\n\n"
                "## 模块划分\n"
                "1. CLI：接收用户输入。\n"
                "2. Orchestrator：调度所有 Agent。\n"
                "3. RequirementAgent：生成需求。\n"
                "4. ArchitectureAgent：生成架构。\n"
                "5. TaskAgent：拆解任务。\n"
                "6. CodeAgent：生成代码。\n"
                "7. TestAgent：运行测试。\n"
                "8. RepairAgent：分析错误。\n"
                "9. ReportAgent：生成报告。\n\n"
                "## 数据流\n"
                "idea -> requirements.md -> architecture.md -> tasks.json -> generated_app -> test_result.json -> final_report.md\n"
            )

        if "repair" in lower or "修复" in prompt:
            return (
                "# 修复建议\n\n"
                "1. 先阅读 test_result.json 的 stderr。\n"
                "2. 检查 Python 语法错误。\n"
                "3. 检查依赖是否安装。\n"
                "4. 优先修复最小失败测试。\n"
                "5. 修复后重新运行 pytest。\n"
            )

        return "MockLLMProvider 已生成默认内容。"


class OpenAIProvider(BaseLLMProvider):
    """
    可选真实 LLM Provider。
    使用前需要：
    pip install openai
    设置 OPENAI_API_KEY
    """

    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("请先安装 openai：pip install openai") from exc

        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("缺少 OPENAI_API_KEY 环境变量")

        client = OpenAI()
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是严谨的软件工程 Agent，输出结构清晰、可执行。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content or ""


def get_provider(name: str, model: Optional[str] = None) -> BaseLLMProvider:
    if name == "mock":
        return MockLLMProvider()
    if name == "openai":
        return OpenAIProvider(model=model or "gpt-4o-mini")
    raise ValueError(f"未知 provider: {name}")
