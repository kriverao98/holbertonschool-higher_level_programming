document.addEventListener("DOMContentLoaded", () => {
	const hello = document.getElementById("hello");
	const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
	
	fetch(url)
		.then(response => response.json())
		.then(data => {
			const helloTranslation = data.hello;
			hello.innerHTML = helloTranslation;
		})
		.catch(error => {
			console.error("Error:", error);
		});
});