"""处理常见的输入和算术异常，同时保留明确的错误信息。"""

from typing import Optional


def parse_integer(value: str) -> Optional[int]:
    """将文本转换为整数，输入无效时返回 None。

    Args:
        value: 待转换的文本。

    Returns:
        转换后的整数；转换失败时返回 None。
    """
    try:
        return int(value)
    except ValueError:
        return None


def safe_divide(numerator_text: str, denominator_text: str) -> str:
    """使用 try、except、else 和 finally 处理一次除法操作。

    Args:
        numerator_text: 被除数文本。
        denominator_text: 除数文本。

    Returns:
        计算结果或面向用户的错误说明。
    """
    try:
        numerator = float(numerator_text)
        denominator = float(denominator_text)
        result = numerator / denominator
    except ValueError:
        return "Input must be numeric."
    except ZeroDivisionError:
        return "The denominator cannot be zero."
    else:
        return "Result: {:.2f}".format(result)
    finally:
        # 清理和审计逻辑应放在这里，因为该代码块始终会执行。
        pass


def main() -> None:
    """运行成功和失败两类具有代表性的操作。"""
    for value in ("42", "not-a-number"):
        parsed = parse_integer(value)
        print("parse_integer({!r}) -> {}".format(value, parsed))

    for numerator, denominator in (("12", "3"), ("12", "0"), ("x", "2")):
        print("safe_divide({}, {}) -> {}".format(
            numerator, denominator, safe_divide(numerator, denominator)
        ))


if __name__ == "__main__":
    main()
