"""
Day 87 — one dashboard.
========================
A dashboard answers a question someone asks REPEATEDLY.
If they would ask it once, write a report instead.

    streamlit run dashboard/app.py
"""
import pandas as pd
import streamlit as st

# =============================================================================
# 1 -- THE QUESTION. Fill this in before writing any widget.
# =============================================================================
#   THE QUESTION THIS ANSWERS:
#
#   WHO ASKS IT:
#
#   HOW OFTEN:
#       (if the answer is "once", build a report, not a dashboard)
# =============================================================================

st.set_page_config(page_title="<question>", layout="wide")
st.title("<The question, as the title>")


# 3 -- load and CACHE. Under three seconds, or pre-aggregate.
@st.cache_data
def load_data() -> pd.DataFrame:
    """Load Project 2's PROCESSED data. Never the raw CSVs -- too slow."""
    pass


df = load_data()

# 5 -- filters that MATTER. Two or three. Not eight.
#      WHICH FILTERS DOES THE USER ACTUALLY VARY?
with st.sidebar:
    st.header("Filters")
    # region = st.selectbox(...)
    # period = st.date_input(...)


# 4 -- THE HEADLINE ROW. Every tile needs a COMPARISON.
#      A number with no comparison is trivia.
col1, col2, col3, col4 = st.columns(4)
# col1.metric("Revenue", f"PKR {total:,.0f}", delta=f"{change:+.1%} vs last period")


# 6 -- THREE TO FIVE CHARTS. Not twelve.
#      Each one answers PART of the question.
#
#      chart 1 answers:
#      chart 2 answers:
#      chart 3 answers:
#
#      WHAT I LEFT OUT, AND WHY:
#      (if you left nothing out, you probably included too much --
#       a reviewer reads twelve charts as "did not know what mattered")


# 8 -- WHAT THIS DOES NOT SHOW. One line. The same honesty as a README.
st.caption("This does not show: ...")


# =============================================================================
# 7 -- THE LOAD-TIME CHECK.  Under 3 seconds.
#      measured: ____ s
#      WHAT I HAD TO DO TO GET THERE:
#
# 10 -- THE STRANGER TEST. Hand it over. SAY NOTHING. Watch.
#      Who I gave it to:
#      Where they hesitated:
#        1.
#        2.
#      Did they find the answer to my stated question WITHOUT HELP?  yes / no
#      WHAT I FIXED:
# =============================================================================
