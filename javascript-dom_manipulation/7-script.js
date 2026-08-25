fetch("https://swapi-api.hbtn.io/api/films/?format=json")
	.then(response => response.json())
	.then(data => {
		const list_movies = document.querySelector('#list_movies');
		data.results.forEach(movieData => {
			const movie = document.createElement("li");
			movie.textContent = movieData.title;
			list_movies.appendChild(movie);
		})
	})
