document.addEventListener("DOMContentLoaded", function () {
    const activateButton = document.getElementById("activate-button");
    const messageDisplay = document.getElementById("message-display");

    activateButton.addEventListener("click", function () {
        fetch('/activate-assistant')
            .then(response => response.json())
            .then(data => {
                // Display the response message
                messageDisplay.textContent = data.message;
            })
            .catch(error => console.error('Error:', error));
    });
});
