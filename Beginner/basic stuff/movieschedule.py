current_movies = {
    "The Matrix": ["12:00", "15:30", "19:00"],
    "Dune": ["13:15", "16:45"],
    "Spirited Away": ["11:00", "14:30", "18:00"],
}

print(f"currently showing:{current_movies}")

movie= input("Enter the movie you want to watch: ")
selectMovie= current_movies.get(movie) #case sensitive  

if selectMovie:
    print(f"Movie showing at: {selectMovie}")
else:
    print("Sorry, that movie is not currently showing.")
    
