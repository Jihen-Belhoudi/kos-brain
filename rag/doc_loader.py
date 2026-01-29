from pathlib import Path
from pypdf import PdfReader

def load_docs(folder="data"):
    docs = []
    folder = Path(folder)

    if not folder.exists():
        raise FileNotFoundError(f"Data folder not found: {folder}")

    for f in folder.glob("*"):
        if f.suffix.lower() == ".pdf":
            reader = PdfReader(str(f))
            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )
            if text.strip():
                docs.append(text)

        elif f.suffix.lower() in [".txt", ".md"]:
            text = f.read_text(encoding="utf-8")
            if text.strip():
                docs.append(text)

    if not docs:
        raise ValueError("No valid documents found in data folder")

    return docs