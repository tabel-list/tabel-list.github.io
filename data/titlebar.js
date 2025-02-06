function toggleMenu() {
    let menu = document.getElementById('menu');
    let button = document.querySelector('.menu-button');
    let overlay = document.getElementById('overlay');
    let body = document.body;

    menu.classList.toggle('active');
    button.classList.toggle('active');
    overlay.classList.toggle('active');

    if (menu.classList.contains('active')) {
        body.classList.toggle('no-scroll');
    } else {
        body.classList.remove('no-scroll');
    }
}

document.addEventListener('click', function(event) {
    let menu = document.getElementById('menu');
    let button = document.querySelector('.menu-button');
    let overlay = document.getElementById('overlay');
    let body = document.body;

    if (!menu.contains(event.target) && !button.contains(event.target)) {
        menu.classList.remove('active');
        button.classList.remove('active');
        overlay.classList.remove('active');
        body.classList.remove('no-scroll');
    }
});