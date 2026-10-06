"""演示可复用函数、参数形式和模块导入。"""

import math
from statistics import mean
from typing import Dict, List, Tuple


def rectangle_area(width: float, height: float) -> float:
    """根据两个位置参数计算矩形面积。

    Args:
        width: 矩形宽度。
        height: 矩形高度。

    Returns:
        矩形面积。
    """
    return width * height


def calculate_sum_and_product(*numbers: float) -> Tuple[float, float]:
    """根据不定长参数返回总和与乘积。

    Args:
        *numbers: 参与计算的数字。

    Returns:
        包含总和与乘积的元组。
    """
    total = sum(numbers)
    product = 1.0
    for number in numbers:
        product *= number
    return total, product


def describe_student(name: str, age: int = 18) -> str:
    """生成学生基本信息，未提供年龄时使用默认值。

    Args:
        name: 学生姓名。
        age: 学生年龄，默认值为 18。

    Returns:
        格式化后的学生信息。
    """
    return "{} is {} years old".format(name, age)


def build_profile(name: str, *, city: str, **details: str) -> Dict[str, str]:
    """组合必填参数、仅限关键字参数和额外字段。

    Args:
        name: 用户姓名。
        city: 用户所在城市，必须使用关键字传入。
        **details: 其他用户信息。

    Returns:
        用户信息字典。
    """
    profile = {"name": name, "city": city}
    profile.update(details)
    return profile


def append_score(scores: List[int], score: int) -> None:
    """向可变列表中追加一个成绩。

    Args:
        scores: 待修改的成绩列表。
        score: 需要追加的成绩。
    """
    scores.append(score)


def reassign_score(score: int) -> int:
    """返回递增后的整数，以展示整数不可变的特性。

    Args:
        score: 原始成绩。

    Returns:
        加一后的成绩。
    """
    return score + 1


def main() -> None:
    """运行参数、返回值、可变性和模块导入案例。"""
    print("Area:", rectangle_area(width=4, height=5))
    print("Student:", describe_student("Alex"))
    print("Student:", describe_student(age=20, name="Alex"))
    print("Sum and product:", calculate_sum_and_product(2, 3, 4))
    print("Profile:", build_profile("Alex", city="Shanghai", role="developer"))

    scores = [80, 90]
    append_score(scores, 95)
    score = 80
    print("Mutable list:", scores)
    print("Immutable integer:", score, "->", reassign_score(score))

    print("Square root:", math.sqrt(16))
    print("Average:", mean(scores))


if __name__ == "__main__":
    main()
