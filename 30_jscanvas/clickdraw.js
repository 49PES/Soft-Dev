var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if(mode == "rect"){
        mode = "circle"
    }
    else{
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.fillRect(mouseX, mouseY, 30, 70);

    console.log("mouseclick registered at ", mouseX, mouseY);
}

var drawCircle = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;

    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.strokeStyle = "black";
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
}

var draw = (e) => {
    if(mode == "rect"){
        return drawRect(e);
    }
    else if(mode == "circle"){
        return drawCircle(e);
    }
}

var wipeCanvas = function(){
    clearRect(0, 0, 600, 600);
}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);