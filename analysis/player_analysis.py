import pandas as pd
import matplotlib.pyplot as plt

def player_analysis(matches, deliveries):

    print("\n" + "=" * 60)
    print("MODULE 9 : PLAYER ANALYSIS")
    print("=" * 60)


    orange_cap = (
        deliveries
        .groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n🏏 Top 10 Run Scorers\n")
    print(orange_cap.head(10))

  

    wickets = deliveries[deliveries["is_wicket"] == 1]

    purple_cap = (
        wickets
        .groupby("bowler")["is_wicket"]
        .count()
        .sort_values(ascending=False)
    )

    print("\n🎯 Top 10 Wicket Takers\n")
    print(purple_cap.head(10))

  

    player_of_match = (
        matches["player_of_match"]
        .value_counts()
    )

    print("\n⭐ Top 10 Player of the Match Winners\n")
    print(player_of_match.head(10))



    player_summary = pd.DataFrame({
        "Runs": orange_cap
    })

    player_summary.to_csv(
        "reports/player_summary.csv"
    )

    # ------------------------------------------
    # Graph 1
    # ------------------------------------------

    plt.figure(figsize=(12,6))

    orange_cap.head(10).plot(
        kind="bar",
        color="orange",
        edgecolor="black"
    )

    plt.title("Orange Cap - Top Run Scorers")

    plt.xlabel("Player")

    plt.ylabel("Runs")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


    plt.figure(figsize=(12,6))

    purple_cap.head(10).plot(
        kind="bar",
        color="purple",
        edgecolor="black"
    )

    plt.title("Purple Cap - Top Wicket Takers")

    plt.xlabel("Bowler")

    plt.ylabel("Wickets")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

  

    plt.figure(figsize=(12,6))

    player_of_match.head(10).plot(
        kind="bar",
        color="green",
        edgecolor="black"
    )

    plt.title("Top Player of the Match Winners")

    plt.xlabel("Player")

    plt.ylabel("Awards")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    print("\n✅ player_summary.csv saved successfully!")