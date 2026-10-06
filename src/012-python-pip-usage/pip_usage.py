"""通过当前 Python 解释器检查 pip，且不修改已安装的软件包。"""

import subprocess
import sys
from typing import List, Tuple


def run_pip(*arguments: str) -> Tuple[int, str, str]:
    """运行只读 pip 命令，并返回状态码、标准输出和错误输出。

    Args:
        *arguments: 传递给 pip 的命令参数。

    Returns:
        包含进程状态码、标准输出和错误输出的元组。
    """
    command: List[str] = [sys.executable, "-m", "pip"]
    command.extend(arguments)
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    stdout, stderr = process.communicate()
    return process.returncode, stdout.strip(), stderr.strip()


def main() -> None:
    """显示当前 pip 版本和安全的命令格式。"""
    return_code, output, error = run_pip("--version")
    if return_code == 0:
        print(output)
    else:
        print("pip is unavailable: {}".format(error))

    # 安装和卸载命令仅用于学习展示，不会实际执行。
    command_examples = [
        ["install", "package-name"],
        ["uninstall", "package-name"],
        ["list"],
        ["show", "package-name"],
    ]
    print("Command patterns:")
    for arguments in command_examples:
        print("  {} -m pip {}".format(
            sys.executable, " ".join(arguments)
        ))


if __name__ == "__main__":
    main()
