from ai_coding_agent.config import AgentConfig
from ai_coding_agent.models import ProjectSpec
from ai_coding_agent.providers import get_provider
from ai_coding_agent.utils import ensure_dir, read_text
from ai_coding_agent.agents.requirement_agent import RequirementAgent
from ai_coding_agent.agents.architecture_agent import ArchitectureAgent
from ai_coding_agent.agents.task_agent import TaskAgent
from ai_coding_agent.agents.code_agent import CodeAgent
from ai_coding_agent.agents.test_agent import TestAgent
from ai_coding_agent.agents.repair_agent import RepairAgent
from ai_coding_agent.agents.report_agent import ReportAgent


class ProjectOrchestrator:
    def __init__(self, config: AgentConfig | None = None):
        self.config = config or AgentConfig()

    def _make_spec(self, name: str, idea: str) -> ProjectSpec:
        project_dir = self.config.project_dir(name)
        ensure_dir(project_dir)
        return ProjectSpec(name=name, idea=idea, project_dir=project_dir)

    def plan(self, name: str, idea: str, provider_name: str = "mock") -> ProjectSpec:
        spec = self._make_spec(name, idea)
        provider = get_provider(provider_name, self.config.openai_model)

        requirements = RequirementAgent(provider).run(spec)
        ArchitectureAgent(provider).run(spec, requirements)
        TaskAgent().run(spec)

        return spec

    def run(self, name: str, idea: str, provider_name: str = "mock") -> ProjectSpec:
        spec = self._make_spec(name, idea)
        provider = get_provider(provider_name, self.config.openai_model)

        requirements = RequirementAgent(provider).run(spec)
        architecture = ArchitectureAgent(provider).run(spec, requirements)
        tasks = TaskAgent().run(spec)
        CodeAgent().run(spec)
        test_result = TestAgent().run(spec)
        repair_suggestions = RepairAgent(provider).run(spec, test_result)
        ReportAgent(provider).run(
            spec=spec,
            requirements=requirements,
            architecture=architecture,
            tasks=tasks,
            test_result=test_result,
            repair_suggestions=repair_suggestions,
        )

        return spec

    def test(self, name: str) -> str:
        project_dir = self.config.project_dir(name)
        spec = ProjectSpec(name=name, idea="", project_dir=project_dir)
        result = TestAgent().run(spec)
        return f"success={result.success}, return_code={result.return_code}"

    def report_path(self, name: str) -> str:
        path = self.config.project_dir(name) / "final_report.md"
        if not path.exists():
            return f"报告不存在：{path}"
        return str(path)

    def read_report(self, name: str) -> str:
        path = self.config.project_dir(name) / "final_report.md"
        if not path.exists():
            return f"报告不存在：{path}"
        return read_text(path)
