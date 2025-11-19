const images = document.querySelectorAll('.slider-img');
const texts = document.querySelectorAll('.over');
const controls = document.querySelectorAll('.controls');
let currentIndex = 0;

function showSlide(index) {
    images.forEach(img => img.classList.remove('active'));
    texts.forEach(txt => txt.classList.remove('actives'));
    images[index].classList.add('active');
    texts[index].classList.add('actives');
    currentIndex = index;
}
controls.forEach(control => {
    control.addEventListener('click', (event) => {
        let index;
        if (event.target.classList.contains('prev')) {
            index = currentIndex - 1;
            if (index < 0) index = images.length - 1;
        } else if (event.target.classList.contains('next')) {
            index = currentIndex + 1;
            if (index >= images.length) index = 0;
        }
        showSlide(index);
    });
});


setInterval(() => {
    let index = currentIndex + 1;
    if (index >= images.length) index = 0;
    showSlide(index);
}, 5000);

