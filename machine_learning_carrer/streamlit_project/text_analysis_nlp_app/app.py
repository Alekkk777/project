import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
#NLP Pkgs
import neattext.functions as nfx
from wordcloud import WordCloud
from collections import Counter
from textblob import TextBlob
#Data visualizzation Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt


def get_pos_tags (docx):
    blob = TextBlob (docx)
    tagged_docx = blob.tags
    tagged_df = pd.DataFrame(tagged_docx, columns=[ 'token', 'tags' ])
    return tagged_df

def plot_mendelhall_curve(docx) :
    word_length = [ len (token) for token in docx.split()]
    word_length_count = Counter (word_length)
    sorted_word_length_count = sorted (dict(word_length_count).items())
    x, y = zip(*sorted_word_length_count)
    mendelhall_df = pd.DataFrame ({'tokens':x,'counts': y})
    st.line_chart(mendelhall_df[ 'counts'])

TAGS={
    'NN':'green',
    'NNS':'green',
    'NNP':'green',
    'NNPS':'green',
    'VB':'blue',
    'VBD':'blue',
    'VBG':'blue',
    'VBN':'blue',
    'VBP':'blue',
    'VBZ':'blue',
    'JJ':'red',
    'JJR':'red',
    'JJS':'red',
    'RB':'cyan',
    'RBR':'cyan',
    'RBS':'cyan',
    'IN':'darkwhite',
    'POS':'darkyellow',
    'PRP$':'magenta',
    
}

def mytag_visualizer(tagged_docx) :
    colored_text = []
    for i in tagged_docx:
        if i[1] in TAGS.keys():
            token = i[0]
            color_for_tag = TAGS.get(i[1])
            result = '<span style="color:{}">{}</span>'.format(color_for_tag,token)
            colored_text.append(result)
    result = ''.join(colored_text)
    print (result)
    return result

def plot_wordcloud(docx):
    if docx.strip():  # Verifica se ci sono parole nel testo
        mywordcloud = WordCloud().generate(docx)
        fig = plt.figure(figsize=(20,10))
        plt.imshow(mywordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()
    else:
        st.warning("Il testo è vuoto. Inserisci almeno una parola per generare una nuvola di parole.")


def plot_word_freq (docx, num=10) :
    word_freq = Counter(docx.split())
    most_common_tokens = word_freq.most_common(num)
    x,y = zip(*most_common_tokens)
    fig = plt.figure(figsize=(20,10))
    plt.bar(x,y)
    plt.xticks(rotation=45)
    plt.show()
    st.pyplot(fig)

def plot_word_freq_with_altair(docx, num=10):
    word_freq = Counter(docx.split())
    most_common_tokens = dict(word_freq.most_common(num))
    word_freq_df = pd.DataFrame({'tokens': most_common_tokens.keys(), 'counts': most_common_tokens.values()})
    brush = alt.selection(type='interval', encodings=['x'])
    c = alt.Chart(word_freq_df).mark_bar().encode(
        x="tokens",
        y="counts",
        opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7)),
    ).add_selection(brush)


    st.altair_chart(c,use_container_width=True)

def main():
    st.title("Text Analysis App")
    menu=["Home","About"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        raw_text= st.text_area("Enter Text Here")
        if st.button("Submit"):
            if len(raw_text)>2:
                st.success("Processing")
            elif len(raw_text)==1:
                st.Warning("Insufficient Text,minimum is 2")
            else:
                st.write("Enter Text")
        col1,col2=st.columns(2)
        processed_text=nfx.remove_stopwords(raw_text)
        with col1:
            with st.expander("Original Text"):
                st.write(raw_text)
            with st.expander("PoS Tagged Text"):
                tagged_docx=TextBlob(raw_text).tags
                processed_tags=mytag_visualizer(tagged_docx)
                stc.html(processed_tags,scrolling=True)
            with st.expander("Plot Word Freq"):
                plot_word_freq_with_altair(processed_tags)

        with col2:
            with st.expander("Processed Text"):
                st.write(processed_text)
            with st.expander("Plot Wordcloud"):
                st.success("Wordcloud")
                plot_wordcloud(processed_text) 
            with st.expander("Plot Stilometry Curve"):
                st.success("Mendelhall Curve")
                plot_mendelhall_curve(raw_text)   


    else:
        st.subheader("About")

if __name__ == "__main__":
    main()








