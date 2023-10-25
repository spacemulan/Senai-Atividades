const frmpesquisa = document.querySelector("form");
const apikey = '1cffa8f9'; // Substitua '1cffa8f9' pela sua chave API OMDB.

frmpesquisa.onsubmit = (ev) => {
    ev.preventDefault();
    const pesquisa = ev.target.pesquisa.value;
    if (pesquisa === "") {
        alert('Preencha o campo!');
        return;
    }
    fetch(`https://www.omdbapi.com/?s=${pesquisa}&apikey=${apikey}`) // Corrigido o uso da variável apikey
        .then(result => result.json())
        .then(json => carregaLista(json));
};

const carregaLista = (json) => {
    const lista = document.querySelector("div.lista");
    lista.innerHTML = "";
    if (json.Response === "False") {
        alert('Filme não encontrado');
        return;}

    json.Search.forEach(element => {
        console.log(element);

        let item = document.createElement("div");
        item.classList.add("item");
        item.innerHTML = `<img src="${element.Poster}"/><h2>${element.Title}</h2>`; // Corrigido o uso de `${}` e a tag de fechamento </h2>
        lista.appendChild(item);
    });
};
