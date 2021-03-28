//sequencia inicio,fim,e passo sem area em branco
function conta() {
  var first = document.getElementById("first")
  var last = document.getElementById("last")
  var step = document.getElementById("step")
  let res = document.getElementById("res")
  if (
    first.value.lenght == 0 ||
    last.value.lenght == 0 ||
    step.value.lenght == 0 ||
    step.value == 0
  ) {
    res.innerHTML = "Impossivel contar"
    window.alert("[ERRO]Verifique os Dados e Tente Novamente")
  } else {
    res.innerHTML = "Contando: <br> "
    let start = Number(first.value)
    let end = Number(last.value)
    let pass = Number(step.value)
    if (pass <= 0) {
      pass = 1
      window.alert("Considerando passo = 1 ")
    }
    if (end > start) {
      for (let c = start; c <= end; c += pass) {
        res.innerHTML += `${c}\u{1F449}`
      }
    } else {
      for (let c = start; c >= end; c -= pass) {
        res.innerHTML += `${c}\u{1F449}`
      }
    }
    res.innerHTML += `\u{1f3C1}`
  }
}
