const textInput = document.querySelector("#text-input");
const checkButton = document.querySelector("#check-btn");
const resultText = document.querySelector("#result");
const form = document.querySelector("form");

const sanitizeInput = (str) => {
  const regex = /[^a-zA-Z\d]/g;
  const sanitized = str.replace(regex, "").toLowerCase();
  return sanitized;
};

const isPalindrome = (str) => {
  const reversed = str.split("").toReversed().join("");
  if (str === reversed) return true;
  return false;
};

const handleSubmit = (e) => {
  e.preventDefault();

  if (!textInput.value) {
    alert("Please input a value");
  }
  const sanitized = sanitizeInput(textInput.value);
  if (isPalindrome(sanitized)) {
    resultText.classList.replace("red", "green");
    resultText.innerText = `${textInput.value} is a palindrome`;
  } else {
    resultText.classList.replace("green", "red");
    resultText.innerText = `${textInput.value} is not a palindrome`;
  }
};

form.onsubmit = handleSubmit;
