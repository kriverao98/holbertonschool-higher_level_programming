const toggle_header = document.getElementById("toggle_header");
const header = document.querySelector("header");

if (toggle_header) {
	toggle_header.addEventListener("click", function() {
		if (!header.classList.contains("red") && !header.classList.contains("green")) {
			document.querySelector("header").classList.add("red");
		}
		else if (header.classList.contains("red")) {
			document.querySelector("header").classList.remove("red");
			document.querySelector("header").classList.add("green");
		}
		else {
			document.querySelector("header").classList.remove("green");
			document.querySelector("header").classList.add("red");
		}
	});
};