"""检查 Python 运行环境，并对比两种简单的设计方式。"""

import platform
from typing import Dict, List


def describe_runtime() -> Dict[str, str]:
    """返回检查 Python 安装情况时有用的运行环境信息。

    Returns:
        包含 Python 版本、实现方式和平台信息的字典。
    """
    return {
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
    }


def calculate_total(prices: List[float]) -> float:
    """使用面向过程的函数计算价格总和。

    Args:
        prices: 商品价格列表。

    Returns:
        商品价格总和。
    """
    return sum(prices)


class ShoppingCart:
    """保存商品价格，并通过对象方法提供求和操作。"""

    def __init__(self, prices: List[float]) -> None:
        """初始化购物车。

        Args:
            prices: 商品价格列表。
        """
        self.prices = prices

    def total(self) -> float:
        """计算当前购物车中的价格总和。

        Returns:
            当前购物车的价格总和。
        """
        return sum(self.prices)


def main() -> None:
    """打印 Python 环境信息，并对比两种编程设计方式。"""
    print("Python runtime:")
    for name, value in describe_runtime().items():
        print("  {}: {}".format(name, value))

    prices = [19.9, 29.5, 10.0]
    print("Procedural total: {:.2f}".format(calculate_total(prices)))
    print("Object-oriented total: {:.2f}".format(ShoppingCart(prices).total()))


if __name__ == "__main__":
    main()
