const header = document.querySelector('header');
const button = document.querySelector('#red_header');
function onclick () {
  header.style.color = 'red';
}
button.addEventListener('click', onclick);
