const form = document.querySelector("form");
const searchInput = document.querySelector("#search-input");
const table = document.querySelector("#table");
const figure = document.querySelector("#figure");

const format = (str) => {
  const regex = /[^a-zA-Z0-9\-]/g;
  return str
    .replace(regex, (match) => {
      if (match === "♂") {
        return "m";
      } else if (match === "♀") {
        return "f";
      } else {
        return "";
      }
    })
    .toLowerCase();
};

form.onsubmit = (e) => {
  e.preventDefault();
  const formatted = format(searchInput.value);
  console.log(formatted);
  fetch(`https://pokeapi-proxy.freecodecamp.rocks/api/pokemon/${formatted}`)
    .then((res) => res.json())
    .then((data) => {
      updateUI(data);
      console.log(data);
    })
    .catch((err) => alert("Pokémon not found"));
  console.log(formatted);
};

const updateUI = (data) => {
  figure.innerHTML = `
      <img id="sprite" src="${data.sprites.front_default}" alt=""/>
      <div id="nameid">
        <p id="pokemon-name">${data.name.toUpperCase()}</p>
        <p id="pokemon-id">#${data.id}</p>
      </div>
      <p id="weight">Weight: ${data.weight}</p>
      <p id="height">Height: ${data.height}</p>
      <div id="types">
        ${data.types
          .map((el) => `<p>${el.type.name.toUpperCase()}</p>`)
          .join("")}
      </div>
  `;
  table.innerHTML = `
        <thead>
          <tr>
            <th>Attributes</th>
            <th>Stats</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>HP:</td>
            <td id="hp">${data.stats[0].base_stat}</td>
          </tr>
          <tr>
            <td>Attack:</td>
            <td id="attack">${data.stats[1].base_stat}</td>
          </tr>
          <tr>
            <td>Defense:</td>
            <td id="defense">${data.stats[2].base_stat}</td>
          </tr>
          <tr>
            <td>Sp.Attack:</td>
            <td id="special-attack">${data.stats[3].base_stat}</td>
          </tr>
          <tr>
            <td>Sp.Defense:</td>
            <td id="special-defense">${data.stats[4].base_stat}</td>
          </tr>
          <tr>
            <td>Speed:</td>
            <td id="speed">${data.stats[5].base_stat}</td>
          </tr>
        </tbody>
  `;
};
