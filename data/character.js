const char_name = window.location.pathname.split('/').filter(Boolean).pop();

async function loadJSON(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Ошибка: ${response.status}`);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Ошибка загрузки JSON:', error);
    }
}

loadJSON(`../${char_name}/${char_name}.json`); // Заменить на нужный URL
