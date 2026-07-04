import streamlit as st
import plotly.express as px


def plot_matches_per_season(matches):
    season_data = (
        matches.groupby("season")
        .size()
        .reset_index(name="Matches")
    )

    fig = px.bar(
        season_data,
        x="season",
        y="Matches",
        color="Matches",
        title="Matches Played Per Season"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_top_teams(matches):
    teams = (
        matches["winner"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    teams.columns = ["Team", "Wins"]

    fig = px.bar(
        teams,
        x="Wins",
        y="Team",
        orientation="h",
        color="Wins",
        title="Top 10 Successful Teams"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_top_batsmen(deliveries):
    batsmen = (
        deliveries.groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        batsmen,
        x="batter",
        y="batsman_runs",
        color="batsman_runs",
        title="Top 10 Run Scorers"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_top_bowlers(deliveries):
    wickets = deliveries[deliveries["is_wicket"] == 1]

    bowlers = (
        wickets.groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="Wickets")
    )

    fig = px.bar(
        bowlers,
        x="bowler",
        y="Wickets",
        color="Wickets",
        title="Top 10 Wicket Takers"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_toss_decision(matches):
    toss = (
        matches["toss_decision"]
        .value_counts()
        .reset_index()
    )

    toss.columns = ["Decision", "Count"]

    fig = px.pie(
        toss,
        names="Decision",
        values="Count",
        title="Toss Decision Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_match_result(matches):
    result = (
        matches["result"]
        .value_counts()
        .reset_index()
    )

    result.columns = ["Result", "Count"]

    fig = px.pie(
        result,
        names="Result",
        values="Count",
        title="Match Result Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)