function toggleMenu() {
    let menu = document.getElementById('menu');
    let button = document.querySelector('.menu-button');
    let overlay = document.getElementById('overlay');

    menu.classList.toggle('active');
    button.classList.toggle('active');
    overlay.classList.toggle('active');
}

document.addEventListener('click', function(event) {
    let menu = document.getElementById('menu');
    let button = document.querySelector('.menu-button');
    let overlay = document.getElementById('overlay');

    if (!menu.contains(event.target) && !button.contains(event.target)) {
        menu.classList.remove('active');
        button.classList.remove('active');
        overlay.classList.remove('active');
    }
});
