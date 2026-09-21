import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="School Student Ranking System",
    page_icon="🏆",
    layout="wide"
)


# ---------------- CSS ----------------

st.markdown("""
<style>

header{
    visibility:hidden;
}

.stApp{
    background:#0F172A;
    color:white;
}

.block-container{
    padding-top:1rem;
}


p,label,span{
    color:#E2E8F0;
}


.title{
    color:#38BDF8;
    text-align:center;
    font-size:42px;
    font-weight:800;
}


.sub{
    color:#CBD5E1;
    text-align:center;
    font-size:20px;
}


.metric{
    background:linear-gradient(135deg,#1E3A8A,#2563EB);
    padding:20px;
    border-radius:18px;
    color:white;
    text-align:center;
}


.metric h2{
    color:white;
}


h1,h2,h3{
    color:#38BDF8 !important;
}


.stButton button{
    background:#2563EB;
    color:white;
    border-radius:12px;
}


[data-testid="stMetricValue"]{
    color:#22C55E;
}


</style>

""", unsafe_allow_html=True)



# ---------------- GRADE FUNCTION ----------------

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"



# ---------------- LOAD DEFAULT FILE ----------------

df = pd.read_excel("Book1.xlsx")



# ---------------- CREATE PERCENTAGE ----------------

if "Percentage" not in df.columns:

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns


    marks_columns = [
        col for col in numeric_columns
        if col.lower() != "attendance"
    ]


    df["Percentage"] = (
        df[marks_columns]
        .mean(axis=1)
    )



# ---------------- NEW GRADE COLUMN ----------------

df["Grade"] = df["Percentage"].apply(
    calculate_grade
)



# ---------------- CREATE RANK ----------------

df = df.sort_values(
    "Percentage",
    ascending=False
)


df["Rank"] = range(
    1,
    len(df)+1
)



# ---------------- TITLE ----------------


st.markdown(
"""
<p class="title">
🏆 School Student Ranking System
</p>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<p class="sub">
Student Performance Analytics Dashboard
</p>
""",
unsafe_allow_html=True
)



st.write("---")



# ---------------- FILE UPLOAD ----------------


st.subheader("📂 Upload Student Excel File")


uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)



if uploaded_file:


    df = pd.read_excel(
        uploaded_file
    )


    # Percentage

    if "Percentage" not in df.columns:


        numeric_columns = df.select_dtypes(
            include="number"
        ).columns


        marks_columns = [
            col for col in numeric_columns
            if col.lower()!="attendance"
        ]


        df["Percentage"] = (
            df[marks_columns]
            .mean(axis=1)
        )



    # Grade

    df["Grade"] = df["Percentage"].apply(
        calculate_grade
    )


    # Rank

    df = df.sort_values(
        "Percentage",
        ascending=False
    )


    df["Rank"] = range(
        1,
        len(df)+1
    )



st.subheader("📊 Student Data")

st.dataframe(
    df,
    use_container_width=True
)



# ---------------- CARDS ----------------


st.write("---")

st.subheader(
    "📈 Performance Overview"
)


c1,c2,c3,c4 = st.columns(4)


with c1:

    st.metric(
        "Total Students",
        len(df)
    )


with c2:

    st.metric(
        "Average %",
        f"{round(df['Percentage'].mean(),2)}%"
    )


with c3:

    st.metric(
        "Highest %",
        f"{round(df['Percentage'].max(),2)}%"
    )


with c4:

    st.metric(
        "Top Student",
        df.iloc[0]["Name"]
    )



# ---------------- RANK TABLE ----------------


st.write("---")


st.subheader(
    "🏅 Student Ranking"
)


st.dataframe(
    df[
        [
            "Rank",
            "Student_ID",
            "Name",
            "Class",
            "Percentage",
            "Grade",
            "Attendance"
        ]
    ],
    use_container_width=True
)
)
