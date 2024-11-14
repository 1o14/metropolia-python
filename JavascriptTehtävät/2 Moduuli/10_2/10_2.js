const candidates = [];
const voters = [];

// Get number of candidates
const numCandidates = parseInt(prompt("Enter the number of candidates:"));
for (let i = 1; i <= numCandidates; i++) {
    const name = prompt(`Name for candidate ${i}`);
    candidates.push({ name, votes: 0 });
}

// Get number of voters
const numVoters = parseInt(prompt("Enter the number of voters:"));
for (let i = 1; i <= numVoters; i++) {
    const vote = prompt(`Voter ${i}, enter the name of the candidate you vote for (or leave empty for blank vote):`);
    if (vote) {
        const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
        if (candidate) {
            candidate.votes++;
        } else {
            console.log(`Invalid vote: ${vote}`);
        }
    }
}

// Sort candidates by votes
candidates.sort((a, b) => b.votes - a.votes);

// Display results
console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log("Results:");
candidates.forEach(candidate => {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
});
