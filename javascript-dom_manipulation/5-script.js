const update_header = document.getElementById("update_header");
if (update_header) {
	update_header.addEventListener("click", function() {
		update_header.textContent = "New Header!!!";	
	});
};