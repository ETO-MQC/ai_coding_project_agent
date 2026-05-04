from ai_coding_agent.config import AgentConfig
from ai_coding_agent.models import Task


def test_project_dir_safe_name():
    config = AgentConfig()
    assert str(config.project_dir("hello world")).endswith("hello_world")


def test_task_to_dict():
    task = Task("T001", "title", "desc")
    data = task.to_dict()
    assert data["id"] == "T001"
    assert data["status"] == "todo"
