//dom
const gouta = document.querySelector('#gh1');
const b1 = document.querySelector('#botao1');
const b2 = document.querySelector('#botao2');
const b3 = document.querySelector('#botao3');
const b4 = document.querySelector('#botao4');

//evento
b1.addEventListener('click', mudar1);
function mudar1(){
    gouta.src = 'images/gojohime2.jpg';
}
b2.addEventListener('click', mudar2);
function mudar2(){
    gouta.src = 'images/story.jpg';
}
b3.addEventListener('click', mudar3);
function mudar3(){
    gouta.src = 'images/Screenshot_13.jpg';
}
b4.addEventListener('click', mudar4);
function mudar4(){
    gouta.src = 'images/638015569514262400-story.jpg';
}