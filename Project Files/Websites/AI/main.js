const API_KEY = "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";
const API_ENDPOINT = "https://api.openai.com/v1/engines/YOUR_ENGINE_ID/jobs";

const inputText = document.getElementById("inputText");
const sendBtn = document.getElementById("sendBtn");
const resultContainer = document.createElement("h2");
document.body.appendChild(resultContainer);

sendBtn.addEventListener("click", function() {
  const inputValue = inputText.value;

  fetch(API_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${API_KEY}`
    },
    body: JSON.stringify({
      prompt: inputValue,
      max_tokens: 100,
      n: 1,
      stop: null,
      temperature: 0.5
    })
  })
  .then(response => {
    return response.json();
  })
  .then(data => {
    console.log(data);
    resultContainer.innerHTML = data.choices[0].text;
  })
  .catch(error => {
    console.error(error);
  });
});
