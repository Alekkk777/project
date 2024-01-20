import streamlit as st
import pandas as pd  
from db_fxns import *

def run_home_page():
	st.subheader("Home")

	choice = st.sidebar.selectbox("SubMenu",["My Tasks","Search"])

	with st.expander("View All Task"):
		result = view_all_tasks()
		df = pd.DataFrame(result,columns=['Task Doer','Task','Tast Status','Task Due Date'])
		st.dataframe(df)

	if choice == "My Tasks":
		c1,c2 = st.columns([1,3])

		with c1:
			st.info("Task List")
			list_of_tasks = [i[0] for i in view_all_task_names()]
			selected_task = st.selectbox("Your Task",list_of_tasks)

		with c2:
			st.info("Details")
			task_result = get_task_by_task_name(selected_task)
			# st.write(task_result)
			task_doer = task_result[0][0]
			task_name = task_result[0][1]
			task_status = task_result[0][2]
			task_due_date = task_result[0][3]
			st.write("Task Doer:{}".format(task_doer))
			st.text("Task:{}".format(task_name))
			st.text("Task Status:{}".format(task_status))
			st.write("Task Due Date:{}".format(task_due_date))

	else:
		st.subheader("Search Task")
		search_term = st.text_input("Search Term")
		search_choice = st.radio("Field To Search",("Task Doer","Task Name"))
		if st.button("Search"):
			if search_choice == "Task Name":
				search_result = get_task_by_task_name(search_term)
				st.write(search_result)
			else:
				search_result = get_task_by_task_doer(search_term)
				st.write(search_result)





