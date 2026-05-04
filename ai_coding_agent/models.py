from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict


@dataclass
class ProjectSpec:
    name: str
    idea: str
    project_dir: Path

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["project_dir"] = str(self.project_dir)
        return data


@dataclass
class Task:
    id: str
    title: str
    description: str
    status: str = "todo"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TestResult:
    success: bool
    return_code: int
    stdout: str
    stderr: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
