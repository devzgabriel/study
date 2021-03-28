

var inputs = readline().split(' ');
let lightX = parseInt(inputs[0]); // the X position of the light of power
let lightY = parseInt(inputs[1]); // the Y position of the light of power
let initialTx = parseInt(inputs[2]); // Thor's starting X position
let initialTy = parseInt(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
    const remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.
    if (lightX < initialTx){
    if (lightY == initialTy){
      console.log("W")                    
      initialTx -= 1               
      initialTy = initialTy
    }

    else if(lightY < initialTy){
      console.log("NW")
      initialTx -= 1
      initialTy -= 1
    }

    else if (lightY > initialTy){
      console.log("SW")
      initialTx -= 1
      initialTy += 1
    }
  }

  else if (lightX > initialTx){
    if (lightY == initialTy){
      console.log("E")
      initialTx += 1
    }

    else if (lightY < initialTy){
      console.log("NE")
      initialTx += 1
      initialTy -= 1
    }

    else if (lightY > initialTy){
      console.log("SE")
      initialTx++
      initialTy += 1
    }
  }
  else{
    if (lightY < initialTy){
      console.log("N")
      initialTy -= 1
    }

    else if (lightY > initialTy){
      console.log("S")
      initialTy += 1
    }
  }
}