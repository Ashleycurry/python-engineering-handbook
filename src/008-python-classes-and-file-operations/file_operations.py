"""读写文本文件，并保持案例自包含。"""

from pathlib import Path
import tempfile
from typing import List


def write_and_read_file() -> List[str]:
    """向临时文本文件写入、追加并读取多行内容。

    Returns:
        去除换行符后的文件内容列表。
    """
    # 使用临时目录，避免教学案例在项目中留下无关文件。
    with tempfile.TemporaryDirectory() as directory:
        file_path = Path(directory) / "notes.txt"

        with file_path.open("w", encoding="utf-8") as file_object:
            file_object.write("first line\n")

        with file_path.open("a", encoding="utf-8") as file_object:
            file_object.write("second line\n")

        with file_path.open("r", encoding="utf-8") as file_object:
            return [line.strip() for line in file_object.readlines()]


def main() -> None:
    """打印从临时文件中读取的文本行。"""
    for line_number, line in enumerate(write_and_read_file(), start=1):
        print("{}: {}".format(line_number, line))


if __name__ == "__main__":
    main()
