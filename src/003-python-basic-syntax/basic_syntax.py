"""演示易读的 Python 语法、命名方式和常见数据类型。"""

import keyword
from typing import Any, Dict


def describe_values(values: Dict[str, Any]) -> None:
    """打印每个值的类型，同时不修改原始数据。

    Args:
        values: 需要检查类型的键值对。
    """
    for name, value in values.items():
        print("{:<12} -> {}".format(name, type(value).__name__))


def main() -> None:
    """通过一个可执行的小案例展示 Python 语法规范。"""
    # 将相关数据集中管理，并使用具有描述性的 snake_case 名称。
    values = {
        "integer": 42,
        "decimal": 3.14,
        "enabled": True,
        "message": "Python",
        "items": [1, 2, 3],
        "coordinates": (10, 20),
        "settings": {"theme": "light"},
        "unique_values": {1, 2, 3},
    }

    describe_values(values)
    print("Keywords: {}".format(", ".join(keyword.kwlist)))


if __name__ == "__main__":
    main()
