var modo = document.querySelector(".mode");
var btn = document.querySelector("#modo");

function setBtn(){
  if(localStorage.getItem("modo") == "Dark"){
    btn.textContent = "Light";
  }else{
    btn.textContent = "Dark"
  }
}

function setModo(value){
  localStorage.setItem("modo", value);
  modo.class=localStorage.getItem("modo");
  modo.className = localStorage.getItem("modo");
  if(localStorage.getItem("modo") == "Dark"){
    btn.textContent = "Light";
  }
  if(localStorage.getItem("modo") == "Light"){
    btn.textContent = "Dark"
  }
}

modo.className = localStorage.getItem("modo");