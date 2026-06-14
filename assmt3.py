import random

# List of teams in the tournament
teams = ["Uganda", "Kenya", "Brazil", "France", "England", "Germany", "Japan", "Argentina"]

print("WELCOME TO THE WORLD CUP 2026 SIMULATOR")
print("Available teams:", teams)

while True:
    # Get user input
    user_choice = input("\nType 'play' to run the tournament, 'list' to see teams, or 'exit' to quit: ").strip().lower()
    
    # 1. Using BREAK to exit the loop completely
    if user_choice == "exit":
        print("Exiting the simulator. Goodbye!")
        break
        
    # 2. Using CONTINUE to skip the rest of the code and restart the loop
    if user_choice == "list":
        print("Current teams in the mix:", teams)
        continue  
        
    # 3. Using PASS as a placeholder for an option we might build later
    if user_choice == "help":
        # TODO: Add a help menu later
        pass  
        continue

    # Run the tournament simulation if they type 'play'
    if user_choice == "play":
        print("\n--- Tournament Started! ---")
        
        current_round = teams.copy()
        
        # Loop until only 1 team is left
        while len(current_round) > 1:
            next_round = []
            print(f"\nPlaying matches for a pool of {len(current_round)} teams...")
            
            # Pair up teams up and make them face each other
            for i in range(0, len(current_round), 2):
                team1 = current_round[i]
                team2 = current_round[i+1]
                
                # Pick a random winner
                winner = random.choice([team1, team2])
                print(f"Match: {team1} vs {team2} -> Winner: {winner}!")
                next_round.append(winner)
                
            # Move the winners to the next round
            current_round = next_round
            
        # Print the grand champion
        print("\n")
        print(f"🏆 {current_round[0].upper()} WINS THE WORLD CUP 2026! 🏆")
        print("")
        
    else:
        print("Invalid input. Please try again.")
