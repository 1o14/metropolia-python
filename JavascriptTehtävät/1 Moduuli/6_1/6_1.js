if (confirm("Should I calculate the square root?")) {
    const num = Number(prompt("Enter a number:"));
    if (num < 0) {
        document.body.innerHTML = "The square root of a negative number is not defined.";
    } else {
        document.body.innerHTML = `Square root: ${Math.sqrt(num).toFixed(2)}`;
    }
} else {
    document.body.innerHTML = "Square root not calculated.";
}j