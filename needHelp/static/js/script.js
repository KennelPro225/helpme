const button = document.querySelector("#menu-button");
const menu = document.querySelector("#menu");
const nav = document.querySelector("#navBar");
const logo = document.querySelector("#logo");
button.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});
window.addEventListener("scroll", () => {
  console.log(window.scrollY);
  nav.classList.toggle("bg-purple-900", window.scrollY > 12);
  logo.classList.toggle("text-white", window.scrollY > 12);
});

