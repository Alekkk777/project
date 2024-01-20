import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()

# Table
# Table must have field/columns
# Field must datatype

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(task_doer TEXT,task_name TEXT,task_status TEXT,task_due_date DATE)')

def add_data(task_doer,task_name,task_status,task_due_date):
	c.execute('INSERT INTO taskstable(task_doer,task_name,task_status,task_due_date) VALUES (?,?,?,?)',(task_doer,task_name,task_status,task_due_date))
	conn.commit()

def view_all_tasks():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data 

def view_all_task_names():
	c.execute('SELECT DISTINCT task_name FROM taskstable')
	data = c.fetchall()
	return data 

def get_task_by_task_name(task_name):
	c.execute('SELECT * FROM taskstable WHERE task_name ="{}"'.format(task_name))
	data = c.fetchall()
	return data

def get_task_by_task_doer(task_doer):
	c.execute('SELECT * FROM taskstable WHERE task_doer ="{}"'.format(task_doer))
	data = c.fetchall()
	return data

def edit_task_data(new_task_doer,new_task_name,new_task_status,new_task_due_date,task_doer,task_name,task_status,task_due_date):
	c.execute("UPDATE taskstable SET task_doer =?,task_name =?,task_status=?,task_due_date=? WHERE task_doer=? and task_name=? and task_status=? and task_due_date=?",(new_task_doer,new_task_name,new_task_status,new_task_due_date,task_doer,task_name,task_status,task_due_date))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task_name):
	c.execute('DELETE FROM taskstable WHERE task_name="{}"'.format(task_name))
	# c.execute('DELETE FROM taskstable WHERE task_name=?',(task_name))
	conn.commit()




