import pandas as pd

data = {
    "movie_id": ["M1", "M2", "M3", "M4", "M5", "M6"],
    "title": ["Inception", "Interstellar", "3 Idiots", "Dangal", "Sholay", "Pathaan"],
    "genre": ["Sci-Fi", "Sci-Fi", "Comedy", "Drama", "Action", "Action"],
    "release_year": [2010, 2014, 2009, 2016, 1975, 2023],
    "imdb_rating": [8.8, 8.7, 8.4, 8.4, 8.2, 6.8],
    "box_office_crores": [800, 750, 400, 2000, 35.0, 1050]
}
df = pd.DataFrame(data)
df.to_excel("04_movies.xlsx", index=False)

# Q1: Genre-wise average rating and total box office
genre_agg = df.groupby("genre").agg({"imdb_rating": "mean", "box_office_crores": "sum"})
print("Q1 - Genre Aggregations:\n", genre_agg)

# Q2: Top 3 highest grossing movies
top_grossing = df.sort_values(by="box_office_crores", ascending=False).head(3)
print("\nQ2 - Top Grossing Movies:\n", top_grossing[["title", "box_office_crores"]])

# Q3: Filter post-2020 high-rated movies
modern_hits = df[(df["release_year"] > 2020) & (df["imdb_rating"] > 8.0)]
print("\nQ3 - Modern Hits:\n", modern_hits)

# Q4: Count movies per genre
genre_counts = df["genre"].value_counts()
print("\nQ4 - Genre Counts:\n", genre_counts)

# Q5: Add conditional success tag
df["success_tag"] = df["box_office_crores"].apply(lambda x: "Blockbuster" if x > 300 else "Hit/Average")
print("\nQ5 - Success Tags:\n", df[["title", "box_office_crores", "success_tag"]])