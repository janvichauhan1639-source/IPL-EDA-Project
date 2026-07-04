import pandas as pd

def dataset_overview(matches, deliveries):

    print("\n" + "=" * 60)
    print("MODULE 1 : DATASET OVERVIEW")
    print("=" * 60)

    print("\nMatches Shape :", matches.shape)
    print("Deliveries Shape :", deliveries.shape)

    print("\nMatches Columns")
    print(matches.columns.tolist())

    print("\nDeliveries Columns")
    print(deliveries.columns.tolist())

    print("\nMatches Data Types")
    print(matches.dtypes)

    print("\nDeliveries Data Types")
    print(deliveries.dtypes)

    print("\nMissing Values (Matches)")
    print(matches.isnull().sum())

    print("\nMissing Values (Deliveries)")
    print(deliveries.isnull().sum())

    print("\nDuplicate Rows (Matches):", matches.duplicated().sum())
    print("Duplicate Rows (Deliveries):", deliveries.duplicated().sum())