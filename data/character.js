const char_name = window.location.pathname.split('/').filter(Boolean).pop();

async function loadJSON(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Ошибка: ${response.status}`);
        const data = await response.json();
        const char = data[char_name]
        console.log(char);

        document.getElementById("bg").appendChild(
            Object.assign(document.createElement("video"), {
                src: `../../data/${(char.en.element).toLowerCase()}_bg.webm`,
                autoplay: true,
                loop: true,
                muted: true 
            })
        );

        const container = document.querySelector('.container');
        container.style.setProperty('padding-top', '50px', 'important');

        const char_element = document.querySelector('.character-prof-element');
        char_element.src = `../../data/${(char.ru.element).toLowerCase()}.png`

        function getBG(num) {return num === 5 ? "linear-gradient(45deg, #FFD700, #FFAA00, #FF8000, #FF4500)" : "linear-gradient(45deg, #8A2BE2, #7A3FF3, #9B59B6, #8B00FF)";}          
        const char_icon = document.querySelector('.character-prof-icon');
        char_icon.src = `../../data/characters/${char_name}/${char_name}_icon.webp`
        char_icon.style.setProperty('background', getBG(char.ru.rarity));

        const char_prof_name = document.querySelector('.character-prof-name');
        char_prof_name.textContent = char.ru.name_ru

        const getStars = rating => "★".repeat(rating);
        const char_rarity = document.querySelector('.character-prof-rarity');
        char_rarity.textContent = getStars(char.ru.rarity)

        const char_detail = document.querySelector('.detail');
        char_detail.textContent = char.ru.more.detail

        const char_gacha = document.querySelector('.character-prof-gacha');
        char_gacha.src = `${char_name}_gacha.webp`
    } catch (error) {
        console.error('Ошибка загрузки JSON:', error);
    }
}

loadJSON(`../${char_name}/${char_name}.json`); // Заменить на нужный URL

document.addEventListener('scroll', function() {
    const gachaImage = document.querySelector('.character-prof-gacha');
    const lPage = document.querySelector('.page');
    const gachaImageRect = gachaImage.getBoundingClientRect();
    const lPageRect = lPage.getBoundingClientRect();
    
    // Определяем, когда изображение начинает пересекаться с .l-page
    if (gachaImageRect.top < lPageRect.bottom) {
      // Вычисляем, насколько изображение пересекается с .l-page
      const overlap = Math.min(gachaImageRect.bottom - lPageRect.top, gachaImageRect.height);
      const percentage = (overlap / gachaImageRect.height) * 100;
  
      // Применяем clip-path, чтобы скрыть часть изображения
      gachaImage.style.clipPath = `inset(0 0 ${percentage}% 0)`;
    } else if (gachaImageRect.bottom <= lPageRect.top) {
      // Если изображение полностью за элементом .l-page, скрываем его полностью
      //gachaImage.style.clipPath = 'inset(0 0 100% 0)';
    } else {
      // Если изображение полностью видимо, сбрасываем clip-path
      gachaImage.style.clipPath = 'inset(0 0 0 0)';
    }
  });