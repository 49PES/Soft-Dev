// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky); // First, when you click on a <td> item, it triggers an alert for just that one Star Wars character
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky); // Second, an alert is given with all of the Star War characters in that row
}

table.addEventListener('click', clicky); // Third, an alert is given with the entire table 


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// Element, Row, Full Table (In sequential order of the for loops)
