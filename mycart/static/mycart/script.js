document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.quantity-input');
    const totalElement = document.querySelector('#total');

    const updateTotals = () => {
        let total = 0;
        inputs.forEach(input => {
            const quantity = parseFloat(input.value) || 0;
            const pricePerKg = parseFloat(input.dataset.price);
            const lineTotal = input.parentElement.nextElementSibling.nextElementSibling;
            const lineAmount = quantity * pricePerKg;
            lineTotal.textContent = lineAmount.toFixed(2);
            total += lineAmount;
        });
        totalElement.textContent = total.toFixed(2);
    };

    inputs.forEach(input => {
        input.addEventListener('input', updateTotals);
    });
    updateTotals();

    const messagesContainer = document.getElementById('messages');
    if (messagesContainer) {
        setTimeout(() => {
            messagesContainer.classList.add('opacity-0');
            setTimeout(() => {
                messagesContainer.remove();
            }, 500);
        }, 4000);
    }
});

