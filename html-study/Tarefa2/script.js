function carregar() {
  var msgElement = document.getElementById("msg")
  var imgElement = document.getElementById("imagem")
  var bomElement = document.getElementById("bom")
  var agora = new Date()
  var hora = agora.getHours()
  var min = agora.getMinutes()

  msgElement.innerHTML = `Agora são ${hora}:${min}h`
  if (hora < 12) {
    bomElement.innerHTML = `Bom Dia`
    bomElement.style.color = "#055299"
    document.getElementById("autor").style.color = "#055299"
    imgElement.src = "img_site_manha.jpg"
    document.body.style.background = "#e6ad63"
  } else if (hora < 18) {
    bomElement.innerHTML = "Boa Tarde"
    bomElement.style.color = "#ff7300ea"
    document.getElementById("autor").style.color = "#ff7300ea"
    imgElement.src = "img_site_tarde.png"
    document.body.style.background = "#055299"
  } else {
    bomElement.innerHTML = "Boa Noite"
    imgElement.src = "img_site_noite.jpg"
    bomElement.style.color = "#ff7300ea"
    document.getElementById("autor").style.color = "#ff7300ea"
    document.body.style.background = "#024d3a"
  }
}
