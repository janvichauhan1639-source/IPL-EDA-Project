import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """Load IPL datasets"""
    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")
    return matches, deliveries


def get_total_matches(matches):
    return len(matches)


def get_total_runs(deliveries):
    return deliveries["total_runs"].sum()


def get_total_wickets(deliveries):
    return deliveries["is_wicket"].sum()


def get_total_teams(matches):
    teams = pd.concat([matches["team1"], matches["team2"]]).unique()
    return len(teams)


def get_top_batsmen(deliveries, top_n=10):
    return (
        deliveries.groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


def get_top_bowlers(deliveries, top_n=10):
    wickets = deliveries[deliveries["is_wicket"] == 1]

    return (
        wickets.groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index(name="Wickets")
    )


def get_team_wins(matches):
    return (
        matches["winner"]
        .value_counts()
        .head(10)
        .reset_index()
        .rename(columns={"index": "Team", "winner": "Wins"})
    )


def get_matches_per_season(matches):
    return (
        matches.groupby("season")
        .size()
        .reset_index(name="Matches")
    )