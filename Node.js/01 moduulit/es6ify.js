

//Muunna seuraavat funktiot ES6-syntaksin mukaisiksi ja talleta ne es6ify.js-tiedostoon.

const hello = () => {
 console.log('Hello, World!');
}
const sayHi = (name) => {
 console.log('Hi ' + name + '!');
}
const multiplyByTen = (a) => {
 return a * 10;
}
const sum = (a, b) => {
 return a + b;
}
const power = (base, exponent)  =>{
 let result = 1;
 for (let count = 0; count < exponent; count++) {
 result *= base;
 }
 return result;
}; 

hello();
sayHi();
multiplyByTen();
sum();
power();
