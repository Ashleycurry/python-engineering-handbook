"""使用字符串、表达式和 print 参数介绍基本输出。"""


def main() -> None:
    """运行一个结果固定的第一个 Python 程序示例。"""
    print("Hello World")
    print("Python", "engineering", "handbook", sep=" | ")
    print("This line continues with end=", end="")
    print(" and finishes here.")
    print("2 + 3 =", 2 + 3)


if __name__ == "__main__":
    main()
