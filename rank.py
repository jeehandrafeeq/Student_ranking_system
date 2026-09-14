import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Page Configuration
st.set_page_config(
    page_title="School Student Ranking System",
    page_icon="🏆",
    layout="wide"
)


# CSS Styling
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

p,label,.stMarkdown{
    color:#E5E7EB;
    font-size:16px;
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
    font-size:32px;
}


h1,h2,h3{
    color:#38BDF8 !important;
}


.stButton>button{
    background:#2563EB;
    color:white;
    border-radius:12px;
    padding:10px 25px;
    font-weight:bold;
}


.stButton>button:hover{
    background:#38BDF8;
    color:#0F172A;
}

</style>
""", unsafe_allow_html=True)



# Load Excel Data
df = pd.read_excel("Book1.xlsx")


# Sort and Create Rank
df = df.sort_values(
    "Percentage",
    ascending=False
)

df["Rank"] = range(1,len(df)+1)



# Title
st.markdown(
    '<p class="title">🏆 School Student Ranking System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub">Dashboard</p>',
    unsafe_allow_html=True
)


st.write("---")


# Student Data Selection

st.subheader("📊 Student Data Selection")


columns = [
    "Rank",
    "Student_ID",
    "Name",
    "Class",
    "Percentage",
    "Grade",
    "Attendance"
]


selected_columns = st.multiselect(
    "Select information you want to display:",
    columns
)


if selected_columns:

    st.dataframe(
        df[selected_columns],
        use_container_width=True
    )

else:

    st.warning("Please select at least one option.")



# Dashboard Cards

st.write("---")

c1,c2,c3,c4 = st.columns(4)


with c1:

    st.markdown(f"""
    <div class="metric">
    <h2>{len(df)}</h2>
    Students
    </div>
    """,unsafe_allow_html=True)



with c2:

    st.markdown(f"""
    <div class="metric">
    <h2>{round(df["Percentage"].mean(),2)}%</h2>
    Average %
    </div>
    """,unsafe_allow_html=True)



with c3:

    st.markdown(f"""
    <div class="metric">
    <h2>{df.iloc[0]["Name"]}</h2>
    Top Student
    </div>
    """,unsafe_allow_html=True)



with c4:

    st.markdown(f"""
    <div class="metric">
    <h2>{df["Percentage"].max()}%</h2>
    Highest %
    </div>
    """,unsafe_allow_html=True)



# Charts

st.write("---")


left,right = st.columns(2)



with left:

    st.subheader("🏆 Top 10 Students")


    top = df.head(10)


    fig,ax = plt.subplots(figsize=(8,5))


    ax.bar(
        top["Name"],
        top["Percentage"]
    )


    plt.xticks(rotation=40)


    st.pyplot(fig)



with right:

    st.subheader("📊 Grade Distribution")


    grade = df["Grade"].value_counts()


    fig2,ax2 = plt.subplots(figsize=(6,5))


    ax2.pie(
        grade,
        labels=grade.index,
        autopct="%1.1f%%"
    )


    st.pyplot(fig2)



# Final Ranking Table

st.write("---")


st.subheader("🏅 Complete Ranking Table")


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