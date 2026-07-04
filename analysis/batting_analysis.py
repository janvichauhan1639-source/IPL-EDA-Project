import pandas as pd
import matplotlib.pyplot as plt

def batting_analysis(deliveries):

    print("\n" + "=" * 60)
    print("MODULE 4 : BATTING ANALYSIS")
    print("=" * 60)

   

    batsman_runs = (
        deliveries
        .groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n🏏 Top 10 Run Scorers\n")
    print(batsman_runs.head(10))

    
    boundaries = deliveries[
        deliveries["batsman_runs"].isin([4, 6])
    ]

    boundary_count = (
        boundaries
        .groupby("batter")
        .size()
        .sort_values(ascending=False)
    )

    print("\n💥 Top 10 Boundary Hitters\n")
    print(boundary_count.head(10))


    batting_summary = pd.DataFrame({
        "Runs": batsman_runs
    })

    batting_summary.to_csv(
        "reports/batting_summary.csv"
    )

    

    plt.figure(figsize=(12,6))

    batsman_runs.head(10).plot(
        kind="bar",
        color="orange",
        edgecolor="black"
    )

    plt.title("Top 10 Run Scorers")

    plt.xlabel("Batsman")

    plt.ylabel("Runs")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    print("\n✅ batting_summary.csv saved successfully!")