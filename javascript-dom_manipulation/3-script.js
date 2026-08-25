const header = document.querySelector("header");
const button = document.querySelector("#toggle_header");
function onclick() {
	if (header.classList.contains("red")) {
		header.classList.replace("red", "green");
	} else {
		header.classList.replace("green", "red");
	}
}
button.addEventListener("click", onclick);
