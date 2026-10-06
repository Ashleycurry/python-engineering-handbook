"""使用线程和可重入锁安全地更新共享状态。"""

import threading
from typing import Dict


def increment_counter(
    counter: Dict[str, int],
    lock: threading.RLock,
    iterations: int,
) -> None:
    """在每次更新时持有锁，递增共享计数器。

    Args:
        counter: 保存共享计数值的字典。
        lock: 用于保护共享数据的可重入锁。
        iterations: 每个线程执行的递增次数。
    """
    for _ in range(iterations):
        with lock:
            counter["value"] += 1


def main() -> None:
    """启动工作线程，等待执行完成并检查同步结果。"""
    counter = {"value": 0}
    lock = threading.RLock()
    worker_count = 4
    iterations_per_worker = 1000

    threads = [
        threading.Thread(
            target=increment_counter,
            args=(counter, lock, iterations_per_worker),
            name="counter-worker-{}".format(index),
        )
        for index in range(worker_count)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    expected = worker_count * iterations_per_worker
    print("Counter:", counter["value"])
    print("Expected:", expected)
    print("Synchronized:", counter["value"] == expected)


if __name__ == "__main__":
    main()
