# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd 

# Utils
import base64
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")


# Fake Data Generation
from faker import Faker 

def generate_locale_profile(number,locale,random_seed=200):
	locale_fake = Faker(locale)
	data = [locale_fake.simple_profile() for i in range(number)]
	df = pd.DataFrame(data)
	return df


# Function to Download Data

def make_downloadable_df_format(data,format_type="csv"):
	if format_type == "json":
		datafile = data.to_json()
	else:
		datafile = data.to_csv(index=False)
	

	b64 = base64.b64encode(datafile.encode()).decode()  # B64 encoding
	st.markdown("###  Download File  ### ")
	new_filename = "fake_dataset_{}.{}".format(timestr,format_type)
	href = f'<a href="data:file/{format_type};base64,{b64}" download="{new_filename}">Click Here!</a>'
	st.markdown(href, unsafe_allow_html=True)


custom_title = """
<div style="font-size:40px;font-weight:bolder;background-color:#fff;padding:10px;
border-radius:10px;border:5px solid #464e5f;text-align:center;">
		<span style='color:blue'>F</span>
		<span style='color:black'>a</span>
		<span style='color:black'>k</span>
		<span style='color:black'>e</span>
		<span style='color:green'>-</span>
		<span style='color:black'>D</span>
		<span style='color:blue'>a</span>
		<span style='color:blue'>T</span>
		<span style='color:blue'>a</span>
		<span style='color:#464e5f'>G</span>
		<span style='color:red'>e</span>
		<span style='color:green'>n</span>
		<span style='color:yellow'>e</span>
		<span style='color:black'>r</span>
		<span style='color:blue'>a</span>
		<span style='color:green'>t</span>
		<span style='color:yellow'>o</span>
		<span style='color:black'>r</span>
		
</div>
"""

def main():
	# st.title("Fake Data Generator")
	stc.html(custom_title)

	menu = ["Home","Customize","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Simple Profile Generator")
		num_to_gen = st.sidebar.number_input("Number",10,5000)
		locale_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
		locale = st.sidebar.multiselect("Locale",locale_providers,default='en_US')
		dataformat = st.sidebar.selectbox("Save As ",["csv","json"])

		df = generate_locale_profile(num_to_gen,locale)
		st.dataframe(df)
		with st.expander("Download File"):
			make_downloadable_df_format(df,dataformat)


	elif choice == "Customize":
		st.subheader("Select Custom Fields")
		num_to_gen = st.sidebar.number_input("Number",10,5000)
		locale_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
		locale = st.sidebar.multiselect("Locale",locale_providers,default='en_US')
		dataformat = st.sidebar.selectbox("Save As ",["csv","json"])

		profile_options_list = ['username', 'name', 'sex' , 'address', 'mail' , 'birthdate','job', 'company', 'ssn', 'residence', 'current_location', 'blood_group', 'website'] 
		profile_fields = st.sidebar.multiselect("Fields",profile_options_list,default='username')
		custom_fake = Faker(locale)

		data = [custom_fake.profile(fields=profile_fields) for i in range(num_to_gen)]
		df = pd.DataFrame(data)
		st.dataframe(df)

		with st.expander("View As JSON"):
			for i in range(num_to_gen):
				st.write(custom_fake.profile(fields=profile_fields))

		with st.expander("Download File"):
			make_downloadable_df_format(df,dataformat)


	




	else:
		st.subheader("About")


if __name__ == '__main__':
	main()

