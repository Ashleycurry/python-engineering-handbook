"""使用 while 和 for 循环演示常见的流程控制方式。"""

from typing import Iterable, Optional


def factorial(number: int) -> int:
    """使用 while 循环计算整数的阶乘。

    Args:
        number: 需要计算阶乘的非负整数。

    Returns:
        number 的阶乘。

    Raises:
        ValueError: number 为负数时抛出。
    """
    if number < 0:
        raise ValueError("factorial is undefined for negative numbers")

    result = 1
    current = 1
    while current <= number:
        result *= current
        current += 1
    return result


def first_even(numbers: Iterable[int]) -> Optional[int]:
    """跳过奇数并返回第一个偶数。

    Args:
        numbers: 待遍历的整数序列。

    Returns:
        第一个偶数；没有偶数时返回 None。
    """
    for number in numbers:
        if number % 2:
            continue
        return number
    return None


def sum_until_limit(numbers: Iterable[int], limit: int) -> int:
    """累加非负数，直到下一个数会使总和超过上限。

    Args:
        numbers: 待遍历的整数序列。
        limit: 允许达到的总和上限。

    Returns:
        未超过上限时的累计总和。
    """
    total = 0
    for number in numbers:
        if number < 0:
            continue
        if total + number > limit:
            break
        total += number
    return total


def print_characters(text: str) -> None:
    """逐个打印字符串中的字符，以展示 for 循环的遍历过程。

    Args:
        text: 待拆分打印的字符串。
    """
    for character in text:
        print(character)


def main() -> None:
    """运行课程中的阶乘和字符串遍历案例。"""
    try:
        number = int(input("Integer: "))
    except ValueError:
        print("Input error: please enter an integer.")
        return

    text = input("Text: ")
    print("Factorial: {}".format(factorial(number)))
    print("Characters:")
    print_characters(text)
    print("First even: {}".format(first_even([1, 3, 7, 8, 10])))
    print("Limited sum: {}".format(sum_until_limit([4, -2, 5, 6], 10)))


if __name__ == "__main__":
    main()
