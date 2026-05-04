from ai_coding_agent.models import ProjectSpec
from ai_coding_agent.utils import ensure_dir, write_text


class CodeAgent:
    """
    生成一个示例 Python 项目。
    后续可以把这里替换为真实 LLM 代码生成。
    """

    def run(self, spec: ProjectSpec) -> None:
        app_dir = spec.project_dir / "generated_app"
        package_dir = app_dir / "src" / "generated_app"
        test_dir = app_dir / "tests"

        ensure_dir(package_dir)
        ensure_dir(test_dir)

        write_text(app_dir / "README.md", f"""# {spec.name} Generated App

这是由 AI Coding 项目自动开发 Agent 生成的示例应用。

原始想法：

{spec.idea}
""")

        write_text(package_dir / "__init__.py", "")

        write_text(package_dir / "core.py", """
def normalize_idea(text: str) -> str:
    """
    把用户输入的项目想法进行基础清洗。
    """
    if not isinstance(text, str):
        raise TypeError("text must be str")
    return " ".join(text.strip().split())


def estimate_project_complexity(idea: str) -> str:
    """
    非严格复杂度估计：
    - 内容较短：simple
    - 内容中等：medium
    - 内容较长：hard
    """
    cleaned = normalize_idea(idea)
    length = len(cleaned)

    if length < 30:
        return "simple"
    if length < 120:
        return "medium"
    return "hard"


def make_project_summary(name: str, idea: str) -> dict:
    """
    输出一个结构化项目摘要。
    """
    return {
        "name": normalize_idea(name),
        "idea": normalize_idea(idea),
        "complexity": estimate_project_complexity(idea),
    }
""")

        write_text(test_dir / "test_core.py", """
from generated_app.core import normalize_idea, estimate_project_complexity, make_project_summary
import pytest


def test_normalize_idea():
    assert normalize_idea("  hello    world  ") == "hello world"


def test_normalize_idea_type_error():
    with pytest.raises(TypeError):
        normalize_idea(123)


def test_estimate_project_complexity():
    assert estimate_project_complexity("短项目") == "simple"
    assert estimate_project_complexity("这是一个中等长度的项目想法，需要自动生成代码和测试") in {"simple", "medium"}
    assert estimate_project_complexity("A" * 200) == "hard"


def test_make_project_summary():
    summary = make_project_summary(" demo ", "  build   an app ")
    assert summary["name"] == "demo"
    assert summary["idea"] == "build an app"
    assert summary["complexity"] in {"simple", "medium", "hard"}
""")

        write_text(app_dir / "pyproject.toml", """
[project]
name = "generated-app"
version = "0.1.0"
description = "Generated app by AI Coding Project Agent"
requires-python = ">=3.9"

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
""")
