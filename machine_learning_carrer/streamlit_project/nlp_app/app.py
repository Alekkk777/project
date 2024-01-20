import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
# NLP Pkgs
import spacy
from spacy import displacy
from textblob import TextBlob
# Text cleaning Pkgs
import neattext as nt
import neattext.functions as nfx
# Utils
from collections import Counter
import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
# Data visualize
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud
# File processing 
import docx2txt
from PyPDF2 import PdfFileReader
import pdfplumber

# Modifica questa riga
nlp = spacy.load('en_core_web_sm')

HTML_WRAPPER = """<div style="overflow-x: auto;border:1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">
                    <div class="entities" style="line-height: 2.5; direction: ltr">
                        <mark class="entity" style="background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
                            John <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">PERSON</span>
                        </mark> 
                        was going to 
                        <mark class="entity" style="background:#feca74; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
                            London <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">GPE</span>
                        </mark> 
                        to work at 
                        <mark class="entity" style="background: #7aecec; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
                            Streamlit.org <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">ORG</span>
                        </mark>
                    </div>
                </div>"""

def text_analyzer(my_text):
    docx = nlp(my_text)
    allData = [(token.text, token.shape_, token.pos_, token.tag_, token.lemma_, token.is_alpha, token.is_stop) for token in docx]
    df = pd.DataFrame(allData, columns=['Token', 'Shape', 'PoS', 'Tag', 'Lemma', 'IsAlpha', 'Is_Stopword'])
    return df

def render_entities(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style="ent")
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)
    return result

def get_most_common_tokens(my_text,num=5):
    word_tokens=Counter(my_text.split())
    most_common_tokens=dict(word_tokens.most_common(num))
    return most_common_tokens

def get_sentiment(my_text):
    blob=TextBlob(my_text)
    sentiment= blob.sentiment
    return sentiment

def plot_wordcloud(my_text):
    my_wordcloud = WordCloud().generate(my_text)
    fig=plt.figure()
    plt.imshow(my_wordcloud,interpolation='bilinear')
    st.pyplot(fig)

def make_downloadable(data):
    csvfile=data.to_csv(index=False)
    b64=base64.b64encode(csvfile.encode()).decode()
    new_filename='nlp_result_{}_.csv'.format(timestr)
    st.markdown('###** Download CSV file **')
    href=f'<a href="data:file/csv;based64,{b64}" download="{new_filename}">Click here</a>'
    st.markdown(href,unsafe_allow_html=True)

def read_pdf(file):
    pdfReader =PdfFileReader(file)
    count=pdfReader.numPages
    all_page_text=""
    for i in range(count):
        page=pdfReader.getPage(i)
        all_page_text==page.extractText()
    return all_page_text

def read_pdf2(file):
    with pdfplumber.open(file) as pdf:
        page=pdf.pages[0]
        return page.extract_text()

def main():
    st.title("NLP App")
    menu = ["Home", "NLP_file", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home: Analyze text")
        raw_text = st.text_area("Enter Text Here")
        num_of_most_common = st.sidebar.number_input("Most Common Tokens", 5, 15)

        if st.button("Analyze"):
            with st.expander("Original text"):
                st.write(raw_text)
            with st.expander("Text Analysis"):
                token_result_df = text_analyzer(raw_text)
                st.dataframe(token_result_df)
            with st.expander("Entities"):
                #entity_result=get_entities(raw_text)
                #st.write(entity_result)
                entity_result=render_entities(raw_text)
                stc.html(entity_result,height=1000,scrolling=True)

            c1, c2 = st.columns(2)
            with c1:
                with st.expander("Word Stats"):
                    st.info("Word Statistics")
                    docx=nt.TextFrame(raw_text)
                    st.write(docx.word_stats())

                with st.expander("Top Keywords"):
                    st.info("Top Keywords/Tokens")
                    processed_text=nfx.remove_stopwords(raw_text)
                    keywords=get_most_common_tokens(processed_text,num_of_most_common)
                    st.write(keywords)

                with st.expander("Sentiment"):
                    sent_result=get_sentiment(raw_text)
                    st.write(sent_result)
            with c2:
                with st.expander("Plot Word Freq"):
                    fig=plt.figure()
                    top_keywords=get_most_common_tokens(processed_text,num_of_most_common)
                    plt.bar(keywords.keys(),top_keywords.values())
                    st.pyplot(fig)

                with st.expander("Plot Part of Speech"):
                    try:
                        fig=plt.figure()
                        sns.countplot(token_result_df['PoS'])
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
                    except:
                        st.warning("insufficient Data")

                with st.expander("Plot Wordcloud"):
                    plot_wordcloud(raw_text)
            with st.expander("Download Text Analysis Results"):
                make_downloadable(token_result_df)

    elif choice == "NLP_file":
        st.subheader("NLP task")
        text_file=st.file_uploader("Upload Files",type=['pdf','docx','txt'])
        num_of_most_common = st.sidebar.number_input("Most Common Tokens", 5, 15)
        if text_file is not None:
            if text_file.type == 'application/pdf':
                raw_text=read_pdf(text_file)
                st.write(raw_text)
            elif text_file.type=='text/plain':
                raw_text=str(text_file.read(),"utf-8")
                st.write(raw_text)
            else:
                raw_text=docx2txt.process(text_file)
                st.write(raw_text)


    else:
        st.subheader("About")
        st.write("Information about the app goes here.")

if __name__ == '__main__':
    main()
