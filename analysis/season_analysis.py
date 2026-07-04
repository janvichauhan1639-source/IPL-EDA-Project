import pandas as pd
import matplotlib.pyplot as plt

def season_analysis(matches, deliveries):

    print("\n" + "=" * 60)
    print("MODULE 7 : SEASON ANALYSIS")
    print("=" * 60)

    season_matches = (
        matches
        .groupby("season")
        .size()
        .sort_index()
    )

    print("\n📅 Matches Played Per Season\n")
    print(season_matches)


    season_data = deliveries.merge(
        matches[["id", "season"]],
        left_on="match_id",
        right_on="id",
        how="left"
    )

   
    season_runs = (
        season_data
        .groupby("season")["total_runs"]
        .sum()
        .sort_index()
    )

    print("\n🏏 Total Runs Per Season\n")
    print(season_runs)


    avg_runs = (
        season_runs / season_matches
    ).round(2)

    season_summary = pd.DataFrame({
        "Matches": season_matches,
        "Runs": season_runs,
        "Average_Runs": avg_runs
    })

    print("\n📊 Season Summary\n")
    print(season_summary)


    season_summary.to_csv(
        "reports/season_summary.csv"
    )



    plt.figure(figsize=(12,5))

    season_matches.plot(
        kind="line",
        marker="o",
        linewidth=2
    )

    plt.title("Matches Played Per Season")

    plt.xlabel("Season")

    plt.ylabel("Matches")

    plt.grid(True)

    plt.tight_layout()

    plt.show()

    # ------------------------------------------
    # Graph 2
    # ------------------------------------------

    plt.figure(figsize=(12,5))

    season_runs.plot(
        kind="bar",
        color="orange",
        edgecolor="black"
    )

    plt.title("Total Runs Per Season")

    plt.xlabel("Season")

    plt.ylabel("Runs")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    print("\n✅ season_summary.csv saved successfully!")