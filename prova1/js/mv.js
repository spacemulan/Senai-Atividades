//izadora, cleiton
const sinopse = document.querySelector("#sinopse");
const jjk0 = document.querySelector('#jjk0');
const pasf = document.querySelector('#pasf');
const spdv = document.querySelector('#spdv');
const castle = document.querySelector('#castle');
const icon = document.querySelector('#icon');

//event
jjk0.addEventListener('click', mudar1);
function mudar1(){
    icon.src ='image/jjk0.jpg'
    sinopse.textContent = 'O jovem Yuta Okkotsu ganha o controle de um espírito extremamente poderoso, então um grupo de feiticeiros o matriculam na Tokyo Prefectural Jujutsu High School, para ajudá-lo a controlar esse poder e também para ficar de olho nele.'
}

pasf.addEventListener('click', mudar2);
function mudar2(){
    icon.src ='image/pasf.webp'
    sinopse.textContent = 'A trama se passa no reino de Sky Land e na cidade de Sorashido, envolta na natureza. Um dia, a princesa Eru de Sky Land foge de um monstro e é seguida por uma jovem que quer ser heroína, Sora — elas vão parar em Sorashido e lá conhecem Mashiro Nijigaoka.'
}
spdv.addEventListener('click', mudar3);
function mudar3(){
    icon.src ='image/spider.jpg'
    sinopse.textContent = 'Depois de se reunir com Gwen Stacy, Homem-Aranha é jogado no multiverso, onde ele encontra uma equipe encarregada de proteger sua própria existência.'
}
castle.addEventListener('click', mudar4);
function mudar4(){
    icon.src ='image/howl.webp'
    sinopse.textContent = 'Uma bruxa lança uma terrível maldição sobre a jovem Sophie transformando-a em uma velha. Desesperada, ela embarca em uma odisseia em busca do mago Howl, um misterioso feiticeiro que pode ajudá-la a reverter o feitiço.'
}




