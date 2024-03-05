document.addEventListener('DOMContentLoaded', function() {
    var messagesElement = document.getElementById('messages');

    // Check if the messages element exists and contains a message
    if (messagesElement && messagesElement.children.length > 0) {
      // Set a timeout to hide the message after 5000 milliseconds (adjust as needed)
      setTimeout(function() {
        // Remove the message element or hide it
        messagesElement.innerHTML = '';
      }, 5000);
    }
  });
  function submitLogoutForm() {
    document.getElementById('logout-form').submit();
  };