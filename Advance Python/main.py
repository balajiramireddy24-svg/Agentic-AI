#University Management System using python and streamlit

import streamlit as st  #used for frontend development

#config the frontend of the app
st.set_page_config(
    page_title="University Management System",
    layout="wide",
)

st.title("University Management portal")  #title of the app


#creating a empty list of collges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

menu_choice = st.sidebar.radio(
    "SELECT ACTION",
    (
        "Creating College",
        "ADD Student",
        "ADD Teacher",
        "Display Student",
        "Display Teacher",
        "Display College List",
    )
)

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, s):
        self.students.append(s)

    def add_teacher(self, t):
        self.teachers.append(t)

#This function will find the college object from the college list
    def find_college(cname):
        return next((c for c in st.session_state.colleges if c.cname==cname ), None)

#creating new college
if menu_choice == "Creating College":
    cname = st.text_input("Enter College Name")
    if st.button("Create"):
        clg_obj = college(cname) #creating new college object
        st.session_state.colleges.append(clg_obj)  #storing college class object in the list
        st.success(f"College {cname} created successfully")  #success message

# Adding student to the college
elif menu_choice == "ADD Student":
    if not st.session_state.colleges:
        st.info("Please insert the college first")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])
        roll=st.text_input("Enter the Roll Number ")
        cname = st.text_input("Enter the Student Name ")
        branch=st.text_input("Enter the branch")
        if st.button("ADD STUDENT"):
            if not(clgname and roll and sname and branch):
                st.error("Please Enter all the above infromation ")
            else:
                clg=find_college(clgname)
                std_obj= student(roll,sname,branch)
                clg.add_student(std_obj)