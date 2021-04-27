'use strict'
//1
let i = 0;
let primes = [2, 3, 5, 7];

while (i<=100) {
if (i > 7){
	let prime = true;
  
  for (let firstPrimes of primes.slice(0, 4)) {
    if (i % firstPrimes == 0){
    prime = false;
    break
    }}
    
  if (prime){
  	primes.push(i)}
  } i++;}
  
  console.log(primes);

//2 //3
function countBasketPrice(basket){
var total = 0;
for (var i = 0; i < basket.length; i++){
	total += basket[i]
}
return total;
}

let myBasket = [63, 31, 31];
console.log(countBasketPrice(myBasket))

//4
for (let j=0; j < 10; console.log(j++));

//5
let lines = 20
for (var count=0; count < lines; count++){
console.log('x'.repeat(count + 1));
}
