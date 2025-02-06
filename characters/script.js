import { charactersList } from "./data.js";

const filterToggleButton = document.getElementById('filters-toggle-button');
const filters = document.querySelector('.filters');
const overlay = document.getElementById('overlay2');

// Функция для проверки, вверху ли страницы
function isAtTop() {
    return window.scrollY === 0;
}

// Функция для открытия/закрытия фильтра
function toggleFilter() {
    filters.classList.toggle('open');
    overlay.classList.toggle('active');
    
    // Когда фильтр открыт, скрываем кнопку для открытия, когда закрыт — показываем
    if (filters.classList.contains('open')) {
        filters.classList.remove('hidden');
        filterToggleButton.classList.remove('show');
    } else {
        filters.classList.add('hidden');
        filterToggleButton.classList.add('show');
    }
}

// Обработчик клика по кнопке для открытия/закрытия фильтра
filterToggleButton.addEventListener('click', function(event) {
    // Предотвратить всплытие события (клик на кнопке не должен закрывать фильтр)
    event.stopPropagation();
    toggleFilter();
});

// Обработчик клика вне фильтра для его закрытия
document.addEventListener('click', function(event) {
    // Проверяем, был ли клик за пределами фильтра и кнопки
    if (!filters.contains(event.target) && !filterToggleButton.contains(event.target)) {
        if (filters.classList.contains('open')) {
            toggleFilter();
        }
    }
});

// Слушаем прокрутку страницы для скрытия/показа фильтра
window.addEventListener('scroll', function() {
    if (isAtTop()) {
        // Когда находимся на верхней части страницы, показываем фильтр
        filters.classList.remove('hidden');
        filterToggleButton.classList.remove('show');
    } else {
        // Когда прокручиваем вниз, скрываем фильтр и показываем кнопку
        filters.classList.add('hidden');
        filters.classList.remove('open');
        filterToggleButton.classList.add('show');
        overlay.classList.remove('active');
    }
});

// Установка lazy-loading для изображений
document.querySelectorAll("img").forEach(img => img.setAttribute("loading", "lazy"));

document.addEventListener("DOMContentLoaded", function () {
    const getStars = rating => "★".repeat(rating);

    // Преобразуем все данные при инициализации, чтобы избежать лишних вычислений при рендере
    const characters = charactersList.map(char => ({
        ...char,
        name_lower: char.name.toLowerCase(),
        name_ru_lower: char.name_ru.toLowerCase(),
    })).sort((a, b) => b.rarity - a.rarity || b.id - a.id);

    const charactersContainer = document.getElementById("characters-list");
    const searchInput = document.getElementById("search");
    const sortElement = document.getElementById("sort-element");
    const sortWeapon = document.getElementById("sort-weapon");
    const sortRarity = document.getElementById("sort-rarity");

    // Функция для создания карточки персонажа
    const createCharacterCard = character => `
        <a class="character-card" href="../character/${encodeURIComponent(character.name)}">
            <div class="namecard" style="background-image: url(../data/characters/${encodeURIComponent(character.name)}/${encodeURIComponent(character.name)}_namecard.webp);">
                <img class="character-icon" src="../data/characters/${encodeURIComponent(character.name)}/${encodeURIComponent(character.name)}_icon.webp">
                <img class="character-element" src="../data/${encodeURIComponent(character.element).toLowerCase()}.png">
                <img class="character-weapon" src="../data/${encodeURIComponent(character.weapon).toLowerCase()}.png">
            </div>
            <div class="bottom-namecard">
                <span class="character-name">${character.name_ru}</span>
                <span class="character-rarity">${getStars(character.rarity)}</span>
            </div>
        </a>
    `;

    // Функция рендеринга персонажей
    const renderCharacters = () => {
        const searchQuery = searchInput.value.toLowerCase();
        const elementFilter = sortElement.value;
        const weaponFilter = sortWeapon.value;
        const rarityFilter = sortRarity.value;

        // Фильтрация персонажей
        const filteredCharacters = characters.filter(character =>
            (searchQuery === "" || character.name_lower.includes(searchQuery) || character.name_ru_lower.includes(searchQuery)) &&
            (elementFilter === "" || character.element == elementFilter || character.element === "None") &&
            (weaponFilter === "" || character.weapon === weaponFilter) &&
            (rarityFilter === "" || character.rarity.toString() === rarityFilter)
        );

        // Создание всех карточек и добавление их в контейнер
        const cardsHTML = filteredCharacters.map(createCharacterCard).join('');
        charactersContainer.innerHTML = cardsHTML;
    };

    // Дебаунс для оптимизации поиска
    const debounce = (func, delay) => {
        let timeout;
        return (...args) => {
            clearTimeout(timeout);
            timeout = setTimeout(() => func(...args), delay);
        };
    };

    const debouncedRenderCharacters = debounce(renderCharacters, 150);

    // Добавляем обработчики событий
    searchInput.addEventListener("input", debouncedRenderCharacters);
    sortElement.addEventListener("change", renderCharacters);
    sortWeapon.addEventListener("change", renderCharacters);
    sortRarity.addEventListener("change", renderCharacters);

    renderCharacters();  // Первый рендер
});
