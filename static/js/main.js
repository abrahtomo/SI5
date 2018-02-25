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
              
                
                <tr>
                    <td class="modaltd">${response['name']}</td>
                    <td class="modaltd">${response['height']}</td>
                    <td class="modaltd">${response['mass']}</td>
                    <td class="modaltd">${response['hair_color']}</td>
                    <td class="modaltd">${response['skin_color']}</td>
                    <td class="modaltd">${response['eye_color']}</td>
                    <td class="modaltd">${response['birth_year']}</td>
                    <td class="modaltd">${response['gender']}</td>
                </tr>
                
                `;
            appendToElement(document.getElementById("modalbody"), modalBody)}})}})}});


