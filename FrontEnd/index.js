console.log('Anime Shedule');

let animeCards = document.querySelector('.Anime-list');

showList()


function clearChildres(classe) {
    const animeList = document.getElementsByClassName(classe)[0];
    animeList.textContent = '';
}

function showList(day) {
    if (day) {
        fetch('../weekAnimeDays.json')
            .then(response => response.json())
            .then(animeList => animeList
                .forEach((anime, index) => {
                    if (anime['time']['dia'] == day) {
                        let animeCard = document.createElement('div');
                        animeCard.classList.add('Anime-card')
                        animeCards.appendChild(animeCard);

                        animeCard.innerHTML = `
                    <h1 id="title">${anime['nome']}</h1>
                    <img src="${anime['image']}" alt="Teste">
                    <h3>${anime['time']['dia']} às ${anime['time']['horas']} </h3>
                    `;
                    }
                }));
    } else {
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
    }


}


var ul = document.getElementById('menu_left').children[0];  // Parent
console.log(ul)

ul.addEventListener('click', function (e) {
    if (e.target.tagName === "LI") {
        clearChildres("Anime-list")
        showList(e.target.innerHTML + "s")
    }

});

