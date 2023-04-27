// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // A click will only register an event with the highest priority

  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)


// According to the MDN documentation, 
// the boolean value "capture" given in the event listener indicates that events of this type 
// will be dispatched to the registered listener before being dispatched to any ** EventTarget beneath it in the DOM Tree **

// Based on uncommenting the lines with true / false capture booleans, we see that the events with true are given higher priority than those with false, and then events that have a higher priority in the DOM happen earlier

// e.g. if all are given true, then table -> row -> cell

// if table is given false, row -> cell -> table

// if row is given false, table -> cell -> row

// if cell is given false, the default of table -> row -> cell occurs

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  // tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  // trs[x].addEventListener('click', clicky, false);
}

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);
