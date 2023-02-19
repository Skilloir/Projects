// Get the button by its id
const embedButton = document.getElementById("embedButton");

// Add an event listener to the button that runs when it's clicked
embedButton.addEventListener("click", function() {
  // Define the data for the embed
  const data = {
    title: "Test",
    body: "Embed Body",
    color: "ff0000", // hex color code
    footer: "Embed Footer"
  };
  // Send a POST request to the Discord integration link
  fetch("https://discord.com/api/webhooks/1005560349656875090/R7VqaoRVTUAPVUCvJDRS8V1bIP2dvJn2mdbj4Yp91FOdbbmWmja7nnUlJ7ctD5Vbqv19", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
});