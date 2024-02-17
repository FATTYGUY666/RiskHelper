// Define a function to handle when the document is loaded
document.addEventListener("DOMContentLoaded", function() {
    // Your JavaScript code goes here
    // For example, you can add event listeners, manipulate the DOM, etc.

    // Example: Change the text of an element with id "example-element"
    var exampleElement = document.getElementById("example-element");
    if (exampleElement) {
        exampleElement.textContent = "Hello, JavaScript!";
    }

    // Example: Add a click event listener to an element with id "click-me-button"
    var clickMeButton = document.getElementById("click-me-button");
    if (clickMeButton) {
        clickMeButton.addEventListener("click", function() {
            alert("Button clicked!");
        });
    }
});