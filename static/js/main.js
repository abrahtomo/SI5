function addButton() {
    var lastCells = document.getElementsByClassName('residents');

    for (let i=0; i<lastCells.length; i++) {
        var button = "<button class=\"btn btn-outline-secondary\" role=\"button\" data-toggle=\"modal\" data-target=\"#myModal\">"+lastCells[i].innerHTML+"</button>";
        if (lastCells[i].innerHTML !== 'No known residents') {
            lastCells[i].innerHTML=button;
        }
    }
}

addButton();