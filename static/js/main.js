function appendToElement(elementToExtend, textToAppend) {
            let fakeDiv = document.createElement('div');
            fakeDiv.innerHTML = textToAppend.trim();
            elementToExtend.appendChild(fakeDiv.firstChild);
            return elementToExtend.lastChild;}


$(document).ready(function () {
        var buttons = document.getElementsByClassName('resident');
        for (let button of buttons){
            button.addEventListener('click', function () {
                var modalBody = `
                <tbody>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>`
            })
        }
        debugger;
});

function getResidents() {
    $.ajax({
    dataType: "json",
    url: 'https://api.github.com/repos/atom/atom',
    success: function(response) {
        console.log(response['stargazers_count'])
    }
})

}

/*$.ajax({
    dataType: "json",
    url: 'https://api.github.com/repos/atom/atom',
    success: function(response) {
        console.log(response['stargazers_count'])
    }
});*/

