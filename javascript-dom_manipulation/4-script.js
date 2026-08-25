const my_list = document.querySelector(".my_list");
const button = document.querySelector("#add_item");
function onclick() {
  const new_item = document.createElement("li");
  new_item.textContent = "Item";
  my_list.appendChild(new_item);
}
button.addEventListener("click", onclick);
