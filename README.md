DATASET
Dataset used: netflix_titles.csv
Contains information about:
-Type (Movie / TV Show)
-Country
-Date added
-Genre
-Director and more

DATA CLEANING STEPS
Removed rows with missing date_added
Converted date_added to datetime format
Extracted:
-year_added
-month_added
-Filled missing values:
-country → "Unknown"
-director → "Unknown"

Analysis & Visualizations
1.Movies vs TV Shows
Compared total number of Movies and TV Shows
 Insight: Movies dominate Netflix’s content library
2.Content Added Over Years
Analyzed how content additions changed over time
 Insight: Rapid growth observed after 2015, with a peak in recent years
3.Top 10 Content Producing Countries
Identified countries contributing the most content
 Insight: United States leads significantly in content production
4.Top 10 Genres
Extracted and analyzed genres from the dataset
 Insight: Drama and Comedy are the most popular genres
5.Movies vs TV Shows Over Time
Compared growth trends of Movies vs TV Shows
 Insight: Movies have grown faster, but TV Shows are steadily increasing

TECHNOLOGIES USED
Python
Pandas
Matplotlib
