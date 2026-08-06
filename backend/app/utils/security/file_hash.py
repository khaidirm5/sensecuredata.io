from hashlib import sha256
from pathlib import Path


class FileHash:
    @staticmethod
    def generate(
        file_path: str | Path,
    ) -> str:
        hasher = sha256()

        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hasher.update(chunk)

        return hasher.hexdigest()
