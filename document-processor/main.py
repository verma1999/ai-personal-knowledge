from pathlib import Path
from models.document import Document
from uuid import uuid4


DOCS_DIR = Path("../docs")
documents = []

def find_documents():
    for file in DOCS_DIR.rglob("*"):
        if file.is_file() and file.suffix in [".pdf", ".md", ".txt"]:
                document = read_document(file)
                documents.append(document)
    return documents

def read_document(file) -> Document:
    with open(file, "r") as f:
        content = f.read()
        return Document(
            id=str(uuid4()),
            path=file, 
            content=content
        )


if __name__ == "__main__":
    find_documents()
    print(documents)