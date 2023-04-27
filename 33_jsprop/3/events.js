// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  e.stopPropagation(); // It'll only listen to an event once (the click) and perform the action with the highest priority
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?

// The eventListeners with true are given a priority - making table.addEventListener with true makes it appear first, and making it false makes it appear last 

//   (Leave exactly 1 version uncommented to test...)

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, true);

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// Depends on the boolean parameter in addEventListener and the placement in the sequence 
// - if only the table.addEvent is given true, then the table will appear first, otherwise the <td> will appear first