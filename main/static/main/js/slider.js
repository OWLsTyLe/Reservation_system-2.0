const images = document.querySelectorAll('.slider-img');
const controls = document.querySelectorAll('.controls');
let imagesIndex = 0;

function showImage(index) {
    images[imagesIndex].classList.remove('active');
    images[index].classList.add('active');
    imagesIndex = index;
}

controls.forEach((e) => {
    e.addEventListener('click', () => {
        if (event.target.classList.contains('prev')) {
            let index = imagesIndex - 1;

            if (index < 0) {
                index = images.length - 1;
            }
            showImage(index);
        } else if (event.target.classList.contains('next')) {
            let index = imagesIndex + 1;

            if (index >= images.length) {
                index = 0;
            }
            showImage(index);
        }
    })
})

showImage(imagesIndex);
