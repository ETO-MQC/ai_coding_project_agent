import sys
from ai_coding_agent.models import ProjectSpec, TestResult
from ai_coding_agent.utils import run_command, write_json


class TestAgent:
    def run(self, spec: ProjectSpec) -> TestResult:
        app_dir = spec.project_dir / "generated_app"

        if not app_dir.exists():
            result = TestResult(
                success=False,
                return_code=1,
                stdout="",
                stderr="generated_app 不存在，请先运行 CodeAgent。",
            )
            write_json(spec.project_dir / "test_result.json", result.to_dict())
            return result

        raw = run_command([sys.executable, "-m", "pytest", "-q"], cwd=app_dir, timeout=60)
        result = TestResult(
            success=raw["return_code"] == 0,
            return_code=raw["return_code"],
            stdout=raw["stdout"],
            stderr=raw["stderr"],
        )
        write_json(spec.project_dir / "test_result.json", result.to_dict())
        return result
