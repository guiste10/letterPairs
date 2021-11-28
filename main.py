from pandas_ods_reader import read_ods
from random import shuffle
import time

SLEEPING_TIME_SEC = 2

ODS_PATH = "letterPairs.ods"
SHEET_INDEX = 1


def print_pairs_ordered():
    for first_char in range(ord('A'), ord('V') + 1):
        for second_char in range(ord('A'), ord('V') + 1):
            if first_char != second_char:
                print(chr(second_char) + chr(first_char))
                time.sleep(SLEEPING_TIME_SEC)


def test_pairs():
    pair_to_word = build_pair_to_word_map()
    pairs = list(pair_to_word.keys())
    shuffle(pairs)
    answer = '-'
    for pair in pairs:
        print("Answer = " + answer)
        print(pair + ' ?')
        answer = pair_to_word[pair]
        time.sleep(SLEEPING_TIME_SEC)


def build_pair_to_word_map():
    df = read_ods(ODS_PATH, SHEET_INDEX)
    matrix = df.values.tolist()
    first_char = ord('A')
    pair_to_word = {}
    for row in matrix:
        if not row[0] is None:
            second_char = ord('A')
            for word in row:
                if word is not None and len(word) > 1 and word != "empty":
                    pair_to_word[chr(first_char) + chr(second_char)] = word
                second_char += 1
            print("")
            first_char += 1
    return pair_to_word


if __name__ == '__main__':
    # print_pairs_ordered()
    test_pairs()
