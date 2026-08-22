from dataclasses import dataclass
from pathlib import Path

@dataclass
class Document:
    id: str
    path: Path
    content: str