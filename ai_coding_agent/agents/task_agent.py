from typing import List
from ai_coding_agent.models import ProjectSpec, Task
from ai_coding_agent.utils import write_json


class TaskAgent:
    def run(self, spec: ProjectSpec) -> List[Task]:
        tasks = [
            Task("T001", "创建项目结构", "创建 generated_app 目录和基础文件。"),
            Task("T002", "实现核心函数", "实现一个可测试的核心业务函数。"),
            Task("T003", "编写单元测试", "为核心函数编写 pytest 测试。"),
            Task("T004", "执行测试", "运行 pytest 并记录结果。"),
            Task("T005", "生成报告", "汇总需求、架构、任务和测试结果。"),
        ]
        write_json(spec.project_dir / "tasks.json", [task.to_dict() for task in tasks])
        return tasks
