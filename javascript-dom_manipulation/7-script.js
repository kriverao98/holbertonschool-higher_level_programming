const list_movies = document.getElementById("list_movies");
const url = "https://swapi-api.hbtn.io/api/films/?format=json";

if (list_movies) {
	fetch(url)
		.then(response => response.json())
		.then(data => {
			const movies = data.results;
			const movieList = movies.map(movie => `<li>${movie.title}</li>`).join("");
			list_movies.innerHTML = movieList;
		});
}