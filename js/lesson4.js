'use strict'

//1
class NumberObject {
  constructor(ones, tens, hundreds) {
    this.ones = ones;
    this.tens = tens;
    this.hundreds = hundreds;
}
}
function objFromNum(myNum) {
  if (0 <= myNum && myNum <= 999) {
    return new NumberObject(myNum % 10, Math.floor(myNum % 100 / 10), Math.floor(myNum /100));
  }
  else {
    console.log('число больше 999 или меньше 0');
    return null;
}
}

let rndNum = objFromNum(245);
console.log(rndNum);

//2
//3

class Product {
	constructor(name, info){
		this.name = name;
    this.info = info;
  }
}
class ProductCatalog extends Product {
	constructor(name, info, price, totalAmount, availableAt) {
    super(name, info);
    this.price = price;
    this.totalAmount = totalAmount;
    this.availableAt = availableAt;
}
}
class BasketProduct extends ProductCatalog {
	constructor (name, price, basketAmount, totalAmount, availableAt) {
  super(name, price, basketAmount, totalAmount, availableAt);
  }
}
function addProduct(basket, product, AddAmount){
		let buy = new BasketProduct(product.name, product.info, product.price, product.totalAmount, product.availableAt);
    buy.basketAmount = AddAmount;
    product.totalAmount = product.totalAmount - AddAmount;
    buy.totalAmount = product.totalAmount;
    basket.push(buy);
    return 0;
  }

function BasketPrice(basket) {
  let totalPrice = 0;
  for (var i = 0; i < basket.length; i++) {
  	totalPrice += basket[i].price * basket[i].basketAmount;
  }
  return totalPrice;
}

let refrigerator = new ProductCatalog ('toshiba', 'lorem ipsum', 3500, 16, 'Moscow');
let playstation = new ProductCatalog ('sony ps 9 + DLC', 'dolorem ipsum', 1000, 32, 'Moscow');
let audiosystem = new ProductCatalog ('marshall', 'nunc erat lorem', 4000, 5, 'Moscow');

let someBasket = [];

addProduct(someBasket, playstation, 2);
addProduct(someBasket, audiosystem, 1);
console.log(BasketPrice(someBasket));
