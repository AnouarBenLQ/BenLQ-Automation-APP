document.addEventListener('alpine:init', () => {
    Alpine.data('priceCalculator', () => ({
        
        init() {
            console.log("Hallo Welt");
            this.calculateTotals();

            // Listen for HTMX's afterSwap event to recalculate totals when new rows are added
            document.body.addEventListener('htmx:afterSwap', (event) => {
                const swappedContent = event.detail.target;
                //console.log(event.detail.target.id)
                if (event.detail.target.id === 'invoice-listing') { {
                console.log("Row Fetched !")
                console.log(swappedContent);
                this.calculateTotals();
                }}
            });
        },
        calculateTotals() {
this.$nextTick(() => {
    document.querySelectorAll('#invoice-listing .myUniqueClass').forEach((row) => {
        const quantity = parseFloat(row.querySelector('.quantity').value) || 0;
        const price_ht = parseFloat(row.querySelector('.price_ht').value) || 0;
        const price_ttc = parseFloat(row.querySelector('.price_ttc').value) || 0;
        
        const total_ht = quantity * price_ht;
        const total_ttc = quantity * price_ttc;

        row.querySelector('.total_ht').value = total_ht.toFixed(2);
        row.querySelector('.total_ttc').value = total_ttc.toFixed(2);
    });
});
}
    }));
});