const header = document.querySelector('header');
const button = document.querySelector('#update_header');
function onclick () {
  header.textContent = 'New Header!!!';
}
button.addEventListener('click', onclick);
