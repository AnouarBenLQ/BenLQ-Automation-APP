function saveFormData() {
    var form = document.getElementById('myForm');
    console.log("Rage");
    var formData = {};
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];
        var name = element.name;
        var value = element.value;
        if (name) {
            formData[name] = value;
        }
    }
    var clientSelect = form.elements['client'];
    var selectedOption = clientSelect.options[clientSelect.selectedIndex];
    var clientName = selectedOption.text; // Assuming the dropdown shows the client's name
    formData['clientName'] = clientName;

    var clientSelect = form.elements['suivi_par'];
    var selectedOption = clientSelect.options[clientSelect.selectedIndex];
    var AgentName = selectedOption.text; // Assuming the dropdown shows the client's name
    formData['agentName'] = AgentName;
    
    

    localStorage.setItem('formData', JSON.stringify(formData));
    console.log(localStorage.getItem('formData'));
    displayFormData();
}

function displayFormData() {
    var savedData = localStorage.getItem('formData');
    if (savedData) {
        var formData = JSON.parse(savedData);
        // Display the saved data on the main page
        // You need to have elements with these IDs on your main page
        document.getElementById('displayClient').textContent = formData.clientName || '----------';
        document.getElementById('displayDate').textContent = formData.date || '';
        document.getElementById('displayEcheance').textContent = formData.echeance || '';
        document.getElementById('displayNumero').textContent = formData.numero || '';
        // document.getElementById('displayReference').textContent = formData.reference || '';
        document.getElementById('displaySuiviPar').textContent = formData.agentName || '';
    }
}
function saveAndReload() {
    saveFormData();
    window.location.reload(); // Reload the page to reflect the changes
}

// Call displayFormData on the main page load
window.addEventListener('DOMContentLoaded', displayFormData);