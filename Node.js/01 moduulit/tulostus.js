

const tulostaTahtia = (x) => {
    for (i = 0; i < x; i++){
     process.stdout.write("x") 
    }
  console.log("")
}

const tulostaTulos = (inp) => {
  let parsed = inp.toString();
  for (i = 0; i < parsed.length; i++){
    process.stdout.write("-")
  }

  console.log("");
  console.log(parsed);

  for (i = 0; i < parsed.length; i++){
    process.stdout.write("-")
  }
  console.log("");
}



/*tulostaTahtia(10);

tulostaTulos("Tämä on lopputulos");

tulostaTulos(34523452);*/


module.exports = {
  tulostaTahtia,
  tulostaTulos,
}