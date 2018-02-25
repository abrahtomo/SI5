function appendToElement(elementToExtend, textToAppend) {
            let fakeDiv = document.createElement('div');
            fakeDiv.innerHTML = textToAppend.trim();
            elementToExtend.appendChild(fakeDiv.firstChild);
            return elementToExtend.lastChild;}


$(document).ready(function () {
        var buttons = document.getElementsByClassName('residents');
        for (let button of buttons){
            button.addEventListener('click', function () {
                var url = JSON.parse(button.getAttribute("value"))[0];
                console.log(url);
                debugger;
                var modalBody = `
                <tbody>
                <tr>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>`
            appendToElement(document.getElementById("modalbody"), modalBody)})
        }

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

