import pandas as pd
import matplotlib.pyplot as plt

def bowling_analysis(deliveries):

    print("\n" + "=" * 60)
    print("MODULE 5 : BOWLING ANALYSIS")
    print("=" * 60)

    wickets = deliveries[deliveries["is_wicket"] == 1]

    bowler_wickets = (
        wickets
        .groupby("bowler")["is_wicket"]
        .count()
        .sort_values(ascending=False)
    )

    print("\n🎯 Top 10 Wicket Takers\n")
    print(bowler_wickets.head(10))

   
    bowler_runs = (
        deliveries
        .groupby("bowler")["total_runs"]
        .sum()
    )

    bowler_balls = (
        deliveries
        .groupby("bowler")
        .size()
    )

    economy = (
        (bowler_runs * 6) / bowler_balls
    ).round(2)

    economy_df = pd.DataFrame({
        "Runs_Conceded": bowler_runs,
        "Balls": bowler_balls,
        "Economy": economy
    })

    print("\n🎯 Best Economy Bowlers (Minimum 300 Balls)\n")

    print(
        economy_df[economy_df["Balls"] >= 300]
        .sort_values("Economy")
        .head(10)
    )

    
    bowling_summary = pd.DataFrame({
        "Wickets": bowler_wickets
    })

    bowling_summary.to_csv(
        "reports/bowling_summary.csv"
    )

    

    plt.figure(figsize=(12,6))

    bowler_wickets.head(10).plot(
        kind="bar",
        color="purple",
        edgecolor="black"
    )

    plt.title("Top 10 Wicket Takers")

    plt.xlabel("Bowler")

    plt.ylabel("Wickets")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    print("\n✅ bowling_summary.csv saved successfully!")