//const readline = require('readline')

const readline = require('readline').createInterface({ 
  input: process.stdin, 
  output: process.stdout })
  readline.question("what's your name? ", name => { console.log(`Hello ${name}`); readline.close(); })
//let response = readline()
//console.log(readline)