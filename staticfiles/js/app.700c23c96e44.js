const ham=document.querySelector('.hamburger')
const menu=document.querySelector('.nav-ul')
ham.addEventListener("click",Mobile)
function Mobile()
{
    ham.classList.toggle("active")
    menu.classList.toggle("active")
}
const navLink = document.querySelectorAll(".nav-link");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    ham.classList.remove("active");
    menu.classList.remove("active");
}