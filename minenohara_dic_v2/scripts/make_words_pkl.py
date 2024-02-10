import os
import sqlite3
import pickle
from pathlib import Path


dataset_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
conn = sqlite3.connect(dataset_dir / "db/ejdict.sqlite3")


def make_sorted_words():
    c = conn.cursor()
    # sql = '''SELECT * FROM items WHERE level > 0 ORDER BY word'''
    sql = """SELECT * FROM items ORDER BY word"""
    rows = c.execute(sql)
    return sorted((r[1], r[2]) for r in rows)


def make_pkl():
    dic_words = make_sorted_words()
    words = [w for w, m in dic_words]
    means = [m for w, m in dic_words]
    pkl_fileneme = dataset_dir / "db/ejdict.pkl"
    with open(pkl_fileneme, 'wb') as f:
        pickle.dump((words, means), f)


if __name__ == "__main__":
    """Make pkl from sqlite3 for app data"""
    make_pkl()
