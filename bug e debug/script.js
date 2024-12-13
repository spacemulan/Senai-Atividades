//let b  = 2;

//try {
  //  let a = 2 +b;
//}catch(error){
  //  console.log(error);
//}


//const reg1 = new RegExp(`Bola`)

//console.log(reg1.test(`Tem Bola`));
//console.log(reg1.test(`Não tem`))
//const reg2 =/bola/;
//console.log(reg2.test(`Tem bola`));
//console.log(reg2.test(`não tem `));

//const reg1 =/[1,2,3,4,5]/;
//console.log(reg1.test(`Temos o numero 6`)) ;
//console.log(reg1.test(`Temos o numero 3`));

const dia =/\d\d/;
console.log(dia.test(`2019`) && `2019`.length==2)
const palavras = /\w\w\w/;
console.log(palavras.test(`ads`));

//function saudacao(nome){
    //if(typeof nome != `string`){
       // throw new  console.error(`O parametro esta errado`);
   // }else{
     //   console.log(`oi ${nome}`)
    //}
//}
//saudacao(`Izadora`)

const notab =/[^ab]/
console.log(notab.test(`a`))
console.log(`Aqui tem a`);

let cep = /\d{5}-\d{3}/
console.log(cep.test(`88888-888`));
console.log(cep.test(`777-77777`));

const digitos = /\d+/;
console.log(digitos.exec(`Tem numero 1000 aqui`));
console.log(digitos.exec(`aqui não tem`));

const reg = /\w+: (Ana|João | Maria)/
console.log(reg.test(`Nome: Ana`));
console.log(reg.test(`Nome: Pedro`));

const validaDominio = /\w+@\w+\.\w+/;
console.log(validaDominio.test(`carlosalberto@gmail.com`));
