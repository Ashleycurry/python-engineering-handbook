"""演示列表、元组、集合和字典的常见操作。"""

from typing import Dict, List, Tuple


def list_example() -> List[str]:
    """演示列表的索引、有序性和可变操作。

    Returns:
        操作后的语言名称列表。
    """
    languages = ["python", "java"]
    languages.append("go")
    languages.insert(1, "rust")
    languages.remove("java")
    languages.sort()
    return languages


def tuple_example() -> Tuple[str, int, str]:
    """返回一个不应被原地修改的固定记录。

    Returns:
        包含姓名、年龄和职业的元组。
    """
    return ("Ada", 36, "engineer")


def set_example() -> set:
    """利用集合特性去除重复值。

    Returns:
        去重后的技能名称集合。
    """
    return {"python", "python", "sql", "go"}


def dictionary_example() -> Dict[str, object]:
    """使用基于键的访问和更新操作管理相关字段。

    Returns:
        更新后的用户信息字典。
    """
    profile = {"name": "Ada", "skills": ["python"]}
    profile.update({"level": "senior"})
    return profile


def main() -> None:
    """打印具有代表性的容器操作及其结果。"""
    languages = list_example()
    print("List:", languages)
    print("Index of python:", languages.index("python"))

    person = tuple_example()
    print("Tuple name:", person[0])

    print("Set:", sorted(set_example()))

    profile = dictionary_example()
    print("Dictionary name:", profile.get("name"))
    print("Dictionary keys:", list(profile.keys()))
    print("Dictionary items:", list(profile.items()))


if __name__ == "__main__":
    main()
