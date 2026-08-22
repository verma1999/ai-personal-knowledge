from pathlib import Path

DOCS_DIR = Path("../docs")


def find_documents():
    for file in DOCS_DIR.rglob("*"):
        if file.is_file() and file.suffix in [".pdf", ".md", ".txt"]:
                print(f"Found document: {file}")


if __name__ == "__main__":
    find_documents()