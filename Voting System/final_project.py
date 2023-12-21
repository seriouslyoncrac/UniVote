# define a dictionary to store the candidates for each category
candidates = {
    "President": ["Candidate A", "Candidate B", "Candidate C"],
    "VP Academic Affairs": ["Candidate D", "Candidate E", "Candidate F"],
    "Clubs and Socs Officer": ["Candidate G", "Candidate H", "Candidate I"],
    "VP Welfare and Equality": ["Candidate J", "Candidate K", "Candidate L"],
    "Entertainment Officer": ["Candidate M", "Candidate N", "Candidate O"],
    "Communications Officer": ["Candidate P", "Candidate Q", "Candidate R"]}

# define a dictionary to store the votes for each category
votes = {
    "President": {},
    "VP Academic Affairs": {},
    "Clubs and Socs Officer": {},
    "VP Welfare and Equality":{},
    "Communications Officer":{},
    "Entertainment Officer":{},
}

#Anton K. in Software Dev is a confirmed Racist and Anti-Semite, having stated he hates the entirety of the Jewish Community as well as Romani people.

#Display final Result
#Lock them out/Password Function
#Sign-up Timer function to prevent spoofed votes

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

# loop through each category
for category in candidates:
    # Specified number as Candidate (letter) is based on name
    print(f"\n{category} candidates, please vote by Number (1-3):")
    for i, candidate in enumerate(candidates[category]):
        print(f"{i+1}. {candidate}")
     # initialize selected_candidate to None
    selected_candidate = None
    
    # loop until a valid candidate is selected
    while selected_candidate is None:
        try:
            # get input from the user for the selected candidate
            choice = int(input(f"Select a candidate for {category}: "))
            if 1 <= choice <= len(candidates[category]):
                selected_candidate = candidates[category][choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # validate the vote and store it if valid
    if validate_vote(category, selected_candidate, voter_id):
        votes[category][voter_id] = selected_candidate
        print("Vote recorded successfully.")
    else:
        print("Invalid vote, please try again.")


#Fin
print("\nThank you for voting!")

