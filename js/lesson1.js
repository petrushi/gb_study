'use strict'
//1
var Tc = 15;
var Tf = (9 / 5) * Tc + 32;
window.alert(Tf);
//2
//3
var name = 'Василий';
var admin = name;
console.log(admin);
//4 1000 + "108" = ?
// Конкатенация в данном случае приоритетнее сложения, поэтому Number будет приведен к String.
// Ответ: '1000108'
console.log(1000 + '108');
