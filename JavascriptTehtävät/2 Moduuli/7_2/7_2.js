function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

// Get the number of sides from the user
const sides = parseInt(prompt("Enter the number of sides for the dice:"));
if (isNaN(sides) || sides < 2) {
    document.getElementById("result").textContent = "Invalid number of sides.";
} else {
    let rolls = [];
    let roll;
    do {
        roll = rollDice(sides);
        rolls.push(roll);
    } while (roll !== sides);

    // Print the results to the HTML document
    document.getElementById("result").textContent = `Rolls: ${rolls.join(", ")}`;
}
