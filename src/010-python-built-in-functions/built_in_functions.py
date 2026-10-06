"""在成绩处理流程中使用具有代表性的内置函数。"""

from functools import reduce
from operator import add
from typing import List, Tuple


def summarize_scores(scores: List[int]) -> Tuple[int, float, List[int], List[int]]:
    """返回总分、平均分、及格成绩和降序排名。

    Args:
        scores: 成绩列表。

    Returns:
        包含总分、平均分、及格成绩和降序排名的元组。
    """
    total = reduce(add, scores, 0)
    average = round(total / len(scores), 2)
    passing = list(filter(lambda score: score >= 60, scores))
    ranking = sorted(scores, reverse=True)
    return total, average, passing, ranking


def main() -> None:
    """演示数值、类型转换、迭代和对象检查相关的内置函数。"""
    scores = [88, 59, 76, 95]
    total, average, passing, ranking = summarize_scores(scores)
    print("abs:", abs(-7), "max:", max(scores), "min:", min(scores))
    print("pow:", pow(2, 5), "divmod:", divmod(total, len(scores)))
    print("total:", total, "average:", average)
    print("passing:", passing, "ranking:", ranking)

    names = ["Ada", "Grace", "Linus", "Guido"]
    score_by_name = dict(zip(names, scores))
    print("enumerate:", list(enumerate(names, start=1)))
    print("score_by_name:", score_by_name)
    print("mapped scores:", list(map(lambda score: score + 5, scores)))
    print("all positive:", all(score > 0 for score in scores))
    print("any perfect score:", any(score == 100 for score in scores))

    print("binary:", bin(10), "hex:", hex(10))
    print("character:", chr(ord("A") + 1))
    print("types:", type(scores).__name__, isinstance(scores, list))
    print("length:", len(scores), "has append:", hasattr(scores, "append"))


if __name__ == "__main__":
    main()
