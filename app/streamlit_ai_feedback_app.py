import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
file_1 = "data/AI_Tools_User_Feedback_Responses.xlsx"
file_2 = "data/AI_User_Behavior_Responses.xlsx"
file_3 = "data/AI_Merged_User_Feedback_Responses.xlsx"

# Function to load datasets safely
def load_data(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
        return None

df_1 = load_data(file_1)
df_2 = load_data(file_2)
df_3 = load_data(file_3)

# Sidebar Navigation
st.sidebar.title("📊 AI User Feedback Analysis")
tab = st.sidebar.radio(
    "Select Dataset",
    ["AI Tools User Feedback", "AI User Behavior", "AI Merged User Feedback"]
)

# Function to plot bar charts safely
def plot_bar_chart(df, column, title):
    if df is not None and column in df.columns:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.countplot(y=df[column], order=df[column].value_counts().index, palette="coolwarm", ax=ax)
        ax.set_title(title)
        ax.set_xlabel("Count")
        st.pyplot(fig)
    else:
        st.warning(f"Column '{column}' not found in the dataset.")

# Function to generate correlation heatmap
def plot_correlation_heatmap(df):
    if df is not None:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Feature Correlation Heatmap")
        st.pyplot(fig)

# Dataset 1: AI Tools User Feedback Analysis
if tab == "AI Tools User Feedback" and df_1 is not None:
    st.title("AI Tools User Feedback Analysis")
    st.write("### 📌 Available Columns in Dataset:")
    st.write(df_1.columns.tolist())

    st.subheader("📌 Data Preview")
    st.dataframe(df_1.head())

    st.subheader("📌 Age Group Distribution")
    plot_bar_chart(df_1, "Age Group", "Distribution of Age Groups")

    st.subheader("📌 Professions of Users")
    plot_bar_chart(df_1, "Profession/Industry", "Distribution of Professions")

    st.subheader("📌 AI Usage Rate")
    plot_bar_chart(df_1, "AI Tools Used", "Most Used AI Tools")

    st.subheader("📌 Satisfaction Level")
    if "Overall AI Satisfaction (Scale 1-10)" in df_1.columns:
        fig, ax = plt.subplots()
        df_1["Overall AI Satisfaction (Scale 1-10)"].value_counts().sort_index().plot(kind="bar", ax=ax)
        ax.set_title("AI Satisfaction Level")
        ax.set_xlabel("Satisfaction Score")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.warning("Column 'Overall AI Satisfaction (Scale 1-10)' not found.")

    st.subheader("📌 Feature Correlation Heatmap")
    plot_correlation_heatmap(df_1)

# Dataset 2: AI User Behavior Analysis
elif tab == "AI User Behavior" and df_2 is not None:
    st.title("AI User Behavior Analysis")
    st.write("### 📌 Available Columns in Dataset:")
    st.write(df_2.columns.tolist())

    st.subheader("📌 Data Preview")
    st.dataframe(df_2.head())

    st.subheader("📌 Occupation Distribution")
    plot_bar_chart(df_2, "Occupation", "Occupations of AI Users")

    st.subheader("📌 AI Usage Frequency")
    plot_bar_chart(df_2, "AI Usage Frequency", "How Often Users Use AI")

    st.subheader("📌 Trust in AI")
    if "Trust in AI (Scale 1-10)" in df_2.columns:
        fig, ax = plt.subplots()
        df_2["Trust in AI (Scale 1-10)"].value_counts().sort_index().plot(kind="bar", ax=ax)
        ax.set_title("Trust in AI")
        ax.set_xlabel("Trust Score")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.warning("Column 'Trust in AI (Scale 1-10)' not found.")

    st.subheader("📌 Feature Correlation Heatmap")
    plot_correlation_heatmap(df_2)

# Dataset 3: AI Merged User Feedback Analysis
elif tab == "AI Merged User Feedback" and df_3 is not None:
    st.title("AI Merged User Feedback Analysis")
    st.write("### 📌 Available Columns in Dataset:")
    st.write(df_3.columns.tolist())

    st.subheader("📌 Data Preview")
    st.dataframe(df_3.head())

    st.subheader("📌 AI Tools Used by Users")
    plot_bar_chart(df_3, "AI Tools Used", "Most Commonly Used AI Tools")

    st.subheader("📌 Challenges in AI Usage")
    plot_bar_chart(df_3, "Challenges in AI Usage", "Common AI Challenges")

    st.subheader("📌 AI Necessity in Workflows")
    plot_bar_chart(df_3, "AI Necessity", "How Users View AI as Necessary")

    st.subheader("📌 Feature Correlation Heatmap")
    plot_correlation_heatmap(df_3)

st.sidebar.info("Developed for AI Tools Matchmaking Analysis.")
