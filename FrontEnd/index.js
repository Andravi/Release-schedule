console.log('Anime Shedule');

let animeCards = document.querySelector('.Anime-list');

fetch('../weekAnimeDays.json')
    .then(response => response.json())
    .then(animeList => animeList
        .forEach((anime, index) => {

    let animeCard = document.createElement('div');
    animeCard.classList.add('Anime-card')
    animeCards.appendChild(animeCard);

    animeCard.innerHTML = `
    <h1 id="title">${anime['nome']}</h1>
    <img src="${anime['image']}" alt="Teste">
    <h3>${anime['time']['dia']} às ${anime['time']['horas']} </h3>
    `;
}));



var ul = document.getElementById('menu_left').children[0];  // Parent
console.log(ul)

ul.addEventListener('click', function(e) {
    if (e.target.tagName === "LI"){
        // TODO -> Fazer uma verificação para cade um para filtrar 
        alert(e.target.innerHTML)
    }
    
});

