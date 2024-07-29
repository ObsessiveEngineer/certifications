const numberInput = document.getElementById("number");
const convertButton = document.getElementById("convert-btn");
const outputParaph = document.getElementById("output");

const handleSubmit = (e) => {
  e.preventDefault();
  const parsedInput = parseInt(numberInput.value);

  outputParaph.classList.remove("success", "error");

  if (!numberInput.value) {
    outputParaph.classList.add("error");
    outputParaph.innerText = "Please enter a valid number";
  } else if (parsedInput <= -1) {
    outputParaph.classList.add("error");
    outputParaph.innerText = "Please enter a number greater than or equal to 1";
  } else if (parsedInput >= 4000) {
    outputParaph.classList.add("error");
    outputParaph.innerText = "Please enter a number less than or equal to 3999";
  } else {
    outputParaph.classList.add("success");
    outputParaph.innerText = convertNumeralToRoman(parsedInput);
  }
};

const convertNumeralToRoman = (number) => {
  let result = "";
  let converted = number;
  const equalityTable = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1,
  };

  for (const key in equalityTable) {
    const quotient = Math.floor(number / equalityTable[key]);
    result += key.repeat(quotient);
    number -= quotient * equalityTable[key];
  }

  return result;
};

document.querySelector("form").onsubmit = handleSubmit;
