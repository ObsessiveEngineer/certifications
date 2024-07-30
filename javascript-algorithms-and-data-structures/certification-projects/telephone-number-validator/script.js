const checkButton = document.getElementById("check-btn");
const clearButton = document.getElementById("clear-btn");
const userInput = document.getElementById("user-input");
const resultsDiv = document.getElementById("results-div");
const form = document.querySelector("form");

const isUsPhoneNumber = (input) => {
  const cleansed = input.replace(/\s/g, "");
  const regex = /^1?(?:\([0-9]{3}\)|[0-9]{3})(?:-|)[0-9]{3}(?:-|)[0-9]{4}$/;//Yeah I looooooooove regex
  return regex.test(cleansed);
};

form.onsubmit = (e) => {
  e.preventDefault();
  if (userInput.value === "") {
    alert("Please provide a phone number");
    return;
  }

  resultsDiv.classList.remove("error", "success");
  if (isUsPhoneNumber(userInput.value)) {
    resultsDiv.classList.add("success");
    resultsDiv.innerText = `Valid US Number: ${userInput.value}`;
  } else {
    resultsDiv.classList.add("error");
    resultsDiv.innerText = `Invalid US Number: ${userInput.value}`;
  }

  return;
};

clearButton.onclick = () => {
  resultsDiv.innerText = "";
};
