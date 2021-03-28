var conj = []

function add() {
  let num = document.getElementById("num")
  let tab = document.getElementById("seltab")

  if (conj.indexOf(num.value) != -1) {
    window.alert("Número já adicionado")
  } else if (num.value >= 1 && num.value <= 100) {
    //Adiciona Elemento na tabela:
    conj.push(Number(num.value))
    let item = document.createElement("option")
    item.text = `Valor ${num.value} adicionado`
    item.value = `tab${num.value}`
    tab.appendChild(item)
  } else {
    window.alert("Dados não Compativeis")
  }
  ans.innerHTML = ""
  num.value = ""
  num.focus()
}

function answer() {
  let ans = document.querySelector("div#ans")
  ans.innerHTML = ""
  size = conj.length
  if (size == 0) {
    window.alert("Não há dados o Suficiente")
  } else {
    maior = conj[0]
    menor = conj[0]
    sum = 0
    for (let pos in conj) {
      if (conj[pos] > maior) {
        maior = conj[pos]
      }
      if (conj[pos] < menor) {
        menor = conj[pos]
      }
      sum += conj[pos]
    }

    averange = sum / size

    ans.innerHTML += `${size} numeros cadastrados</br>`
    ans.innerHTML += `${maior} é o maior valor</br>`
    ans.innerHTML += `${menor} é o menor valor</br>`
    ans.innerHTML += `${sum} é a soma</br>`
    ans.innerHTML += `${averange} é a média</br>`
  }
}
