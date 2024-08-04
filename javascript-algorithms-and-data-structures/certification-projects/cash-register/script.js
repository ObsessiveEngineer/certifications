const cidUl = document.querySelector("#cid");
const cashInput = document.querySelector("#cash");
const changeDue = document.querySelector("#change-due");
const priceParaf = document.querySelector("#price");
const statusParaf = document.querySelector("#status");
const form = document.querySelector("form");

let price = 22.22;
let cid = [
  ["ONE HUNDRED", 100],
  ["TWENTY", 60],
  ["TEN", 20],
  ["FIVE", 55],
  ["ONE", 90],
  ["QUARTER", 4.25],
  ["DIME", 3.1],
  ["NICKEL", 2.05],
  ["PENNY", 1.01],
];
let cashUnits = {
  "ONE HUNDRED": 100,
  TWENTY: 20,
  TEN: 10,
  FIVE: 5,
  ONE: 1,
  QUARTER: 0.25,
  DIME: 0.1,
  NICKEL: 0.05,
  PENNY: 0.01,
};

const totalCID = (cid) => {
  return cid.reduce((acc, cash) => acc + cash[1], 0);
};

const renderCID = (cid) => {
  priceParaf.innerText = "Total: $" + price;
  cidUl.innerHTML = "";
  cidUl.innerHTML = cid
    .map((cash) => `<li>${cash[0]}: $${cash[1]}</li>`)
    .join("");
};

const renderChange = (cdl, status) => {
  changeDue.innerHTML =
    `<p>${status}</p>` +
    cdl.map((cash) => `<p>${cash[0]}: $${cash[1]}</p>`).join("");
};

form.onsubmit = (e) => {
  e.preventDefault();
  const cash = parseFloat(cashInput.value);
  if (cash < price) {
    alert("Customer does not have enough money to purchase the item");
    return;
  }
  if (cash === price) {
    changeDue.innerText = "No change due - customer paid with exact cash";
    return;
  }
  const [change, cashInRegister, changeDueList] = checkout(
    cid,
    cashUnits,
    cash - price
  );
  changey(change, cashInRegister, changeDueList);
  renderCID(cid);
  cashInput.value = "";
};

const checkout = (cid, units, change) => {
  const cashInRegister = JSON.parse(JSON.stringify(cid));
  const changeDueList = [];
  cashInRegister.forEach((cash, i) => {
    while (cash[1] > 0 && change > 0 && change >= units[cash[0]]) {
      cash[1] = Number((cash[1] - units[cash[0]]).toFixed(2));
      change = Number((change - units[cash[0]]).toFixed(2));
      if (!changeDueList[i]) {
        changeDueList[i] = [cash[0], Number(units[cash[0]].toFixed(2))];
      } else {
        changeDueList[i][1] += Number(units[cash[0]].toFixed(2));
      }
    }
  });

  return [
    change,
    cashInRegister,
    changeDueList.map((el) => [el[0], Number(el[1].toFixed(2))]),
  ];
};

const changey = (change, cashInRegister, changeDueList) => {
  if (change) {
    changeDue.innerHTML = "Status: INSUFFICIENT_FUNDS";
    return;
  } else if (change === totalCID(cashInRegister)) {
    renderChange(changeDueList, "Status: CLOSED");
  } else {
    renderChange(changeDueList, "Status: OPEN");
  }
  cid = Array.from(cashInRegister);
};

renderCID(cid);
