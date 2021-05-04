'use strict'
var cart ={}

if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}
function ready(){
    var addToCartButtons = document.getElementsByClassName('button-add')
    for (var i = 0; i < addToCartButtons.length; i++) {
        var button = addToCartButtons[i]
        button.addEventListener('click', addToCart)
    }
    var clearButton = document.getElementsByClassName('clear-button')
    clearButton[0].addEventListener('click', clearCart)
    var removeCart = document.getElementsByClassName('remove')
    for (var i = 0; i < removeCart.length; i++) {
        var button = removeCart[i]
        button.addEventListener('click', removeThis)
    }
}

function addToCart(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement
    var name = shopItem.getElementsByClassName('name')[0].textContent
    var price = shopItem.getElementsByClassName('price')[0].textContent
    name in cart ? cart[name] += 1: cart[name] = 1
    itemToCart(price)
    drawCart()
}

function itemToCart(price) {
    var total = document.getElementsByClassName('total')
    var newTotal = Number(total[0].textContent.split(' ')[0]) + Number(price.split(' ')[0])
    total[0].textContent = `${newTotal.toFixed(2)} ${total[0].textContent.split(' ')[1]}`
}

function clearCart() {
    var total = document.getElementsByClassName('total')
    total[0].textContent = `0 ${total[0].textContent.split(' ')[1]}`
    cart = {}
    drawCart()
}

function drawCart(){
    var cartList = document.getElementsByClassName('cart-list')[0]
    cartList.textContent = ''
    Object.entries(cart).forEach(([key, value]) => cartList.innerHTML += `${key}: ${value}<br/>`) 
}
