const button = {
  element: 'fire',
  active: null
}
const someBreathe = function() {
  return `I am Breathing ${this.element}`
}
const dragon = {
  element: 'whater',
  breathe: someBreathe
}

button.active = dragon.breathe
console.log(button.active())

//this se refere ao objeto em que pertence
//no seu momentode execução