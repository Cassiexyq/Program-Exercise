"""
判断一个数是否能够被2，3，5相乘的数组成
"""


def check_ci(input, amazing):  # 自己写的
    ci = 1
    while(1):
        if input % (pow(amazing, ci)) != 0:
            ci = ci-1
            break
        else:
            ci = ci + 1
    return ci


def get_simple_factors(n):  # 参考答案
    simple_words = [2,3,5]

    if n in simple_words: return [n]

    for s in simple_words:
        if not n % s and get_simple_factors(n / s):
            return [s] + get_simple_factors(n / s)
    return None


if __name__ == '__main__':
    # input = int(input())

    print(get_simple_factors(4))

    # two = check_ci(input,2)
    # three = check_ci(input,3)
    # five = check_ci(input,5)
    # # print(two,three,five)
    # if pow(2, two) * pow(3, three) * pow(5, five) == input:
    #     str = "2"*two+"3"*three+"5"*five
    #     print("("+",".join(str)+")")
    #
    # else:
    #     print("None")