import streamlit as st
from db.ejdic import found_word


LIMIT = 10


def words_means(word):
    out = []
    for i in range(4):
        out.extend(list(found_word(word, i)))
        if len(out) > LIMIT + 20:
            break
    return out


def get_results(word):
    count = 0
    text_list = set()
    out = words_means(word)
    for text, mean in out:
        if text not in text_list:
            yield text, mean
            count += 1
            text_list.add(text)
            if count > LIMIT + 1:
                break


st.title("Minenohara Dic V2")
st.caption("英単語の意味と、入力された近い単語を出力")
word = st.text_input("Word")
search = st.button("Search")

if word:
    results = get_results(word)
    for text, mean in results:
        if word == text:
            st.subheader(text)
        else:
            st.subheader(text, help="Not exact match")
        st.write(mean)
        st.divider()
