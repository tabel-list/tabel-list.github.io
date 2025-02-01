document.querySelectorAll("img").forEach(img => img.setAttribute("loading", "lazy"));

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

    function getStars(rating) {
        return "★".repeat(rating);
    }

    async function getData() {
        let response = await fetch('https://raw.githubusercontent.com/tabel-list/tabel-list.github.io/refs/heads/main/genshin_config.json');
        if (!response.ok) throw new Error(`Ошибка HTTP: ${response.status}`);
        return await response.json();
    }
    
    // Использование данных в другом месте
    getData().then(data => {
        const charactersList = data['charactersList'].sort((a, b) => b.rarity - a.rarity || b.id - a.id);

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
                const characterCard = document.createElement("a");
                characterCard.classList.add("character-card");
                characterCard.href = `../character/${character.name}`;
                characterCard.innerHTML = `
                    <div class="namecard" style="background-image: url(../data/characters/${encodeURIComponent(character.name)}/${encodeURIComponent(character.name)}_namecard.png);">
                        <img class="character-icon" src="../data/characters/${encodeURIComponent(character.name)}/${encodeURIComponent(character.name)}_icon.png">
                        <img class="character-element" src="../data/${encodeURIComponent(character.element)}.png">
                        <img class="character-weapon" src="../data/${encodeURIComponent(character.weapon)}.png">
                    </div>
                    <div class="bottom-namecard">
                        <span class="character-name">${character.name_ru}</span>
                        <span class="character-rarity">${getStars(character.rarity)}</span>
                    </div>
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
});