document.addEventListener("DOMContentLoaded", function () {
  // Capture form submission event

  function handleFormTwoData() {
    console.log("Wrath of Cobly");
    var commercialSelect = document.getElementById("id_commercial");
    var commercialValue =
      commercialSelect.options[commercialSelect.selectedIndex].text;

    var paymentSelect = document.getElementById("id_moyen_de_paiement");
    var paymentValue = paymentSelect.options[paymentSelect.selectedIndex].text;

    var adresseValue = document.getElementById("id_adresse_de_livraison").value;
    var commissionValue = document.getElementById("id_commission_pourcentage").value;
    var noteValue = document.getElementById("id_note").value;

    document.getElementById("commercial").innerText = commercialValue;
    document.getElementById("payment").innerText = paymentValue;
    document.getElementById("adresse").innerText = adresseValue;
    document.getElementById("commission").innerText = commissionValue;
    document.getElementById("note").innerText = noteValue;
  }
  function handleFormData() {
    var clientSelect = document.getElementById("id_client");
    var clientValue = clientSelect.options[clientSelect.selectedIndex].text;

    var AccoutantSelect = document.getElementById("id_suivi_par");
    var suiviParValue =
      AccoutantSelect.options[AccoutantSelect.selectedIndex].text;

    //var clientValue = document.getElementById("id_client").value;
    var dateValue = document.getElementById("id_date").value;
    var echeanceValue = document.getElementById("id_echeance").value;
    var numeroValue = document.getElementById("id_numero").value;
    var referenceValue = document.getElementById("id_reference").value;
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
});
