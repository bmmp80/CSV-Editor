import csv
import pandas as pd
import shutil
from tempfile import NamedTemporaryFile

#columns to remove: A, B, C, G, H, I, K, L, P, V, W, Z, AB
#want to keep data that satisfies:
#if column D >= 2000
#if column E != preseason
#if column F <= 15 (only doing regular season, 16 is test data)
#if column M isn't 0 or blank

#will be left with:
#D
#E
#F
#M
#N: passes completed
#O: passes attempted
#Q: passing yards
#R: yards/attempt
#S: TD passes
#T: interceptions
#U: sacks
#X: rushing yards
#Y: rushing attempts
#Z: yards/carry
#AA: rushing TDs
#AB: fumbles lost

#column J is class (win/loss)
df = pd.read_csv("Game_Logs_Quarterback.csv", header=1)
outputdf = ((df[df['D']>=2000][df['E']!="Preseason"][df['E']!="Postseason"][df['F']<=15][df['M']!="0"]).loc[:,['D', 'E', 'F', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'X', 'Y', 'Z', 'AA', 'AC']])
#outputdf = ((df[df['Year']>=2000][df['Season']!="Preseason"][df['Season']!="Postseason"][df['Week']<=15][df['Games Started']!="0"]).loc[:,['Year', 'Season', 'Week', 'Games Started', 'Passes Completed', 'Passes Attempted', 'Yards', 'Yards Per Attempt', 'TD Passes', 'Ints', 'Sacks', 'Rushing Attempts', 'Rushing Yards', 'Yards Per Carry', 'Rushing TDs', 'Fumbles Lost']])

outputdf.to_csv("output.csv", index=False)

