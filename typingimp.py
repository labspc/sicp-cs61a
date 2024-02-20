import random
import string
from datetime import datetime


def pick_paragraph_from_file(file_path):
    """
    从文件中随机选择一个段落。

    参数:
      file_path: 文件路径

    返回:
      一个随机选择的段落字符串
    """
    # with 语句提供了一种更加简洁和安全的方式来管理资源
    # 'r'代表只读模式
    with open('sample_paragraphs.txt', 'r') as file:
        paragraphs = file.readlines()
    # random.choice函数
    return random.choice(paragraphs)


def generate_random_paragraph():
    """
    生成一个随机段落。

    返回:
      一个随机生成的段落字符串
    """
    paragraph = ' '.join(''.join(random.choices(string.ascii_letters + string.punctuation, k=random.randint(5, 15)))
                         for _ in range(random.randint(3, 5)))
    return paragraph


def calculate_accuracy(typed, source):
    """
    计算打字准确率。

    参数:
      typed: 输入的文本
      source: 原始文本

    返回:
      准确率百分比
    """
    typed_words = typed.split()
    source_words = source.split()
    correct_words = sum(1 for tw, sw in zip(typed_words, source_words) if tw.lower() == sw.lower())
    return round(correct_words / len(source_words) * 100, 2)


def calculate_wpm(typed, elapsed_time):
    """
    计算打字速度 (每分钟字数)。

    参数:
      typed: 输入的文本
      elapsed_time: 花费的时间 (秒)

    返回:
      每分钟字数
    """
    return round(len(typed.split()) / elapsed_time * 60, 2)


def run_test(topic):
    """
    运行打字测试。

    参数:
      topic: 主题单词
    """
    try:
        paragraph = pick_paragraph_from_file("paragraphs.txt")
    except FileNotFoundError:
        print("段落文件未找到。")
        return

    print(f"\n主题: {topic.upper()}")
    print(paragraph)
    start_time = datetime.now()
    typed_text = input("\n请键入以上段落并按回车键: ")
    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    accuracy = calculate_accuracy(typed_text, paragraph)
    wpm = calculate_wpm(typed_text, elapsed_time)
    print(f"\n准确率: {accuracy:.2f}%")
    print(f"每分钟字数: {wpm:.2f}")


if __name__ == "__main__":
    topic = input("请输入一个主题单词: ")
    run_test(topic)
