from pandas_ods_reader import read_ods
from random import shuffle
import time

ods_path = "letterPairs.ods"
sheet_index = 1


def test_pairs():
    print("Hello, pro blind solver\n")
    pair_to_word = build_pair_to_word_map()
    pairs = list(pair_to_word.keys())
    shuffle(pairs)
    answer = '-'
    for pair in pairs:
        print("Answer = " + answer)
        print(pair + ' ?')
        answer = pair_to_word[pair]
        time.sleep(2)


def build_pair_to_word_map():
    df = read_ods(ods_path, sheet_index)
    matrix = df.values.tolist()
    first_char = ord('A')
    pair_to_word = {}
    for row in matrix:
        if not row[0] is None:
            second_char = ord('A')
            for word in row:
                if word is not None and len(word) > 1 and word != "empty":
                    pair_to_word[chr(first_char)+chr(second_char)] = word
                second_char += 1
            print("")
            first_char += 1
    return pair_to_word


if __name__ == '__main__':
    test_pairs()
