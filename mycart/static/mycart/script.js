document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('.quantity-input');
    const totalElement = document.querySelector('#total');

    function updateTotals() {
        let total = 0;
        inputs.forEach(input => {
            const quantity = parseFloat(input.value) || 0;
            const price = parseFloat(input.dataset.price) || 0;
            const lineTotal = quantity * price;
            total += lineTotal;
            const lineTotalElement = input.closest('#input-page').querySelector('.line-total');
            lineTotalElement.textContent = `${lineTotal.toFixed(2)} AED`;
        });
        totalElement.textContent = `${total.toFixed(2)} AED`;
    }

    inputs.forEach(input => {
        input.addEventListener('change', updateTotals);
    });
    updateTotals();

    const messagesContainer = document.getElementById('messages');
    if (messagesContainer) {
        setTimeout(() => { // Fade out the messages after 4 seconds
            messagesContainer.classList.add('opacity-0');
            setTimeout(() => {
                messagesContainer.remove();
            }, 500);
        }, 4000);
    }
});
