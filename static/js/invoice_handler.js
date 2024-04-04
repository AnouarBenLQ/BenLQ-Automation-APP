document.addEventListener("DOMContentLoaded", function () {
  // Capture form submission event

  function handleFormTwoData() {
    console.log("Wrath of Cobly");
    var commercialSelect = document.getElementById("id_form2-commercial");
    var commercialValue =
      commercialSelect.options[commercialSelect.selectedIndex].text;

    var paymentSelect = document.getElementById("id_form2-moyen_de_paiement");
    var paymentValue = paymentSelect.options[paymentSelect.selectedIndex].text;

    var adresseValue = document.getElementById("id_form2-adresse_de_livraison").value;
    var commissionValue = document.getElementById("id_form2-commission_pourcentage").value;
    var noteValue = document.getElementById("id_form2-note").value;

    document.getElementById("commercial").innerText = commercialValue;
    document.getElementById("payment").innerText = paymentValue;
    document.getElementById("adresse").innerText = adresseValue;
    document.getElementById("commission").innerText = commissionValue;
    document.getElementById("note").innerText = noteValue;
  }
  function handleFormData() {
    var clientSelect = document.getElementById("id_form1-client");
    var clientValue = clientSelect.options[clientSelect.selectedIndex].text;

    var AccoutantSelect = document.getElementById("id_form1-suivi_par");
    var suiviParValue =
      AccoutantSelect.options[AccoutantSelect.selectedIndex].text;

    //var clientValue = document.getElementById("id_client").value;
    var dateValue = document.getElementById("id_form1-date").value;
    var echeanceValue = document.getElementById("id_form1-echeance").value;
    var numeroValue = document.getElementById("id_form1-numero").value;
    var referenceValue = document.getElementById("id_form1-reference").value;
    //var suiviParValue = document.getElementById("id_suivi_par").value;

    // Display input values on the main page or perform any other action
    document.getElementById("displayClient").innerText = clientValue;
    document.getElementById("displayDate").innerText = dateValue;
    document.getElementById("displayEcheance").innerText = echeanceValue;
    document.getElementById("displayNumero").innerText = numeroValue;
    //document.getElementById("displayReference").innerText = referenceValue;
    document.getElementById("displaySuiviPar").innerText = suiviParValue;
  }
  console.log("Wrath Of Chaos");
  
  document
    .getElementById("saleinfoForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      handleFormTwoData();
    });
  // Retrieve input values
 

  handleFormData();
  document
    .getElementById("myForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      handleFormData();
    });

   submitForms = function() {
    let form1 = document.getElementById("myForm");
    let form2 = document.getElementById("saleinfoForm");
    console.log("something", form1, form2);

    // Combine form data into a FormData object
    let formData = new FormData(form1);
    let formData2 = new FormData(form2);
    
    // Append form2 data to formData
    for (let [key, value] of formData2.entries()) {
        formData.append(key, value);
    }

    // Send combined form data to the server
    fetch(form1.action, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // or return response.text() if response is not JSON
    })
    .then(data => {
      if (data && data.data && data.data.redirect_url) {
        // Redirect to the URL
        window.location.href = data.data.redirect_url;
    }
    })
    // .catch((error) => {
    //     console.error('Error:', error);
    // });
};

      
 
 
});


  

