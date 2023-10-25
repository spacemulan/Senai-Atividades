//dom
const chave = "cf88e6f2e2067a5b6fad83ff1917a2f9"
const cidade = document.querySelector('.input-cidade')
const botao = document.querySelector('.botao-busca')
const nomeCidade = document.querySelector('.cidade')
const previsao = document.querySelector('.texto-previsao')
const temperatura = document.querySelector('.temp')

//evento
botao.addEventListener('click', cliquebotao)

//function
function cliquebotao(){
    const city = cidade.value
    dados(city)
}
async function dados(city){
    const resultado = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${chave}&units=metric&lang=pt_br`)
    .then(resultado => resultado.json())
    console.log(resultado)
    
    nomeCidade.textContent = "Tempo em "+resultado.name
    temperatura.textContent = Math.ceil(resultado.main.temp) + "°C"
    previsao.textContent = resultado.weather[0].description
}