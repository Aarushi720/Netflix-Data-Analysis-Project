import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# ------------------ DATA CLEANING ------------------

# Drop rows where date_added is missing (important for time analysis)
df = df.dropna(subset=['date_added']).copy()

# Convert date_added to datetime (correct way)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Drop rows where conversion failed
df = df.dropna(subset=['date_added'])

# Extract year and month
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Fill missing categorical values
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')

# ------------------ ANALYSIS ------------------

# 1. Movies vs TV Shows
type_counts = df['type'].value_counts()

plt.figure()
type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
for i, v in enumerate(type_counts):
    plt.text(i, v, str(v), ha='center')
plt.text(0, max(type_counts)*0.9, "Movies dominate Netflix", color='blue')
plt.tight_layout()
plt.show()

# 2. Content added over years
yearly = df['year_added'].value_counts().sort_index()

plt.figure()
yearly.plot(kind='line', marker='o')
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
max_year = yearly.idxmax()
max_value = yearly.max()

plt.annotate("Peak Content Addition",
             xy=(max_year, max_value),
             xytext=(max_year-2, max_value+500),
             arrowprops=dict(facecolor='black'))
plt.text(yearly.index[3], max_value*0.6,
         "Rapid growth after 2015", color='green')
plt.tight_layout()
plt.show()

# 3. Top 10 countries
top_countries = df['country'].value_counts().head(10)

plt.figure()
top_countries.plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
for i, v in enumerate(top_countries):
    plt.text(i, v, str(v), ha='center')
plt.text(4, max(top_countries)*0.9,
         "USA leads content production", color='purple')
plt.tight_layout()
plt.show()

# 4. Top Genres (from 'listed_in')
genres = df['listed_in'].str.split(', ')
genres_exploded = genres.explode()

top_genres = genres_exploded.value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
for i, v in enumerate(top_genres):
    plt.text(i, v, str(v), ha='center')
plt.text(3, max(top_genres)*0.9,
         "Dramas & Comedies dominate", color='red')
plt.tight_layout()
plt.show()

# 5. Movies vs TV Shows over time
content_trend = df.groupby(['year_added', 'type']).size().unstack()

content_trend.plot(kind='line')
plt.title("Movies vs TV Shows Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.text(2016, content_trend.max().max()*0.7,
         "Movies grew faster than TV Shows", color='green')
peak_year = content_trend.sum(axis=1).idxmax()
peak_value = content_trend.sum(axis=1).max()

plt.annotate("Overall Peak",
             xy=(peak_year, peak_value),
             xytext=(peak_year-2, peak_value+500),
             arrowprops=dict(facecolor='black'))
plt.tight_layout()
plt.show()