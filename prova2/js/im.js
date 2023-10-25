
const peso = document.querySelector('#peso')
const altura = document.querySelector('#altura')
const bt = document.querySelector ('#botao')
const resultado = document.querySelector('#resultado')
const imc = document.querySelector('#imcres')
bt.addEventListener('click', viagem)


function viagem (){
    let pes = peso.value
    let alt = altura.value


    let cal= pes/(alt*alt)
    resultado.textContent = cal.toFixed(2)+"%"
    imc.textContent
    if (cal<18.5){
        imc.textContent = 'Abaixo do peso'
    }
    else if (cal>=19 && cal<=25){
        imc.textContent = 'Peso normal'
    }
    else if (cal>=26 && cal<=30){
        imc.textContent = 'Acima do peso'
    }
     if (cal>31){
        imc.textContent = 'Obesidade' }
}