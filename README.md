# Python Engineering Handbook

一个面向 Python 初学者的课程笔记与案例仓库，内容主要整理自 `课件/` 中的课程资料，并参考《Python 编程入门与实践（微视频版）》补充学习路线和知识笔记。

本仓库强调：先理解基础概念，再通过小案例练习，最后形成清晰、可维护、可复用的代码习惯。

# 学习路线

建议按以下顺序学习：

`Python 环境 -> 基础语法 -> 条件与循环 -> 函数与模块 -> 容器 -> 类与文件 -> 异常 -> 内置函数 -> 多线程 -> pip -> NumPy`

课程案例位于 `src/`，每个课程目录使用三位编号和英文名称，便于在 GitHub 中阅读和检索。

## 目录结构

```text
python-engineering-handbook/
├── README.md
├── 课件/
│   ├── 001_Python介绍与安装/
│   ├── 002_第一个程序-“Hello World”/
│   ├── 003_Python基础语法/
│   ├── 004_Python条件语句/
│   ├── 005_Python循环语句/
│   ├── 006_Python函数和模块/
│   ├── 007_Python容器类型与相关操作/
│   ├── 008_Python类和文件操作/
│   ├── 009_Python异常处理/
│   ├── 010_Python内置函数/
│   ├── 011_Python多线程/
│   ├── 012_Python PiP的使用/
│   ├── 013_Python Numpy基础操作/
│   └── Python编程入门与实践-清华大学.pdf
└── src/
    ├── 001-python-introduction-and-installation/
    ├── 002-first-hello-world-program/
    ├── 003-python-basic-syntax/
    ├── 004-python-conditional-statements/
    ├── 005-python-loops/
    ├── 006-python-functions-and-modules/
    ├── 007-python-containers-and-operations/
    ├── 008-python-classes-and-file-operations/
    ├── 009-python-exception-handling/
    ├── 010-python-built-in-functions/
    ├── 011-python-multithreading/
    ├── 012-python-pip-usage/
    └── 013-python-numpy-basics/
```

## 主课程

主课程目录参考 `课件/` 的 13 个课程主题。每个章节都对应 `src/` 中的可运行案例。

### 001 Python 介绍与安装

学习 Python 的语言特点、跨平台特性、运行环境检查，以及面向过程与面向对象设计思路的初步对比。

案例：[`python_environment.py`](src/001-python-introduction-and-installation/python_environment.py)

### 002 第一个程序：Hello World

学习字符串表示、`print()`、多个对象输出、`sep`、`end` 和简单表达式。

案例：[`hello_world.py`](src/002-first-hello-world-program/hello_world.py)

### 003 Python 基础语法

学习注释、缩进、PEP 8、标识符、关键字，以及数字、字符串、列表、元组、字典和集合。

案例：[`basic_syntax.py`](src/003-python-basic-syntax/basic_syntax.py)

### 004 Python 条件语句

学习算术和关系运算、逻辑运算、成员判断、`if`、`elif` 和 `else` 多分支结构。

案例：[`bmi_calculator.py`](src/004-python-conditional-statements/bmi_calculator.py)

### 005 Python 循环语句

学习 `while`、`for`、`break`、`continue`、`pass`、阶乘计算和字符串遍历。

案例：[`loops_demo.py`](src/005-python-loops/loops_demo.py)

### 006 Python 函数和模块

学习函数定义与返回值、位置参数、默认参数、可变参数、关键字参数、可变性和模块导入。

案例：[`functions_and_modules.py`](src/006-python-functions-and-modules/functions_and_modules.py)

### 007 Python 容器类型与相关操作

学习列表、元组、集合和字典的特点，以及增删改查、去重和更新操作。

案例：[`containers_and_operations.py`](src/007-python-containers-and-operations/containers_and_operations.py)

### 008 Python 类和文件操作

本章对应课件中的两个小节。

#### 类和对象

学习类与对象、属性、构造方法、继承、多态和方法重写。

案例：[`classes_and_objects.py`](src/008-python-classes-and-file-operations/classes_and_objects.py)

#### 文件操作

学习文件名、路径、文本文件、二进制文件，以及文件的读取、写入和追加。

案例：[`file_operations.py`](src/008-python-classes-and-file-operations/file_operations.py)

### 009 Python 异常处理

学习常见异常、`try`、`except`、`else`、`finally`，以及只捕获能够明确处理的异常。

案例：[`exception_handling.py`](src/009-python-exception-handling/exception_handling.py)

### 010 Python 内置函数

学习数值运算、类型转换、进制转换、序列处理、排序、过滤、映射、聚合和对象检查。

案例：[`built_in_functions.py`](src/010-python-built-in-functions/built_in_functions.py)

### 011 Python 多线程

学习进程与线程、`threading.Thread`、`join()`、共享数据和 `RLock` 同步。

案例：[`threading_demo.py`](src/011-python-multithreading/threading_demo.py)

### 012 Python pip 的使用

学习 pip 的作用、版本检查、软件包列表、软件包信息，以及安装和卸载命令格式。

案例：[`pip_usage.py`](src/012-python-pip-usage/pip_usage.py)

### 013 Python NumPy 基础操作

学习数组创建、索引、切片、布尔筛选、形状变换、合并和拆分。

案例：[`numpy_basics.py`](src/013-python-numpy-basics/numpy_basics.py)

## 运行案例

建议使用 Python 3.9 或更高版本。先检查 Python 版本：

```bash
python --version
```

运行普通案例：

```bash
python src/002-first-hello-world-program/hello_world.py
python src/003-python-basic-syntax/basic_syntax.py
```

运行带交互输入的案例：

```bash
python src/004-python-conditional-statements/bmi_calculator.py
python src/005-python-loops/loops_demo.py
```

运行 NumPy 案例前安装依赖：

```bash
python -m pip install numpy
python src/013-python-numpy-basics/numpy_basics.py
```

除 NumPy 案例外，主课程案例主要使用 Python 标准库。`pip_usage.py` 只查询 pip 版本并展示命令格式，不会自动安装或卸载软件包。

## 工程化约定

 - 每个案例都可以作为独立脚本运行。
 - 使用 `if __name__ == "__main__":` 作为脚本入口。
 - 函数和类使用中文文档字符串，说明职责、参数、返回值和可预期异常。
 - 优先使用清晰的命名、明确的边界校验和标准库能力。
 - 文件资源使用上下文管理器，线程共享数据使用锁保护。
 - 示例保持单一主题，避免为了展示功能而引入无关复杂度。
 - 验证代码时关注语法、输入边界、资源释放和可复现性。

## 补充篇：参考书学习笔记

以下内容来自《Python 编程入门与实践（微视频版）》的章节结构，并结合当前课件进行对照整理。补充篇只记录当前课件没有系统覆盖的知识点，不新增代码实现。

### 补充 1：开发工具与帮助系统

课件介绍了 Python 环境和 PyCharm，参考书还介绍了 IDLE 的启动、编辑、运行和调试流程。学习时可以理解三类工具的定位：

 - 命令行解释器适合快速验证语法和表达式。
 - IDLE 适合初学者观察交互执行、编辑和调试过程。
 - PyCharm 适合组织项目、管理解释器、运行脚本和维护较大代码。

参考书还强调了帮助系统的使用，包括查看内置函数、类型、模块成员和完整模块信息。遇到不熟悉的标准库接口时，先阅读对象自身的帮助信息，再查阅官方文档。

### 补充 2：变量、常量与表达式

参考书进一步区分了变量、常量、空值、类型转换、运算符和表达式。学习时应重点掌握：

 - `None` 表示“没有值”或“尚未得到结果”，不等同于 `0`、空字符串或 `False`。
 - 变量保存的是对象引用，赋值操作不等于复制对象。
 - 常量通常使用全大写加下划线命名，Python 主要依靠命名约定表达常量意图。
 - 类型转换应明确数据来源和失败方式，外部输入通常需要先校验再转换。
 - 表达式应保持简单，复杂计算可以拆分为有意义的中间变量。

### 补充 3：常用算法思维

课件覆盖了基本条件和循环，参考书进一步整理了累加与累乘、求最大值和最小值、枚举法、递推与迭代等常用算法思路。

 - 累加和累乘适合处理逐项汇总的问题。
 - 最大值和最小值问题需要明确初始值和空序列边界。
 - 枚举法通过遍历候选解寻找满足条件的结果，重点是定义候选空间和终止条件。
 - 递推使用前一步或前几步结果得到下一步结果，迭代则强调重复更新状态。
 - 编写循环前先明确初始化、循环条件、状态变化和结束后的结果。

### 补充 4：函数进阶

课件已经介绍函数参数和模块导入，参考书还扩展了 Lambda 表达式、变量作用域、闭包和递归调用。

 - Lambda 适合表达短小、一次性的函数逻辑；复杂逻辑应使用具名函数。
 - 变量查找需要理解局部作用域、外部作用域和全局作用域，尽量减少隐式依赖。
 - 闭包可以保存外层函数的状态，但应避免让状态变化难以追踪。
 - 递归需要明确基准条件，否则会无限调用；能用简单循环表达时，优先考虑可读性和资源开销。

### 补充 5：文件与目录进阶

课件覆盖了基础文本文件读写，参考书进一步涉及文件内移动、二进制文件、当前工作目录、目录操作和文件操作。

 - 文件指针决定下一次读写的位置，随机访问时要明确 `seek` 和 `tell` 的语义。
 - 二进制文件应使用字节数据处理，不能直接假设其内容是文本。
 - 路径处理优先使用 `pathlib`，减少手写路径分隔符带来的跨平台问题。
 - 目录和文件操作应区分检查、创建、遍历、复制、移动和删除等动作。
 - 涉及删除或覆盖时，应先确认目标路径和操作范围。

### 补充 6：面向对象设计进阶

课件介绍了类、对象、继承和多态，参考书还进一步涉及析构函数、私有成员、公有成员、多继承和运算符重载。

 - 构造函数负责建立对象的有效初始状态。
 - 析构函数不应承担关键业务逻辑，因为对象销毁时机不适合作为可靠的资源管理机制。
 - 私有成员更多是封装约定和访问控制设计，重点是保护对象的不变量。
 - 多继承会增加方法解析和职责组合的复杂度，应有明确的设计理由。
 - 运算符重载应保持直观语义，让对象的行为符合使用者对该运算符的预期。

### 补充 7：GUI 编程基础

参考书第 7 章介绍 Tkinter 图形用户界面，而当前课件没有 GUI 内容。建议先理解 GUI 程序与命令行程序的差异：

 - GUI 程序由窗口、控件、布局和事件组成。
 - 控件负责展示或接收输入，事件处理函数负责响应用户操作。
 - 主事件循环负责持续接收和分发事件，阻塞式长任务会影响界面响应。
 - 布局设计应关注组件的层级、尺寸、间距和可用性。

本补充篇不提供 Tkinter 代码实现。

### 补充 8：多进程编程

课件介绍了多线程，参考书第 8 章还介绍多进程编程。理解重点包括：

 - 进程拥有相对独立的地址空间，线程通常共享同一进程的内存。
 - 多进程适合需要隔离资源或利用多核计算的场景，但进程创建和通信成本更高。
 - 进程间不能直接依赖普通变量共享状态，需要使用进程安全的通信或共享机制。
 - 线程和进程的选择应根据任务类型、共享状态、隔离要求和部署环境决定。

本补充篇不提供 `multiprocessing` 代码实现。

### 补充 9：数据库访问与 SQL

参考书第 9 章介绍数据库基础、关系型数据库、SQL 和 SQLite3，而当前课件没有数据库内容。建议掌握以下概念：

 - 数据库用于持久化管理结构化数据。
 - 表由字段和记录组成，主键用于唯一标识记录。
 - `SELECT` 用于查询，`INSERT` 用于新增，`UPDATE` 用于更新，`DELETE` 用于删除。
 - 参数化查询用于分离 SQL 结构和外部输入，避免把用户输入直接拼接到 SQL 字符串中。
 - 数据库操作应关注连接、事务、提交、回滚和关闭资源。

本补充篇不提供 SQLite 或 SQL 代码实现。

### 补充 10：图像处理

参考书第 10 章介绍 Pillow，包括图像读写、绘制文字和图形、滤镜、水印、验证码和二维码；当前课件没有图像处理内容。

 - 图像对象负责像素数据和基本属性。
 - 绘制模块负责在图像上添加文字、线条和形状。
 - 字体模块负责文字渲染，字体文件会影响跨平台显示效果。
 - 滤镜改变图像表现，水印和验证码属于典型的图像合成场景。
 - 二维码生成通常还需要额外的第三方依赖和明确的输出格式。

本补充篇不提供 Pillow 代码实现。

### 补充 11：网络编程

参考书第 11 章介绍网络基础、TCP/UDP、网络嗅探器、端口扫描器和网络爬虫，而当前课件没有网络编程内容。学习时应先建立边界意识：

 - TCP 面向连接，强调可靠、有序的字节流传输。
 - UDP 无连接，开销较小，但不保证送达和顺序。
 - 网络程序需要处理超时、断开、半包、编码、资源释放和异常。
 - 网络爬虫应遵守服务条款、访问频率限制、`robots.txt` 和数据隐私要求。
 - 嗅探和端口扫描涉及安全边界，只能在获得明确授权的环境中进行。

本补充篇不提供网络编程、嗅探器或端口扫描器代码实现。

## 参考资料

 - 参考书：[`Python编程入门与实践-清华大学.pdf`](课件/Python编程入门与实践-清华大学.pdf)
 - Python 官方文档：https://docs.python.org/zh-cn/
 - NumPy 官方文档：https://numpy.org/doc/

## 说明

本仓库中的案例用于学习和练习，内容经过简化，不能直接替代生产环境中的完整工程方案。涉及文件、线程、数据库、网络和第三方库时，应结合实际运行环境补充权限、日志、测试、超时和资源管理策略。
