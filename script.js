function toggleMenu() {
    let menu = document.getElementById('menu');
    let button = document.querySelector('.menu-button');
    menu.classList.toggle('active');
    button.classList.toggle('active');
}

document.addEventListener('click', function(event) {
    let menu = document.getElementById('menu');
    let button = document.querySelector('.menu-button');
    if (!menu.contains(event.target) && !button.contains(event.target)) {
        menu.classList.remove('active');
        button.classList.remove('active');
    }
});