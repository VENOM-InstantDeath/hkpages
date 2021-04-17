var qone = 0;
var qtwo = 0;

document.getElementById("beqone").addEventListener("click", function(){document.getElementById("qone").innerHTML = " Correcto"});
document.getElementById("bsqone").addEventListener("click", function(){document.getElementById("qone").innerHTML = " Incorrecto"});
document.getElementById("beqtwo").addEventListener("click", function(){document.getElementById("qtwo").innerHTML = " Incorrecto"});
document.getElementById("bsqtwo").addEventListener("click", function(){document.getElementById("qtwo").innerHTML = " Correcto"});
document.getElementById("beqthree").addEventListener("click", function(){document.getElementById("qthree").innerHTML = " Incorrecto"});
document.getElementById("bsqthree").addEventListener("click", function(){document.getElementById("qthree").innerHTML = " Correcto"});
document.getElementById("prev").addEventListener("click", function() {window.location.replace('index.html')});
document.getElementById("next").addEventListener("click", function() {window.location.replace('py2.html')});
