import pandas as pd
import matplotlib.pyplot as plt

def team_analysis(matches):

    print("\n" + "=" * 60)
    print("MODULE 2 : TEAM ANALYSIS")
    print("=" * 60)

    # ------------------------------------------
    # Matches Played
    # ------------------------------------------

    matches_played = (
        matches["team1"]
        .value_counts()
        .add(matches["team2"].value_counts(), fill_value=0)
        .sort_values(ascending=False)
    )

    print("\nTop 10 Teams by Matches Played\n")
    print(matches_played.head(10))

    # ------------------------------------------
    # Wins
    # ------------------------------------------

    team_wins = matches["winner"].value_counts()

    print("\nTop 10 Teams by Wins\n")
    print(team_wins.head(10))

    # ------------------------------------------
    # Win Percentage
    # ------------------------------------------

    team_summary = pd.DataFrame({
        "Matches_Played": matches_played,
        "Wins": team_wins
    }).fillna(0)

    team_summary["Win_Percentage"] = (
        team_summary["Wins"] /
        team_summary["Matches_Played"] * 100
    ).round(2)

    print("\nTeam Performance Summary\n")
    print(team_summary.sort_values(
        "Win_Percentage",
        ascending=False
    ).head(10))

    # ------------------------------------------
    # Graph
    # ------------------------------------------

    plt.figure(figsize=(12,6))

    team_wins.head(10).plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Top 10 Teams by Wins")

    plt.xlabel("Team")

    plt.ylabel("Wins")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()