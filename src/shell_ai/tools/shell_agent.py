from pathlib import Path
from langchain_core.tools import tool


@tool
def write_new_file(file_path: str, content: str) -> str:
    """Create a new file with the provided content.

    Args:
        file_path: Path of the file to create.
        content: Content to write into the file.

    Returns:
        Success message or error description.
    """
    try:
        path = Path(file_path).expanduser().resolve()

        # Prevent overwriting existing files.
        if path.exists():
            return f"Error: File already exists: {path}"

        # Create parent directories if necessary.
        path.parent.mkdir(parents=True, exist_ok=True)

        # Create the file exclusively to avoid accidental overwrites.
        with path.open("x", encoding="utf-8") as file:
            file.write(content)

        return f"Successfully created file: {path}"

    except PermissionError:
        return f"Error: Permission denied: {file_path}"
    except OSError as e:
        return f"Error creating file: {e}"
