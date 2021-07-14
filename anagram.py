"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
final_lst = []
current_lst = []
current_w = ''
dic = []


def main():
    print('Welcome to stanCode "Anagram Generator"' + " (or -1 to quit)")
    input_word = input("Find anagrams for: ")
    # 讀取字典可以單一function執行，這樣decomposition比較恰當
    read_dictionary()
    while input_word != EXIT:
        # read_dictionary(input_word)
        find_anagrams(input_word, [])
        print(str(len(final_lst)) + ' anagrams:    ' + str(final_lst))
        input_word = input("Find anagrams for: ")


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            #去除換行字元
            word = line.strip()
            dic.append(word)


def find_anagrams(s, current_lst):
    """
    :param current_lst: list,
    :param s: str, targeted word for anagrams
    :return: list of anagrams
    為了避免重複字母出現，使用index去執行排序。
    """
    # 把index轉成英文單字
    target = ''
    for i in current_lst:
        target += s[i]
    # 先檢查開頭字有沒有在字典
    if has_prefix(target):
        if len(target) == len(s):
            # 檢查字典與答案欄
            if target in dic and target not in final_lst:
                print('Searching...')
                final_lst.append(target)
                print('Found:  ' + target)
                # final_lst.append(current_lst)
                # print('Found:  ' + str(current_lst))
        else:
            # 會有重複字母問題，所以要用index去尋找與排序
            for i in range(len(s)):
                if i not in current_lst:
                    # choose
                    current_lst.append(i)
                    # explore
                    find_anagrams(s, current_lst)
                    # unchoose
                    current_lst.pop()


            # for char in s:
            #     if char in current_lst:
            #         pass
            #     else:
            #         current_lst.append(char)
            #         find_anagrams(s, current_word, current_lst)
            #         current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, word that we can look up in the dic
    :return: bool, see if the recursion goes on
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
        # 這邊不能寫else，不然一但檢查到某一個字不是target的開頭時，就會return False
        # 應該要檢查完全部字典中的字，都沒 有target開頭的話，再 return False
        # else:
        #     return False
    return False



if __name__ == '__main__':
    main()
