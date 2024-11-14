const name = prompt("What is your name?");
const houseNumber = Math.floor(Math.random() * 4) + 1;

const houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];
document.body.innerHTML = `${name}, you are in ${houses[houseNumber - 1]}.`;
