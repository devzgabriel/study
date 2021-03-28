
function jaRealizada(){
  return Promise.resolve('01001000');
}

function nRelaizada(){
  return Promise.reject();
}

jaRealizada.then((data)=>{
  console.log(data);
});
nRelaizada.catch(()=>{
  console.log("Faiou");
});

function promiseTrabalhada(){
  return new Promise(function(resolve, reject){
    setTimeout(function(){
      resolve('HelloWorld');
    },1000)
  })
}

promiseTrabalhada().then((mesage)=> console.log(mesage))

//  Para saber endereço usando o fetch( api do browser)
window.
  fetch('https://viacep.com.br/ws/01001000/json/')
  .then(function(data){
    data.json().then(function(endereco){
      // .json é um metodo q transforma o dado em json q usa uma promise
      // e como é uma operação asincrona(promise), por isso o then
      console.log(endereco)
    })
  })

  // OU

window.
  fetch('https://viacep.com.br/ws/01001000/json/')
  .then(function(data){
    return data.json()
  })
  .then(function(endereco){
    console.log(endereco)
  })

  // Englobando:

function pegaCep(cep){
  return window
    .fetch(`https://viacep.com.br/ws/${cep}/json/`)
}
function extraiEndereco(data){
  return data.json()
}
function imrimeEndereco(endereco){
  console.log(endereco)
}
function trataErro(){
  console.log('Erro na execução')
}
jaRealizada()
// tem o CEP
  .then(pegaCep)
//tem o HTTP
  .then(extraiEndereco)
//tem o body da mensagem em json
  .then(imrimeEndereco)
//tem a informação printada
//para tratar algum erro:
  .catch(trataErro)


// usando o promiss all
Promise.all([
  pegaCep('01001000'),
  jaRealizada()
]).then((resultado) => {
  console.log(resultado)
})

Promise.race([
  pegaCep('01001000'),
  jaRealizada()
]).then((resultado) => {
  console.log(resultado)
}, function(valorRejeitado){
  console.log(valorRejeitado)
})