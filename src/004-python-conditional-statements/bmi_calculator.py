"""计算并判断身体质量指数，同时进行明确的输入校验。"""

from typing import Tuple


UNDERWEIGHT_LIMIT = 18.5
NORMAL_LIMIT = 24.9
OVERWEIGHT_LIMIT = 29.9


def calculate_bmi(height_m: float, weight_kg: float) -> float:
    """计算 BMI，并拒绝不合理的身高或体重。

    Args:
        height_m: 身高，单位为米。
        weight_kg: 体重，单位为千克。

    Returns:
        身体质量指数。

    Raises:
        ValueError: 身高或体重不大于零时抛出。
    """
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("height and weight must be greater than zero")
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """将 BMI 数值映射到课程示例中的健康范围。

    Args:
        bmi: 身体质量指数。

    Returns:
        BMI 对应的分类名称。
    """
    if bmi < UNDERWEIGHT_LIMIT:
        return "underweight"
    if bmi < NORMAL_LIMIT:
        return "normal range"
    if bmi < OVERWEIGHT_LIMIT:
        return "overweight"
    return "obese"


def evaluate_bmi(height_m: float, weight_kg: float) -> Tuple[float, str]:
    """计算一次 BMI，并同时返回数值和分类结果。

    Args:
        height_m: 身高，单位为米。
        weight_kg: 体重，单位为千克。

    Returns:
        包含 BMI 数值和分类名称的元组。
    """
    bmi = calculate_bmi(height_m, weight_kg)
    return bmi, classify_bmi(bmi)


def main() -> None:
    """从终端读取身高和体重，并打印评估结果。"""
    try:
        height_m = float(input("Height (m): "))
        weight_kg = float(input("Weight (kg): "))
        bmi, category = evaluate_bmi(height_m, weight_kg)
    except ValueError as error:
        print("Input error: {}".format(error))
        return

    print("BMI: {:.2f}".format(bmi))
    print("Assessment: {}".format(category))


if __name__ == "__main__":
    main()
