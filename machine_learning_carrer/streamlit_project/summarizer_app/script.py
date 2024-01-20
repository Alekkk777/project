import streamlit as st
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from rouge import Rouge
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Scegli un backend appropriato
import seaborn as sns
import altair as alt

# Scarica le risorse necessarie di NLTK (punkt e stopwords)
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

def evaluate_summary(summary, reference):
    r = Rouge()
    eval_score = r.get_scores(summary, reference)
    eval_score_df = pd.DataFrame(eval_score[0])
    return eval_score, eval_score_df

def sumy_summarizer(docx, num=2):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ''.join(summary_list)
    return result

def main():
    st.title("Summarizer App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter Text Here")
        processed_text = remove_stopwords(raw_text)

        if st.button("Summarizer"):
            with st.expander("Original text"):
                st.write(raw_text)

            # Layout
            c1, c2 = st.columns(2)

            with c1:
                with st.expander("Lex_rank"):
                    my_summary = sumy_summarizer(processed_text)
                    document_len = {"Original": len(processed_text), "Summary": len(my_summary)}
                    st.write(document_len)
                    st.write(my_summary)
                    st.info("Rouge Score")
                    eval_score, eval_df = evaluate_summary(my_summary, raw_text)
                    st.dataframe(eval_df)
                    eval_df['metrics'] = eval_df.index
                    c = alt.Chart(eval_df).mark_bar().encode(x='metrics', y='rouge-1')
                    st.altair_chart(c)

            with c2:
                with st.expander("Text_rank"):
                    my_summary = sumy_summarizer(processed_text)
                    document_len = {"Original": len(processed_text), "Summary": len(my_summary)}
                    st.write(document_len)
                    st.write(my_summary)
                    st.info("Rouge Score")
                    eval_score, eval_df = evaluate_summary(my_summary, raw_text)
                    st.dataframe(eval_df)
                    eval_df['metrics'] = eval_df.index
                    c = alt.Chart(eval_df).mark_bar().encode(x='metrics', y='rouge-1')
                    st.altair_chart(c)
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
