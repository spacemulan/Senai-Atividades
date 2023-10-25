const hora = document.querySelector('#hora');
const minuto = document.querySelector('#minuto');
const segundo = document.querySelector('#segundo');
const congrats = document.querySelector('#congrats');

setInterval(() => {
    let dateToday = new Date();
    let hr = dateToday.getHours();
    hora.textContent = hr;
    let min = dateToday.getMinutes();
    minuto.textContent = min;
    let seg = dateToday.getSeconds();
    segundo.textContent = seg;
    if (hr>=18){
        congrats.textContent='Boa Noite!'
    }
    else if (hr>=13){
        congrats.textContent='Boa tarde!'
    }
    else if (hr>=4){
        congrats.textContent='Bom dia!'
    }

}, 1000); 
