// search-box open close js code
let navbar = document.querySelector(".navbar");
let searchBox = document.querySelector(".search-box .bx-search");
background_menu = document.getElementById("back_menu");
document.getElementById("back_menu").addEventListener("click", ocultar_menu);

function ocultar_menu() {
  background_menu.style.display = "none";
  navLinks.style.right = "-100%";

}
// let searchBoxCancel = document.querySelector(".search-box .bx-x");

searchBox.addEventListener("click", ()=>{
  navbar.classList.toggle("showInput");
  if(navbar.classList.contains("showInput")){
    searchBox.classList.replace("bx-search" ,"bx-x");
  }else {
    searchBox.classList.replace("bx-x" ,"bx-search");
  }
});

// sidebar open close js code
let navLinks = document.querySelector(".nav-links");
let menuOpenBtn = document.querySelector(".navbar .bx-menu");
let menuCloseBtn = document.querySelector(".nav-links .bx-x");
menuOpenBtn.onclick = function() {
navLinks.style.right = "0";
background_menu.style.display = "block";
}
menuCloseBtn.onclick = function() {
navLinks.style.right = "-100%";
}


// sidebar submenu open close js code
let htmlcssArrow = document.querySelector(".clip-menu");
htmlcssArrow.onclick = function() {
 navLinks.classList.toggle("show1");
}
let excursionArrow = document.querySelector(".clip-escursiones");
excursionArrow.onclick = function() {
 navLinks.classList.toggle("show2");
}
let casasArrow = document.querySelector(".clip-casascuba");
casasArrow.onclick = function() {
 navLinks.classList.toggle("show21");
}
let jsArrow = document.querySelector(".clip-menu-servicios");
jsArrow.onclick = function() {
 navLinks.classList.toggle("show3");
}
let trArrow = document.querySelector(".clip-menu-tramites");
trArrow.onclick = function() {
 navLinks.classList.toggle("show4");
}





