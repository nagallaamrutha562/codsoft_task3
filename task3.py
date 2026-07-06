import os

def clear_screen():
    # Standard helper function to clear the console output
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# --- DATA DATABASE ---
# A clean dictionary mapping movies to their attributes
MOVIES = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "The Dark Knight": ["Action", "Crime"],
    "Interstellar": ["Sci-Fi", "Adventure"],
    "Spirited Away": ["Animation", "Fantasy"],
    "The Lion King": ["Animation", "Drama"],
    "The Hangover": ["Comedy"],
    "Superbad": ["Comedy"],
    "The Conjuring": ["Horror"],
    "Get Out": ["Horror", "Thriller"],
    "La La Land": ["Romance", "Musical"],
    "The Notebook": ["Romance", "Drama"]
}

print("--- RECOMMENDATION SYSTEM STARTING ---")

# Step 1: Gather User Inputs
username = input("Enter your name: ")

print("\nAvailable genres: Action, Sci-Fi, Thriller, Crime, Adventure, Animation, Fantasy, Drama, Comedy, Horror, Romance")
user_input_genres = input("Enter your favorite genres (separate them with commas): ")

# Clean up the user input into a tidy list
fav_genres = []
for g in user_input_genres.split(","):
    fav_genres.append(g.strip().lower())

# Unique Feature 1: The Mood Filter
print("\nHow are you feeling right now?")
print("1. Happy (wants lighthearted fun)")
print("2. Bored (wants intense action or thriller)")
print("3. Tired (wants a casual regular movie)")
mood = input("Select mood (1, 2, or 3): ").strip()

# Adjust recommendations based on student mood parameters
mood_genres = []
if mood == "1":
    mood_genres = ["comedy", "animation", "fantasy", "musical"]
elif mood == "2":
    mood_genres = ["action", "sci-fi", "thriller", "horror"]

# Step 2: Calculate Recommendation Scores
movie_scores = {}

for movie_title, movie_genres in MOVIES.items():
    score = 0
    
    # Convert movie genres to lower case to prevent matching errors
    lower_movie_genres = []
    for mg in movie_genres:
        lower_movie_genres.append(mg.lower())
        
    # Check for regular genre matches
    for genre in fav_genres:
        if genre in lower_movie_genres:
            score += 3  # Add 3 points for matching user preference
            
    # Apply our unique mood modifier weights
    for m_genre in mood_genres:
        if m_genre in lower_movie_genres:
            score += 2  # Add 2 bonus points if it suits the user's current mood
            
    # Only consider recommending it if it has at least some match score
    if score > 0:
        movie_scores[movie_title] = score

# Sort the results from highest score to lowest score
# This uses basic Python sorting logic that students learn in class
sorted_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

# Step 3: Present Results to the User
clear_screen()
print("=========================================")
print(f"      RECOMMENDATIONS FOR {username.upper()}  ")
print("=========================================")

top_three = sorted_movies[:3]

if not top_three:
    print("We couldn't find any perfect matches for those specific genres.")
    print("Try checking out our top movie: Inception!")
else:
    print("Based on your taste profile and mood, we recommend:\n")
    for index, (title, score) in enumerate(top_three, 1):
        # Fetch original genre tags to display beautifully
        original_genres = ", ".join(MOVIES[title])
        print(f"{index}. {title} [Genres: {original_genres}] (Match Score: {score})")

print("=========================================")

# Unique Feature 2: Watchlist File Generator
print("\nWould you like to save these top picks to your watchlist file?")
save_choice = input("Type 'yes' to save or 'no' to skip: ").strip().lower()

if save_choice == 'yes' and top_three:
    # Open or create a local text file using basic file handling
    file = open("my_watchlist.txt", "w")
    file.write(f"--- {username}'s Personal Watchlist ---\n")
    for title, score in top_three:
        file.write(f"- {title}\n")
    file.close()
    print("Success! Your recommendations have been exported to 'my_watchlist.txt'.")
else:
    print("Thank you for using the recommendation engine!")