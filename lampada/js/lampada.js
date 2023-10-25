//DOM
const lampada = document.querySelector('#lampada')
const bt1 = document.querySelector('#btligar')
const bt2 = document.querySelector('#btapagar')

//evento
bt1.addEventListener('click', ligar)
bt2.addEventListener('click', apagar)
lampada.addEventListener('dblclick', quebrar)

//função - ultima parte
function ligar(){
    lampada.src = "images/acesa.gif"
}
function apagar(){
    lampada.src = "images/apagada.gif"
}
function quebrar(){
    lampada.src = "images/quebrada.jpg"
}
