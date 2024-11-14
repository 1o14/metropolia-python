function concat(strings) {
    let result = "";
    for (let i = 0; i < strings.length; i++) {
        result += strings[i];
    }
    return result;
}

// Hardcoded array
const array = ["Johnny", "DeeDee", "Joey", "Marky"];
const concatenatedString = concat(array);

// Print the result to the HTML document
document.getElementById("result").textContent = concatenatedString;
