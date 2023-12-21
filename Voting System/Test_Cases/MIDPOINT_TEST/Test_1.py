from flask import Flask, render_template, request
import time
import threading


app = Flask(__name__)

# Define the candidates for each category
candidates = {
    "President": ["Candidate A", "Candidate B", "Candidate C"],
    "VP Academic Affairs": ["Candidate D", "Candidate E", "Candidate F"],
    "Clubs and Socs Officer": ["Candidate G", "Candidate H", "Candidate I"],
    "VP Welfare and Equality": ["Candidate J", "Candidate K", "Candidate L"],
    "Entertainment Officer": ["Candidate M", "Candidate N", "Candidate O"],
    "Communications Officer": ["Candidate P", "Candidate Q", "Candidate R"]
}

# Dictionary to store the votes for each category
votes = {
    "President": {},
    "VP Academic Affairs": {},
    "Clubs and Socs Officer": {},
    "VP Welfare and Equality": {},
    "Entertainment Officer": {},
    "Communications Officer": {}
}

@app.route('/')
def index():
    """Render the index.html template with the candidates."""
    return render_template('index.html', candidates=candidates)

@app.route('/submit', methods=['POST'])
def submit_vote():
    """Handle the form submission and process the votes."""
    voter_id = request.form.get('voter_id')

    # Loop through each category to validate and record the vote
    for category, candidate_list in candidates.items():
        choice = request.form.get(category)
        
        # Check if a choice was made for the category
        if not choice:
            return "Please select a candidate for all categories."

        # Check if the voter has already voted in this category
        if voter_id in votes[category]:
            return "You have already voted for this category."

        # Validate the selected candidate
        if choice not in candidate_list:
            return "Invalid candidate selected."

        # Record the vote
        votes[category][voter_id] = choice

    return "Vote recorded successfully."

if __name__ == '__main__':
    app.run(debug=True)
