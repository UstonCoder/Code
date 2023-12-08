import pandas as pd
import datetime
df = pd.read_excel(r"C:\Users\charl\OneDrive - Université Paris-Dauphine\Fixture_score.xlsx")

#Date in Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

#Home
home_stats = df.groupby('Home')[['HomeGoals', 'AwayGoals']].sum().rename(columns={'HomeGoals': 'GoalsScored', 'AwayGoals': 'GoalsConceded'})

df["HomeCleanSheets"] = df["AwayGoals"]==0
home_stats["CleanSheets"] = df.groupby('Home')['HomeCleanSheets'].sum()

#Away
away_stats = df.groupby('Away')[['AwayGoals', 'HomeGoals']].sum().rename(columns={'AwayGoals': 'GoalsScored', 'HomeGoals': 'GoalsConceded'})
df["AwayCleanSheets"] = df["HomeGoals"] == 0
away_stats["CleanSheets"] = df.groupby('Away')["AwayCleanSheets"].sum()

# Calcule le nombre de matchs où les deux équipes marquent
df['BothTeamsScored'] = (df['HomeGoals'] > 0) & (df['AwayGoals'] > 0)

home_stats["both_teams_scored"] = df.groupby('Home')["BothTeamsScored"].sum()
away_stats["both_teams_scored"] = df.groupby("Away")["BothTeamsScored"].sum()

#Plus de 2,5 Buts dans le match
df["Over_2.5"]=(df["HomeGoals"]+df["AwayGoals"])> 2.5

home_stats["Over_2.5"] = df.groupby("Home")["Over_2.5"].sum()
away_stats["Over_2.5"] = df.groupby("Away")["Over_2.5"].sum()

home_stats["Games"] = df.groupby("Home")["Home"].count()
away_stats["Games"] = df.groupby("Away")["Away"].count()
#Points number
df["Home_Points"] = df.apply(lambda x: 3 if x["HomeGoals"]>x["AwayGoals"] else 0 if x["HomeGoals"] < x["AwayGoals"] else 1,axis=1)
df["Away_Points"] = df.apply(lambda x: 3 if x["HomeGoals"]<x["AwayGoals"] else 0 if x["HomeGoals"] > x["AwayGoals"] else 1,axis=1)

home_stats["points"] = df.groupby(";Home")["Home_Points"].sum()
away_stats["points"] = df.groupby("Away")["Away_Points"].sum()



#Last Performances
matches = df[['Date', 'Home', 'Away', 'Home_Points', 'Away_Points']].copy()
# Function to get the last 5 games for a team
