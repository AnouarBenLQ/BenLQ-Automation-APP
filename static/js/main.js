document.addEventListener('alpine:init', () => {
    Alpine.data('myComponent', () => ({
        openForm: false,
        openForm2: false,
        
        get isOpen() {
            return this.openForm;
        },
        set isOpen(open){
            this.openForm = open;
        },
        
    }));

    let isModalLoaded = false; // Track whether the modal content has been loaded

    htmx.on("htmx:afterSwap", (event) => {
        // Check if the target element is the modal containing the form
        if (event.detail.target.id === "formModal") {
            isModalLoaded = true;
            
            console.log(isModalLoaded);
             // Set the flag to indicate that the modal content is loaded
            
            
        }
    });

    function toggleModal() {
        if (!isModalLoaded) {
            
            return htmx.trigger("#buttonToLoadModal", "click");
        }
        else {
            openForm=true;
        }
       
    }
});
