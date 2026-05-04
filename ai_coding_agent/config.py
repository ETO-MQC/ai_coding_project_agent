from dataclasses import dataclass
from pathlib import Path


@dataclass
class AgentConfig:
    workspace_dir: Path = Path("workspace")
    default_provider: str = "mock"
    openai_model: str = "gpt-4o-mini"

    def project_dir(self, name: str) -> Path:
        safe_name = "".join(ch if ch.isalnum() or ch in ("_", "-") else "_" for ch in name)
        return self.workspace_dir / safe_name
