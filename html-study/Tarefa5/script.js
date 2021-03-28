//tabela
function result() {
  var num = Number(document.getElementById("num").value)
  var res = document.querySelector("div#res")
  let tab = document.getElementById("seltab")
  /*res.innerHTML = `Tabuada de ${num}: <br>`
    for(c=1;c<=10;c++){
        produto = c * num
        res.innerHTML += `${c} x ${num} = ${produto} <br>`
    }*/
  tab.innerHTML = ""
  let c = 1
  while (c <= 10) {
    let item = document.createElement("option")
    item.text = `${c} x ${num} = ${c * num}`
    item.value = `tab${c}`
    tab.appendChild(item)
    c++
  }
}
