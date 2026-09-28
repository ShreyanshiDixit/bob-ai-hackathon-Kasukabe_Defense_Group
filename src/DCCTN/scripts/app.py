from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="DCCTN",
    page_icon="🚔",
    layout="wide"
)

# ==================================================
# DATABASE
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "firs.db"

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query(
    "SELECT * FROM firs",
    conn
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🚔 DCCTN")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Repeat Offenders",
        "Search",
        "Correlation",
        "Cases",
        "Happenings",
        "Ask AI"
    ]
)

# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    st.title("🚔 DCCTN")
    st.caption("Digital Crime Correlation & Tracking Network")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total FIRs",
        len(df)
    )

    col2.metric(
        "Crime Types",
        df["crime_type"].nunique()
    )

    col3.metric(
        "Districts",
        df["district"].nunique()
    )

    col4.metric(
        "States",
        df["state"].nunique()
    )

    st.divider()

    st.subheader("Crime Type Distribution")

    crime_counts = (
        df["crime_type"]
        .value_counts()
        .reset_index()
    )

    crime_counts.columns = [
        "Crime Type",
        "Count"
    ]

    fig = px.bar(
        crime_counts,
        x="Crime Type",
        y="Count"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.subheader("District Distribution")

    district_counts = (
        df["district"]
        .value_counts()
        .reset_index()
    )

    district_counts.columns = [
        "District",
        "Count"
    ]

    fig2 = px.pie(
        district_counts,
        names="District",
        values="Count"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

# ==================================================
# REPEAT OFFENDERS
# ==================================================

elif page == "Repeat Offenders":

    st.title("👤 Repeat Offenders")

    if "accused_names" not in df.columns:

        st.warning(
            "accused_names column not found in database."
        )

    else:

        offenders = (
            df.groupby("accused_names")
            .size()
            .reset_index(name="Case Count")
            .sort_values(
                "Case Count",
                ascending=False
            )
        )

        offenders = offenders[
            offenders["Case Count"] > 1
        ]

        st.dataframe(
            offenders,
            width="stretch"
        )

# ==================================================
# SEARCH
# ==================================================

elif page == "Search":

    st.title("🔍 FIR Search")

    search_term = st.text_input(
        "Search FIR Number / Crime Type / District"
    )

    if search_term:

        filtered = df[
            df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search_term,
                    case=False,
                    na=False
                ).any(),
                axis=1
            )
        ]

        st.write(
            f"Results: {len(filtered)}"
        )

        st.dataframe(
            filtered,
            width="stretch"
        )

# ==================================================
# CORRELATION
# ==================================================

elif page == "Correlation":

    st.title("🔗 Case Correlation")

    st.info(
        "Future ChromaDB-powered semantic correlation module."
    )

    query = st.text_input(
        "Describe a crime pattern"
    )

    if query:

        st.success(
            "Future: Search ChromaDB for similar FIRs."
        )

# ==================================================
# CASES
# ==================================================

elif page == "Cases":

    st.title("📁 Cases")

    st.dataframe(
        df,
        width="stretch"
    )

# ==================================================
# HAPPENINGS
# ==================================================

elif page == "Happenings":

    st.title("📢 Recent Happenings")

    st.info(
        "Activity Feed"
    )

    latest = df.tail(20)

    st.dataframe(
        latest,
        width="stretch"
    )

# ==================================================
# ASK AI
# ==================================================

elif page == "Ask AI":

    st.title("🤖 Ask AI")

    st.info(
        "Qwen 3 8B + ChromaDB RAG module will be integrated here."
    )

    question = st.chat_input(
        "Ask a question..."
    )

    if question:

        st.chat_message("user").write(
            question
        )

        st.chat_message("assistant").write(
            "AI module not connected yet."
        )

# ==================================================
# CLOSE DB
# ==================================================

conn.close()