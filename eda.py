
import pandas as pd
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

from analysis.dataset_overview import dataset_overview
from analysis.team_analysis import team_analysis
from analysis.toss_analysis import toss_analysis
from analysis.batting_analysis import batting_analysis
from analysis.bowling_analysis import bowling_analysis
from analysis.venue_analysis import venue_analysis
from analysis.season_analysis import season_analysis
from analysis.boundary_analysis import boundary_analysis
from analysis.player_analysis import player_analysis
from analysis.export_reports import export_reports

print("=" * 60)
print("🏏 IPL DATA ANALYTICS PROJECT")
print("=" * 60)

dataset_overview(matches, deliveries)

team_analysis(matches)
toss_analysis(matches)
batting_analysis(deliveries)
bowling_analysis(deliveries)
venue_analysis(matches, deliveries)
season_analysis(matches, deliveries)
boundary_analysis(deliveries)
player_analysis(matches, deliveries)
export_reports(matches, deliveries)
print("\n" + "=" * 60)
print("✅ ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)
