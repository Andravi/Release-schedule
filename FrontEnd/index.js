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
                    if (anime['time']['dia'] == day) { // Mas quando é incerto ? // Tambem não aparecem o de temporadas antigas
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

async function  searchInList(name){
    // 
    await fetch('../weekAnimeDays.json')
            .then(response => response.json())
            .then(animeList => animeList
                .forEach((anime, index) => {
                    if (anime['nome'].toLowerCase().includes(name.toLowerCase())) { // Mas quando é incerto ? // Tambem não aparecem o de temporadas antigas
                        let animeCard = document.createElement('div');
                        animeCard.classList.add('Anime-card')
                        animeCards.appendChild(animeCard);
                        animeCard.innerHTML = `
                    <h1 id="title">${anime['nome']}</h1>
                    <img src="${anime['image']}" alt="Teste">
                    <h3>${anime['time']['dia']} às ${anime['time']['horas']} </h3>
                    `;
                    }
                }
                ));

    if (animeCards.children.length == 0){
        let info = document.createElement('div');
        animeCards.appendChild(info);
        info.innerHTML = `
        <h1 id="title" style="color: white; text-align: center">Nenhum resultado encontrado</h1>`;
    }
}





let ul = document.getElementById('menu_left').children[0];  // Parent BuscarBtn
let buscarBtn = document.getElementById('BuscarBtn');

ul.addEventListener('click', function (e) {
    if (e.target.tagName === "LI") {
        clearChildres("Anime-list")
        showList(e.target.innerHTML + "s")
    }

});

buscarBtn.addEventListener('click', function (e) {
    // Pegar valor da caixa de testo -> se não vazia -> pesquisar 
    let searchInp = document.getElementById("SearchInput")
    clearChildres("Anime-list")
    searchInList(searchInp.value)
});
