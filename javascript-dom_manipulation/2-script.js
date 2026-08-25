const header = document.querySelector("header");
const button = document.querySelector("#red_header");
function onclick() {
  header.classList.add('red');
}
button.addEventListener("click", onclick);
