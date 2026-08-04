from pathlib import Path

import pandas as pd


class FileReader:
    """Read CSV or Excel files."""

    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx",
        #        ".xls",
    }

    @classmethod
    def read(
        cls,
        file_path: str | Path,
    ) -> list[dict]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if path.suffix.lower() not in cls.ALLOWED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {path.suffix}")

        if path.suffix.lower() == ".csv":
            dataframe = pd.read_csv(path)
        else:
            dataframe = pd.read_excel(path)

        return dataframe.to_dict(orient="records")
