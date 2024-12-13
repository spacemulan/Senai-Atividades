function escrevernoconsole(){
    console.log("Escrevendo no console!");
}
escrevernoconsole();

function imprimirUmnumero(num){
    console.log("Numero " +num);
}
imprimirUmnumero(2);


const numeroAleatorio = function(){
    console.log(Math.random());
}
numeroAleatorio();
numeroAleatorio();
numeroAleatorio();


function multiplicarNumero(x,y,z){
    return x* y* z;
}
console.log(multiplicarNumero(2,3,6));

function podeDirigir(idade, cnh){
    if(idade>=18 && cnh ==true){
        console.log("Pode dirigir");
    }else{
        console.log("Não tem permissão para dirigir.")
    }
}
console.log(podeDirigir(19, true));
console.log(podeDirigir(17, false));

//escopo
let h = 10;

function imprimir(){
    let h = 150;
    console.log(h);
}
imprimir();
console.log(h);

//escopo 2
let consoleTeste = () =>{
    console.log("OIIII");
}
consoleTeste();

//COM PARAMETRO

let soma = (a,b) => {
    return a + b;
}
console.log(soma(1,2));

//recursão
//funçao recursiva repete uma função varias vezes0