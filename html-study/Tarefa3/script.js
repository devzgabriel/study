function result() {
  var data = new Date()
  var ano_atual = data.getFullYear()
  var ano_nasc = document.getElementById("txtano")
  var res = document.querySelector("div#res")
  if (ano_nasc.value.length == 0 || ano_nasc.value > ano_atual) {
    window.alert("[ERRO]Verifique os Dados e Tente Novamente")
  } else {
    var sex = document.getElementsByName("radsex")
    var idade = ano_atual - Number(ano_nasc.value)
    var genero = ""
    var img = document.createElement("img")
    img.setAttribute("id", "foto")

    if (sex[0].checked) {
      genero = "Homem"
      if (0 < idade && idade < 15) {
        img.setAttribute("src", "kid-m.jpg")
      } else if (idade < 25) {
        img.setAttribute("src", "young-m.jpg")
      } else if (idade < 60) {
        img.setAttribute("src", "adult-m.jpg")
      } else if (idade >= 60) {
        img.setAttribute("src", "old-m.jpg")
      }
    } else if (sex[1].checked) {
      genero = "Mulher"
      if (0 < idade && idade < 15) {
        img.setAttribute("src", "kid-f.jpg")
      } else if (idade < 25) {
        img.setAttribute("src", "young-f.jpg")
      } else if (idade < 60) {
        img.setAttribute("src", "adult-f.jpg")
      } else {
        img.setAttribute("src", "old-f.jpg")
      }
    }

    res.style.textAlign = "center"
    res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
    res.appendChild(img)
  }
}
