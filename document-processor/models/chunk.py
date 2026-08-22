from dataclasses import dataclass
from pathlib import Path

@dataclass
class Chunk:
    id: str
    document_id: str
    content: str
    chunk_index: int
    metadata: dict