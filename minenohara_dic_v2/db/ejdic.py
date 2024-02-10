import os
import pickle
from pathlib import Path
from db.automata import Matcher, find_all_matches


dataset_dir = Path(os.path.dirname(os.path.abspath(__file__)))


with open(dataset_dir / 'ejdict.pkl', 'rb') as f:
    words, means = pickle.load(f)


def found_word(word, k):
    m = Matcher(words, means)
    return find_all_matches(word, k, m)


if __name__ == "__main__":
    print(len(dic_words))
    print(dic_words)
