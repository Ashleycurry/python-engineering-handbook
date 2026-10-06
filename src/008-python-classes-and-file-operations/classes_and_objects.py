"""演示类、继承和多态方法调用。"""

from typing import List


class Animal:
    """包含共享状态和行为的动物基类。"""

    kingdom = "animal"

    def __init__(self, name: str) -> None:
        """初始化动物对象。

        Args:
            name: 动物名称。
        """
        self.name = name

    def speak(self) -> str:
        """返回基类的默认叫声。

        Returns:
            默认叫声。
        """
        return "..."

    def describe(self) -> str:
        """返回所有动物对象共享的描述信息。

        Returns:
            包含名称和叫声的描述文本。
        """
        return "{} says {}".format(self.name, self.speak())


class Dog(Animal):
    """重写动物基类行为的狗类。"""

    def speak(self) -> str:
        """返回狗的叫声。

        Returns:
            狗的叫声。
        """
        return "woof"


class Cat(Animal):
    """重写动物基类行为的猫类。"""

    def speak(self) -> str:
        """返回猫的叫声。

        Returns:
            猫的叫声。
        """
        return "meow"


def main() -> None:
    """创建对象，并通过统一接口调用相同的方法。"""
    animals: List[Animal] = [Dog("Buddy"), Cat("Mimi")]
    print("Class attribute:", Animal.kingdom)
    for animal in animals:
        print(animal.describe())


if __name__ == "__main__":
    main()
