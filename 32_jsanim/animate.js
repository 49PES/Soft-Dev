// access canvas and buttons via DOM (update HTML source to align)

var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");
var requestId;
ctx.fillStyle = "cyan";

var radius = 0;
var growing = true;

var clear = function(e){
    // e.preventDefault(); // Stops the default action from happening
    ctx.clearRect(0, 0, 500, 500);
}

var drawDot = () => {
    clear();

    if (growing && radius+1 > maxRadius) {
        growing = false;
    } else if (!growing && radius-1 < 0) {
        growing = true;
    }

    if (growing) {
        radius++; 
    } else {
        radius--;
    }

    ctx.beginPath();
    ctx.arc(maxRadius, maxRadius, radius, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID)
}


var dvdLogoSetup = function(){
    window.cancelAnimationFrame(requestId);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * (500 - rectWidth));
    var rectY = Math.floor(Math.random() * (500 - rectHeight));

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function(){
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
        // ctx.drawImage(logo, rectX, re)

        if(rectX == 0 || rectX + width == 500){
            xVel *= -1;
        }
            
        if(rectY == 0 || rectY + height == 500){
            yVel *= -1;
        }
        
        rectX += xVel;
        rectY += yVel;

        requestId = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo();
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);