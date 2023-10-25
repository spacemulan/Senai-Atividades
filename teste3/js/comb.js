const distancia = document.querySelector('#distancia');
const consumo = document.querySelector('#consumo');
const preco = document.querySelector('#preco');
const bt = document.querySelector('#botao');
const res = document.querySelector('#resultado');

bt.addEventListener('click', gasosa);
function gasosa(){
    let dis = distancia.value;
    let cons = consumo.value;
    let pre = preco.value;
    let calculo = (dis/cons)*pre;
    res.textContent = "R$"+calculo.toFixed(2);
}