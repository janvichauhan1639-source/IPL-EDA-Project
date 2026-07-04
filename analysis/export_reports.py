import os
import pandas as pd

def export_reports(matches, deliveries):

    print("\n" + "=" * 60)
    print("MODULE 10 : EXPORT REPORTS")
    print("=" * 60)

    
    os.makedirs("reports", exist_ok=True)

    

    team_matches = (
        matches["team1"]
        .value_counts()
        .add(matches["team2"].value_counts(), fill_value=0)
    )

    team_wins = matches["winner"].value_counts()

    team_summary = pd.DataFrame({
        "Team": team_matches.index,
        "Matches_Played": team_matches.values
    })

    team_summary["Wins"] = (
        team_summary["Team"]
        .map(team_wins)
        .fillna(0)
        .astype(int)
    )

    team_summary["Win_Percentage"] = (
        team_summary["Wins"] /
        team_summary["Matches_Played"] * 100
    ).round(2)

    team_summary.to_csv(
        "reports/team_summary.csv",
        index=False
    )

    

    batting_summary = (
        deliveries.groupby("batter")["batsman_runs"]
        .sum()
        .reset_index()
    )

    batting_summary.columns = ["Player", "Runs"]

    batting_summary.to_csv(
        "reports/batting_summary.csv",
        index=False
    )

   
    bowling_summary = (
        deliveries[deliveries["is_wicket"] == 1]
        .groupby("bowler")["is_wicket"]
        .count()
        .reset_index()
    )

    bowling_summary.columns = ["Bowler", "Wickets"]

    bowling_summary.to_csv(
        "reports/bowling_summary.csv",
        index=False
    )

   

    venue_summary = (
        matches["venue"]
        .value_counts()
        .reset_index()
    )

    venue_summary.columns = ["Venue", "Matches"]

    venue_summary.to_csv(
        "reports/venue_summary.csv",
        index=False
    )

    

    season_summary = (
        matches.groupby("season")
        .size()
        .reset_index(name="Matches")
    )

    season_summary.to_csv(
        "reports/season_summary.csv",
        index=False
    )

    print("\n" + "=" * 60)
    print("✅ ALL REPORTS EXPORTED SUCCESSFULLY")
    print("=" * 60)

    print("\nGenerated Reports:")

    print("✔ team_summary.csv")
    print("✔ batting_summary.csv")
    print("✔ bowling_summary.csv")
    print("✔ venue_summary.csv")
    print("✔ season_summary.csv")