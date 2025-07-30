import streamlit as st
import pandas as pd

st.set_page_config(page_title="EEG Viewer", layout="wide")
st.title("🧠 EEG Data Viewer")

# Upload EEG CSV file
file = st.file_uploader("Upload EEG file (.csv)", type=["csv"])

if file is not None:
    st.success("✅ File received")

    try:
        # Load EEG data
        df = pd.read_csv(file)
        st.success("✅ File read successfully")
        st.write("📊 Columns detected:", df.columns.tolist())
        st.dataframe(df.head())

        # Plot EEG channel
        if len(df.columns) > 1:
            selected_column = st.selectbox("Choose a channel to plot", df.columns[1:])
            st.line_chart(df[selected_column])
        else:
            st.warning("⚠️ The CSV file doesn't have enough columns to plot EEG data.")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("📥 Please upload a .csv file containing EEG data.")
