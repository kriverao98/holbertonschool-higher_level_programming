const red_header = document.getElementById("red_header");
if (red_header) {
  red_header.addEventListener("click", function() {
	document.querySelector("header").classList.add("red");
  });
}