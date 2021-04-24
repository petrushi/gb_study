'use strict'
var field = document.querySelector('#field');
field.style.width = '640px';
field.style.display = 'flex';
field.style.flexWrap = 'wrap';
var figures = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king'];
const cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

function drawField(){
let isBlack = false;

for (let j = 0; j < 8; j++){
    for (let i = 0; i < 8; i++) {
        let cell = document.createElement('div');
        cell.className = ('cell');
        cell.id = cols[i] + (8 - j);
        cell.style.width = '80px';
        cell.style.height = '80px';
        cell.style.display = 'flex';
        if (isBlack){
            cell.style.backgroundColor = 'rgb(101, 101, 111)';
        }
        else
            cell.style.backgroundColor = 'rgb(140, 140, 150)';
        field.append(cell);
        cell.textContent =  cols[i] + (8 - j);
        isBlack = !isBlack;
    }
isBlack = !isBlack;
}
return 0;
}

function newGame(){
    let startRows = [8, 7, 2, 1];
    for (let i = 0; i < startRows.length; i++){
        if (i < 2){
            var figColor  = 'black';
        }
        else {
            var figColor = 'white';
        }
        for (let k = 0; k < 8; k++){
            let pos = cols[k] + startRows[i];
            let cell = document.getElementById(pos);
            let figure = document.createElement('div');
            if (i == 1 || i == 2){
                var shape = figures[0];
            }
            else {
                if (k < 5){
                    var shape = figures[k + 1];
                }
                else
                    var shape = figures[8 - k];
            }
            figure.className = figColor + ' figure ' + shape;
            figure.style.color = figColor;
            cell.append(figure);
            let icon = document.createElement('img');
            icon.src = 'imgs/'+ figColor + '_' + shape + '.png'
            icon.alt = figColor + ' ' + shape;
            figure.append(icon);
    }
    }
return 0;
}

drawField();
newGame();
