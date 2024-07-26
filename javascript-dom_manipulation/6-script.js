const character = document.getElementById("character");
const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

if (character) {
	fetch(url)
	.then(response => response.json())
	.then(data => {
		const characterName = data.name;
		character.textContent = characterName;
	});
};