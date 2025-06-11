import streamlit as st

st.title("To-Do List ✅")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input to add new task
task = st.text_input("Enter your task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "done": False})
    else:
        st.warning("Please enter a task.")

# Display and manage tasks
for i in range(len(st.session_state.tasks)):
    item = st.session_state.tasks[i]
    col1, col2, col3 = st.columns([6, 1, 1])

    with col1:
        st.markdown(f"{'✔️ ' if item['done'] else ''}{item['task']}")

    with col2:
        if not item["done"] and st.button("✅", key=f"done{i}"):
            st.session_state.tasks[i]["done"] = True
            st.experimental_rerun()

    with col3:
        if st.button("🗑️", key=f"del{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
