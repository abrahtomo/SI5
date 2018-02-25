function appendToElement(elementToExtend, textToAppend) {
            let fakeDiv = document.createElement('div');
            fakeDiv.innerHTML = textToAppend.trim();
            elementToExtend.appendChild(fakeDiv.firstChild);
            return elementToExtend.lastChild;}


$(document).ready(function () {
        var buttons = document.getElementsByClassName('residents');
        for (let button of buttons){
            button.addEventListener('click', function () {
                let myModal = document.getElementById("modalbody");
                myModal.innerHTML = '';
                var url = JSON.parse(button.getAttribute("value"));
                for(let resident of url){
                $.ajax({
                    dataType: "json",
                    url: resident,
                    success: function(response) {


                var modalBody = `
                <tbody>
                <tr>
                    <td>` + response['name'] + `</td>
                    <td>` + response['height'] +`</td>
                    <td>` + response['mass'] + `</td>
                    <td>` + response['hair_colour'] + `</td>
                    <td>` + response['skin_color'] + `</td>
                    <td>` + response['eye_color'] + `</td>
                    <td>` + response['birth_year'] + `</td>
                    <td>` + response['gender'] + `</td>
                </tr>
            </tbody>`;
            appendToElement(document.getElementById("modalbody"), modalBody)}})}})}});


