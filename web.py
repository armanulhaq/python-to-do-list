import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    #creates a dictionary with "new_todo" as key and the item
    #you enter as value
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos('todos.txt')

st.title("My To-Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add new todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
