import streamlit as st
import pandas as pd

from utils import (
    load_data,
    get_total_matches,
    get_total_runs,
    get_total_wickets,
    get_total_teams,
)

from charts import (
    plot_matches_per_season,
    plot_top_teams,
    plot_top_batsmen,
    plot_top_bowlers,
    plot_toss_decision,
    plot_match_result,
)



st.set_page_config(
    page_title="IPL Analytics Dashboard",
    page_icon="🏏",
    layout="wide",
)



matches, deliveries = load_data()



st.sidebar.title("📊 Dashboard Filters")

season_list = sorted(matches["season"].dropna().unique())

selected_season = st.sidebar.selectbox(
    "Select Season",
    ["All"] + list(season_list)
)

teams = sorted(
    list(
        set(matches["team1"].dropna())
        |
        set(matches["team2"].dropna())
    )
)

selected_team = st.sidebar.selectbox(
    "Select Team",
    ["All"] + teams
)



filtered_matches = matches.copy()

if selected_season != "All":
    filtered_matches = filtered_matches[
        filtered_matches["season"] == selected_season
    ]

if selected_team != "All":
    filtered_matches = filtered_matches[
        (filtered_matches["team1"] == selected_team)
        |
        (filtered_matches["team2"] == selected_team)
    ]


st.title("🏏 IPL Analytics Dashboard")

st.subheader(
    "End-to-End Data Analytics Project (2008–2023)"
)


st.markdown("## 📈 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏏 Total Matches",
        get_total_matches(filtered_matches)
    )

with col2:
    st.metric(
        "👥 Teams",
        get_total_teams(filtered_matches)
    )

with col3:
    st.metric(
        "🏃 Total Runs",
        get_total_runs(deliveries)
    )

with col4:
    st.metric(
        "🎯 Total Wickets",
        get_total_wickets(deliveries)
    )

st.divider()

st.markdown("## 📊 Season Analysis")

plot_matches_per_season(filtered_matches)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏆 Top Winning Teams")
    plot_top_teams(filtered_matches)

with col2:
    st.markdown("### 🏏 Top Run Scorers")
    plot_top_batsmen(deliveries)

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 🎯 Top Wicket Takers")
    plot_top_bowlers(deliveries)

with col4:
    st.markdown("### 🪙 Toss Decision Analysis")
    plot_toss_decision(filtered_matches)

st.divider()

st.markdown("## 📈 Match Result Analysis")

plot_match_result(filtered_matches)

st.divider()


st.markdown("## 📋 Dataset Preview")

tab1, tab2 = st.tabs(["Matches Dataset", "Deliveries Dataset"])

with tab1:
    st.dataframe(filtered_matches.head(20), use_container_width=True)

with tab2:
    st.dataframe(deliveries.head(20), use_container_width=True)

st.divider()


st.markdown("## 📥 Download Dataset")

col1, col2 = st.columns(2)

with col1:
    csv_matches = filtered_matches.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Matches CSV",
        data=csv_matches,
        file_name="matches.csv",
        mime="text/csv",
    )

with col2:
    csv_deliveries = deliveries.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Deliveries CSV",
        data=csv_deliveries,
        file_name="deliveries.csv",
        mime="text/csv",
    )

st.divider()



st.markdown("## ℹ About This Project")

st.info(
    """
This IPL Analytics Dashboard is built using:

✅ Python

✅ Pandas

✅ Plotly

✅ Streamlit

✅ SQL

✅ Power BI

The project analyzes IPL data from 2008–2023
and provides interactive insights into team
performance, player statistics, bowling,
batting and match trends.
"""
)

st.divider()



st.markdown("---")

st.markdown(
    """
<div style='text-align:center;'>

### 🏏 IPL Analytics Dashboard

Developed by **Janvi Chauhan**

⭐ Python | SQL | Power BI | Streamlit

</div>
""",
unsafe_allow_html=True,
)