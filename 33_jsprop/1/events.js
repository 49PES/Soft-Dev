// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td'); // Collects all the HTML blocks with tag <td> (all the Star War characters)

var clicky = function(e) {
  alert( this.innerHTML ); // Creates an alert when a <td> block is clicked
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky); // Creates an event listener for all of the <td> blocks 
}
