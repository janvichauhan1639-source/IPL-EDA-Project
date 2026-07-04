import pandas as pd
import matplotlib.pyplot as plt

def venue_analysis(matches, deliveries):

    print("\n" + "=" * 60)
    print("MODULE 6 : VENUE ANALYSIS")
    print("=" * 60)



    venue_data = deliveries.merge(
        matches[["id", "venue"]],
        left_on="match_id",
        right_on="id",
        how="left"
    )



    venue_runs = (
        venue_data
        .groupby("venue")["total_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n🏟️ Top 10 Highest Scoring Venues\n")
    print(venue_runs.head(10))


    venue_matches = (
        matches["venue"]
        .value_counts()
    )

    print("\n🏏 Top 10 Venues by Matches\n")
    print(venue_matches.head(10))



    avg_runs = (
        venue_runs / venue_matches
    ).round(2)

    venue_summary = pd.DataFrame({
        "Matches": venue_matches,
        "Total_Runs": venue_runs,
        "Average_Runs": avg_runs
    }).fillna(0)

    print("\n📊 Venue Summary\n")
    print(
        venue_summary.sort_values(
            "Average_Runs",
            ascending=False
        ).head(10)
    )


    venue_summary.to_csv(
        "reports/venue_summary.csv"
    )

   
    plt.figure(figsize=(14,6))

    venue_runs.head(10).plot(
        kind="bar",
        color="teal",
        edgecolor="black"
    )

    plt.title("Top 10 Highest Scoring Venues")

    plt.xlabel("Venue")

    plt.ylabel("Runs")

    plt.xticks(rotation=75)

    plt.tight_layout()

    plt.show()

    print("\n✅ venue_summary.csv saved successfully!")