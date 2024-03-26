"""
Task 1: Artist Lineup Compilation
    - You are provided with a list of artist names scheduled to perform at different stages of the music festival. Using a loop, compile these artist names into a set to create a unique lineup without duplicates.
"""
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

unique_artists = {artist for artist in artist_names}

print(unique_artists)


"""
Task 2: Genre Sorting
    - You have a list of genres associated with each artist. Using a loop with sets, categorize artists by their genres, creating a set for each genre.
"""
artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}

for artist, genre in artists_genres.items():
    print(f"Genre: {genre}, Artists: {artist}")


"""
Task 3: Playlist Duplication Check
    - Create a Python script that takes multiple playlist sets and checks if any playlist is a duplicate of another (i.e., contains the same set of songs).
"""
playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

if playlist1 <= playlist2 or playlist2 <= playlist3 or playlist1 <= playlist3:
    print("Duplicate playlists found.")
else:
    print("There are no duplicate playlists.")


