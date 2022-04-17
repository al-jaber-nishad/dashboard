// Toogle Button 
let btn = document.querySelector("#toggle-btn");
let sideBar = document.querySelector(".sidebar");

btn.onclick = function(){
  sideBar.classList.toggle("inactive");
}