const urlParams = new URLSearchParams(window.location.search);
const genre = urlParams.get('type'); 


const cards = document.querySelectorAll('.card');
cards.forEach(card => {
    const categories = card.querySelector('.category').textContent.toLowerCase();
    if (!categories.includes(genre)) {
        card.style.display = 'none';
    } else {
        card.style.display = 'block';
    }
});
