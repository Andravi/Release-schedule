import { RealeaseList } from "./realeaseList.js"

let animeCards = document.querySelector('.Anime-list');
// TODO -> show release date



let releaseList = new RealeaseList()

await releaseList.initList().then(
    () => {
        showList()
    }
)


function clearChildres(classe) { // COlocar Uma animação de loading enquanto está vazio
    const animeList = document.getElementsByClassName(classe)[0];
    animeList.textContent = '';
}

function addAnimeCard(anime){
    let animeCard = document.createElement('div');
    animeCard.classList.add('Anime-card')
    animeCards.appendChild(animeCard);
    animeCard.innerHTML = ` <h1 id="title">${anime['nome']}</h1>
                            <span>${anime['generos']}</span>
                            <img src="${anime['image']}" alt="Teste">
                            <h3>${anime['time']['dia']} às ${anime['time']['horas']} </h3>`;
}


function showList(day) {
    if (day) {
        releaseList.__schedule
            .forEach(
                (anime, index) => {
                    if (anime['time']['dia'] == day) {
                        addAnimeCard(anime)
                    }
                }
            );
    } else {
        releaseList.__schedule
            .forEach((anime, index) => {
                addAnimeCard(anime)
            });
    }
}

function filterByGenre(genre) {
    releaseList.__schedule
        .forEach(
            (anime, index) => {
                if (anime['nome'].toLowerCase().includes(genre.toLowerCase())) { // Mas quando é incerto ? // Tambem não aparecem o de temporadas antigas
                    addAnimeCard(anime)
                }
            }
        );
}

function searchInList(name) {
    releaseList.__schedule
        .forEach(
            (anime, index) => {
                if (anime['nome'].toLowerCase().includes(name.toLowerCase())) { // Mas quando é incerto ? // Tambem não aparecem o de temporadas antigas
                    addAnimeCard(anime)
                }
            }
        );
    if (animeCards.children.length == 0) {
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
        if (e.target.innerHTML == "Todos"){
            console.log("deveria")
            showList()
        } else {
            showList(e.target.innerHTML + "s")
        }
    }

});

buscarBtn.addEventListener('click', function (e) {
    // Pegar valor da caixa de testo -> se não vazia -> pesquisar 
    let searchInp = document.getElementById("SearchInput")
    clearChildres("Anime-list")
    searchInList(searchInp.value)
});
