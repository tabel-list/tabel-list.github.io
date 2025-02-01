document.addEventListener("DOMContentLoaded", function() {
    const menuButton = document.querySelector(".menu-button");
    const dropdownMenu = document.querySelector(".dropdown-menu");
    
    menuButton.addEventListener("click", function(event) {
        menuButton.classList.toggle("active");
        dropdownMenu.classList.toggle("active");
        event.stopPropagation();
    });
    
    document.addEventListener("click", function(event) {
        if (!dropdownMenu.contains(event.target) && !menuButton.contains(event.target)) {
            dropdownMenu.classList.remove("active");
            menuButton.classList.remove("active");
        }
    });

    const charactersList = [
        { name: "Amber", name_ru: "Эмбер", rarity: 4, weapon: "Bow", element: "Pyro" },
        { name: "Xianyun", name_ru: "Сянь Юнь", rarity: 5, weapon: "Catalyst", element: "Anemo" },
        { name: "Charlotte", name_ru: "Шарлотта", rarity: 4, weapon: "Catalyst", element: "Cryo" }
    ];

    const charactersContainer = document.getElementById("characters-list");
    const searchInput = document.getElementById("search");
    const sortElement = document.getElementById("sort-element");
    const sortWeapon = document.getElementById("sort-weapon");
    const sortRarity = document.getElementById("sort-rarity");

    function renderCharacters() {
        charactersContainer.innerHTML = "";
        let filteredCharacters = charactersList.filter(character => {
            return (
                (searchInput.value === "" || character.name.toLowerCase().includes(searchInput.value.toLowerCase()) || character.name_ru.toLowerCase().includes(searchInput.value.toLowerCase())) &&
                (sortElement.value === "" || character.element === sortElement.value) &&
                (sortWeapon.value === "" || character.weapon === sortWeapon.value) &&
                (sortRarity.value === "" || character.rarity.toString() === sortRarity.value)
            );
        });
        
        filteredCharacters.forEach(character => {
            const characterCard = document.createElement("div");
            characterCard.classList.add("character-card");
            characterCard.innerHTML = `
                <img src="images/${character.name.toLowerCase()}.png" alt="${character.name_ru}">
                <h3>${character.name_ru}</h3>
                <p>Редкость: ${character.rarity}★</p>
                <p>Оружие: ${character.weapon}</p>
                <p>Элемент: ${character.element}</p>
            `;
            charactersContainer.appendChild(characterCard);
        });
    }

    searchInput.addEventListener("input", renderCharacters);
    sortElement.addEventListener("change", renderCharacters);
    sortWeapon.addEventListener("change", renderCharacters);
    sortRarity.addEventListener("change", renderCharacters);

    renderCharacters();
});