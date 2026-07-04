import pandas as pd
import matplotlib.pyplot as plt

def boundary_analysis(deliveries):

    print("\n" + "=" * 60)
    print("MODULE 8 : BOUNDARY ANALYSIS")
    print("=" * 60)



    fours = deliveries[deliveries["batsman_runs"] == 4]

    total_fours = len(fours)

    print(f"\n🏏 Total Fours : {total_fours}")

    top_fours = (
        fours.groupby("batter")
        .size()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Players with Most Fours\n")

    print(top_fours.head(10))


    sixes = deliveries[deliveries["batsman_runs"] == 6]

    total_sixes = len(sixes)

    print(f"\n💥 Total Sixes : {total_sixes}")

    top_sixes = (
        sixes.groupby("batter")
        .size()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Players with Most Sixes\n")

    print(top_sixes.head(10))


    total_balls = len(deliveries)

    boundary_percentage = (
        (total_fours + total_sixes)
        / total_balls
    ) * 100

    print(f"\nBoundary Percentage : {boundary_percentage:.2f}%")



    boundary_summary = pd.DataFrame({

        "Player": top_fours.index,

        "Fours": top_fours.values

    })

    boundary_summary.to_csv(

        "reports/boundary_summary.csv",

        index=False

    )

    

    plt.figure(figsize=(12,6))

    top_fours.head(10).plot(

        kind="bar",

        color="dodgerblue",

        edgecolor="black"

    )

    plt.title("Top 10 Players by Fours")

    plt.xlabel("Player")

    plt.ylabel("Fours")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    plt.figure(figsize=(12,6))

    top_sixes.head(10).plot(

        kind="bar",

        color="crimson",

        edgecolor="black"

    )

    plt.title("Top 10 Players by Sixes")

    plt.xlabel("Player")

    plt.ylabel("Sixes")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    print("\n✅ boundary_summary.csv saved successfully!")