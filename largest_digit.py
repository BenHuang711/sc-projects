"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(111))  # 1
    print(find_largest_digit(9453))  # 9


"""
demonstration for helper
"""


def find_largest_digit(n):
    return helper(abs(n), 0)
    # abs -> 取數值絕對值消除負號


def helper(num, max):
    # 判斷是否還有數值要分析，將數值/10,如果小於0表示是已經是最後一位數
    if num / 10 < 1:
        if num > max:
            max = num
            return max
        else:
            return max
    else:
        # 對數值取小數點後數值觀察是否大於最大值
        if num % 10 > max:
            # 數值大於目前最大值
            max = num % 10
            return helper(num // 10, max)
        else:
            return helper(num // 10, max)


def find_largest_digit2(n):
    """
	:param n: numbers
	:return: largest value
	"""
    largest_dig = 0  # largest_num被洗掉，需要用helper在解決這個問題。
    # 如果有負號，可以再傳number給helper時，先把數字轉成正的。
    # base case 是所有數字都跑完
    s = str(n)
    if len(s) == 0:
        return largest_dig
    # 只有一個數字的時候
    elif len(s) == 1:
        # 防止他是正負號
        if 9 >= int(s[0]) >= 0:
            if largest_dig < int(s[0]):
                largest_dig = int(s[0])
                return largest_dig
            else:
                return largest_dig
        else:
            return largest_dig
    else:
        # 只限數字能進來比較，防止正負號也被比較
        if 9 >= int(s[len(s) - 1]) >= 0:
            # 如果倒數第二個數字比最後一個數字小，最大的數值變成數第二個數字
            if largest_dig < int(s[len(s) - 1]):
                largest_dig = int(s[len(s) - 1])
                # recursion, 進入倒數第二個數字
                return find_largest_digit((s[:len(s) - 1])), largest_dig
            else:
                return find_largest_digit(s[:len(s) - 1])
        else:
            pass


if __name__ == '__main__':
    main()
