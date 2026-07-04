import pandas as pd
import matplotlib.pyplot as plt

def toss_analysis(matches):

    print("\n" + "=" * 60)
    print("MODULE 3 : TOSS ANALYSIS")
    print("=" * 60)


    toss_winner = matches["toss_winner"].value_counts()

    print("\nTop Teams Winning Toss\n")
    print(toss_winner.head(10))

    
    toss_decision = matches["toss_decision"].value_counts()

    print("\nToss Decisions\n")
    print(toss_decision)

    

    toss_match_win = (
        matches["toss_winner"] == matches["winner"]
    ).sum()

    total_matches = len(matches)

    toss_advantage = (
        toss_match_win / total_matches
    ) * 100

    print(f"\nToss Advantage : {toss_advantage:.2f}%")

    # ------------------------------------------
    # Plot Toss Decision
    # ------------------------------------------

    plt.figure(figsize=(6,6))

    toss_decision.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.ylabel("")

    plt.title("Toss Decision Distribution")

    plt.tight_layout()

    plt.show()