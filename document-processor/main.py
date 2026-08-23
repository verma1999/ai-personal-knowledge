from pathlib import Path
from models.document import Document
from uuid import uuid4
from models.chunk import Chunk


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

def chunk_document(document) -> list[Chunk]:
        index = 0
        chunk_size = 100
        overlap = 1 #overlap sentences
        chunks = []
        current_chunk = []
        sentences = [
            sentence.strip() + "."
            for sentence in document.content.split(".")
            if sentence.strip()
        ]
        for sentence in sentences:
            current_chunk_length = len(" ".join(current_chunk))
            if current_chunk_length + len(sentence) <= chunk_size:
                current_chunk.append(sentence)
            else:
                if current_chunk:
                    chunks.append(
                        Chunk(
                            id=str(uuid4()),
                            document_id=document.id,
                            content=" ".join(current_chunk),
                            chunk_index=index,
                            metadata={}
                        )
                    )
                    index += 1
                overlap_text = current_chunk[-overlap:]
                current_chunk = overlap_text.copy()
                current_chunk.append(sentence)

        if current_chunk:
            chunks.append(
                Chunk(
                    id=str(uuid4()),
                    document_id=document.id,
                    content=" ".join(current_chunk),
                    chunk_index=index,
                    metadata={}
                )
            )
        return chunks


if __name__ == "__main__":
    find_documents()
    #print(documents)
    for document in documents:
        chunks = chunk_document(document)
        print(f"\nDOCUMENT: {document.path}")
        for chunk in chunks:
            print(chunk)