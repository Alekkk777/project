# Core Pkgs
import streamlit as st 

# NLP
import neattext.functions as nfx 

# EDA 
import pandas as pd 

# Text Downloader
import base64 
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")

# Data Viz Pkgs
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud


def plot_wordcloud(my_text):
    my_wordcloud = WordCloud().generate(my_text)
    fig = plt.figure()
    plt.imshow(my_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)




# Load NLP Pkgs
import spacy
nlp = spacy.load('en_core_web_sm')



# Fxns
def text_analyzer(my_text):
	docx = nlp(my_text)
	allData = [(token.text,token.shape_,token.pos_,token.tag_,token.lemma_,token.is_alpha,token.is_stop) for token in docx]
	df = pd.DataFrame(allData,columns=['Token','Shape','PoS','Tag','Lemma','IsAlpha','Is_Stopword'])
	return df 	


def text_downloader(raw_text):
	b64 = base64.b64encode(raw_text.encode()).decode()
	new_filename = "clean_text_result_{}_.txt".format(timestr)
	st.markdown("### ** 📩 ⬇️ Download Cleaned Text file **")
	href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click here!</a>'
	st.markdown(href, unsafe_allow_html=True)


def make_downloadable(data):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "nlp_result_{}_.csv".format(timestr)
    st.markdown("### ** 📩 ⬇️ Download CSV file **")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click here!</a>'
    st.markdown(href, unsafe_allow_html=True)






def main():
	st.title("Text Cleaner App")

	menu = ["TextCleaner","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "TextCleaner":
		st.subheader("Text Cleaning")
		text_file = st.file_uploader("Upload Txt File",type=['txt'])
		normalize_case = st.sidebar.checkbox("Normalize Case")
		clean_stopwords = st.sidebar.checkbox("Stopwords")
		clean_punctuations = st.sidebar.checkbox("Punctuations")
		clean_emails = st.sidebar.checkbox("Emails")
		clean_special_char = st.sidebar.checkbox("Special Characters")
		clean_numbers = st.sidebar.checkbox("Numbers")
		clean_urls = st.sidebar.checkbox("URLS")


		if text_file is not None:
			file_details = {"Filename":text_file.name,"Filesize":text_file.size,"Filetype":text_file.type}
			st.write(file_details)

			# Decode Text
			raw_text = text_file.read().decode('utf-8')

			col1,col2 = st.beta_columns(2)

			with col1:
				with st.beta_expander("Original Text"):
					st.write(raw_text)



			with col2:
				with st.beta_expander("Processed Text"):
					if normalize_case:
						raw_text = raw_text.lower()

					if clean_stopwords:
						raw_text = nfx.remove_stopwords(raw_text)

					if clean_numbers:
						raw_text = nfx.remove_numbers(raw_text)

					if clean_urls:
						raw_text = nfx.remove_urls(raw_text)

					if clean_punctuations:
						raw_text = nfx.remove_punctuations(raw_text)

					st.write(raw_text)

					text_downloader(raw_text)


			with st.beta_expander("Text Analysis"):
				token_result_df = text_analyzer(raw_text)
				st.dataframe(token_result_df)
				make_downloadable(token_result_df)


			with st.beta_expander("Plot Wordcloud"):
				plot_wordcloud(raw_text)


			with st.beta_expander("Plot POS Tags"):
				fig = plt.figure()
				sns.countplot(token_result_df['PoS'])
				plt.xticks(rotation=45)
				st.pyplot(fig)
					






	else:
		st.subheader("About")






if __name__ == '__main__':
	main()
