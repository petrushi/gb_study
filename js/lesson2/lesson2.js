//  https://jsfiddle.net/cn9mkwtd/13/

'use strict'

//1

var a = 1, b = 1, c, d;

//	c = ++a; alert(c);           // 2
// в пред. строке использована префиксная форма инкрементации, поэтому переменная сразу увеличилась на единицу

//	d = b++; alert(d);           // 1
// в пред. строке использована постфиксная форма записи инкрементации, поэтому переменная увеличилась на единицу только после возврата значения

//	c = (2+ ++a); alert(c);      // 5
// в пред. строке 2 складывается с инкременнированной префиксно переменной a, поэтому в значение c попадает 2 + 3

//	d = (2+ b++); alert(d);     // 4
// в пред. строке значение b увеличивается после присваивания, поэтому в d попадает 2 + 2, после этой строки значение b далее не влияет на значение d

//	alert(a);                    // 3
// переменная a увеличивалась на единицу на 3 строке и на 7, после чего были возвраты ее значения

//	alert(b);                    // 3
// переменная b увеличивилась на единицу на 5 и на 9 строке, после чего были ее возвраты ее значения

//2

var a = 2;
var x = 1 + (a *= 2);
// переменная a умножается на 2, после чего к произведению прибавляется единица
//ответ: 5
//	alert(x);

//3

var a = 0;
var b = -10;
if (a >= 0 && b >= 0)
	console.log(a - b);
else if (a < 0 && b <0)
	console.log(a * b);
else // if (Math.abs(a + b) != Math.abs(a) + Math.abs(b)) // тогда для 0 отдельное условие
	console.log(a + b);
  
//4
// без switch
var numsArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
var n = 5;
console.log(numsArr.splice(n,15));

// с помощью switch :(
var a = 8;
switch(a){
	case 0:
  console.log('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 1:
  console.log('1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
    break;
  case 2:
  console.log('2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 3:
  console.log('3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 4:
  console.log('4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 5:
  console.log('5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 6:
  console.log('6, 7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 7:
  console.log('7, 8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 8:
  console.log('8, 9, 10, 11, 12, 13, 14, 15');
  break;
  case 9:
  console.log('9, 10, 11, 12, 13, 14, 15');
  break;
  case 10:
  console.log('10, 11, 12, 13, 14, 15');
  break;
  case 11:
  console.log('11, 12, 13, 14, 15');
  break;
  case 12:
  console.log('12, 13, 14, 15');
  break;
  case 13:
  console.log('13, 14, 15');
  break;
  case 14:
  console.log('14, 15');
  break;
  case 15:
  console.log('15');
  break;
  default:
  console.log('input should be int in [0..15]');
  break;
}

//5

function addition(x, y) {
	return x + y;
}

function substraction(x, y) {
	return x - y;
}

function multiplication (x, y) {
	return x * y;
}

function division (x, y) {
	switch (y){
  case 0:
  return('division by zero');
  default:
  return(x / y);
}
}
//6

function mathOperation(arg1, arg2, operation) {
switch(operation){
case '+':
	return addition(arg1, arg2);
 case '-':
 	return substraction(arg1, arg2);
 case '*':
 	return multiplication(arg1, arg2);
 case '/':
 	return division(arg1, arg2);
 default:
 return('unknown operator');
}
}

//7

console.log(null == 0);
// возвращает false, потому что null это не число 0, а специальное значение, не относящееся к типу Number, например сравнение с undefined покажет true:
console.log(undefined == null);
// однако проверка на идентичность покажет false:
console.log(undefined === null);

//8

function powNum(val, pow) {
if(pow == '1')
	return val;
return val * powNum(val, --pow);
}

console.log(powNum(3, 4));
