import time
import threading

# define a dictionary to store the candidates for each category
candidates = {
    "President": ["Candidate A", "Candidate B", "Candidate C"],
    "VP Academic Affairs": ["Candidate D", "Candidate E", "Candidate F"],
    "Clubs and Socs Officer": ["Candidate G", "Candidate H", "Candidate I"],
    "VP Welfare and Equality": ["Candidate J", "Candidate K", "Candidate L"],
    "Entertainment Officer": ["Candidate M", "Candidate N", "Candidate O"],
    "Communications Officer": ["Candidate P", "Candidate Q", "Candidate R"]
}

# define a dictionary to store the votes for each category
votes = {
    "President": {},
    "VP Academic Affairs": {},
    "Clubs and Socs Officer": {},
    "VP Welfare and Equality": {},
    "Communications Officer": {},
    "Entertainment Officer": {},
}

# define a function to validate the vote
def validate_vote(category, candidate, voter_id):
    if voter_id in votes[category]:
        print("You have already voted for this category.")
        return False
    if candidate not in candidates[category]:
        print("Invalid candidate selected.")
        return False
    return True

# get input from the user
voter_id = input("Enter your voter ID: ")

# Simulated signup timer with 30 seconds
print(f"Signup timer started. You have 30 seconds to sign up.")

# loop through each category
for category in candidates:
    # Specified number as Candidate (letter) is based on name
    print(f"\n{category} candidates, please vote by Number (1-3):")
    for i, candidate in enumerate(candidates[category]):
        print(f"{i+1}. {candidate}")
    
    try:
        # get input from the user for the selected candidate with a timeout of 30 seconds
        choice = input(f"Select a candidate for {category}: ")
    except KeyboardInterrupt:
        print("\nSignup timer expired.")
        exit()

    # validate the vote and store it if valid
    if validate_vote(category, choice, voter_id):
        votes[category][voter_id] = candidates[category][int(choice) - 1]
        print("Vote recorded successfully.")
    else:
        print("Invalid vote, please try again.")

# Fin
print("\nThank you for voting!")