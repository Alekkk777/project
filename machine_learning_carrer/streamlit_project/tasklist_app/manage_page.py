import streamlit as st 
from db_fxns import (
	create_table,add_data,view_all_tasks,view_all_task_names,
	get_task_by_task_name,edit_task_data,delete_data)

import pandas as pd 
import plotly.express as px 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')


def run_manage_page():
	submenu = ["Delete Task","Analytics"]
	choice = st.sidebar.selectbox("SubMenu",submenu)


	if choice == "Delete Task":
		result = view_all_tasks()
		df = pd.DataFrame(result,columns=['Task Doer','Task','Tast Status','Task Due Date'])
		st.dataframe(df)
		unique_list = [i[0] for i in view_all_task_names()]
		delete_by_task_name = st.selectbox("Task to Delete",unique_list)
		st.warning("Deleting {}".format(delete_by_task_name))
		if st.button("Delete"):
			delete_data(delete_by_task_name)
			st.info("Deleted {}".format(delete_by_task_name))

		with st.expander("Current Database"):
			result2 = view_all_tasks()
			new_df = pd.DataFrame(result2,columns=['Task Doer','Task','Tast Status','Task Due Date'])
			st.dataframe(new_df)

		

	else:
		st.subheader("Analytics")
		result = view_all_tasks()
		df = pd.DataFrame(result,columns=['Task Doer','Task','Tast Status','Task Due Date'])

		with st.expander("View All Task"):
			st.dataframe(df)

		with st.expander("Task Doer Stats"):
			st.dataframe(df['Task Doer'].value_counts())
			new_df = df['Task Doer'].value_counts().to_frame()
			new_df = new_df.reset_index()
			st.dataframe(new_df)

			p1 = px.pie(new_df,names='index',values='Task Doer')
			st.plotly_chart(p1)	

		with st.expander("Task Stats"):
			# st.dataframe(df['Task'].value_counts())
			task_df = df['Task'].value_counts().to_frame()
			task_df = task_df.reset_index()
			st.dataframe(task_df)

			p2 = px.pie(task_df,names='index',values='Task')
			st.plotly_chart(p2)	
