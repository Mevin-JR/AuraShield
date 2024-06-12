window.addEventListener('load', () => {
    const loader = document.querySelector(".loader");
    loader.classList.add('loader-hidden');
    loader.addEventListener('transitionend', () => {
        document.body.removeChild("loader");
    });
});

const navbar = document.getElementById("navbar");
const contactBtn = document.getElementById("contact-btn");
const hamburgerIcon = document.getElementById('hamburger-icon');

window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        navbar.style.backgroundColor = 'black';
        contactBtn.classList.add('btn-outline-light');
        contactBtn.classList.add('text-light')
    } else {
        navbar.style.backgroundColor = 'transparent';
        contactBtn.classList.remove('btn-outline-light');
        contactBtn.classList.remove('text-light')
    }
});

hamburgerIcon.addEventListener('click', () => {
    if (navbar.style.backgroundColor !== 'black') {
        navbar.style.backgroundColor = 'black';
    }
});