'use strict'

const $catalogue = document.querySelector('#catalogue');
const $showCartBtn = document.querySelector('#cart-button')
const $clearCartBtn = document.querySelector('#clear-button')
const $cart = document.querySelector('#cart')
const $total = document.querySelector('#total')
const $closeCartBtn = document.querySelector('#close-cart')
const $cartList = document.querySelector('#cart-list')
const $orderNavigation = document.querySelector('#order-navigation')
const $NextDeliveryBtn = document.querySelector('#delivery-btn')
const $delivery = document.querySelector('#delivery')
const $send = document.querySelector('#comment')
const $NextSendBtn = document.querySelector('#send-btn')
const $navBtns = $orderNavigation.children


const products = {
    'noodles':40.99,
    'beer': 70.99,
    'milk': 100.99,
    'bread': 50.99,
    'gum': 30.99
}
var cart ={}

function drawProducts(){

    const htmlCard = Object.keys(products).map(function(product) {
        return `<div class="${product}-card card">
        <div class="card-name">${product}</div>
        <img class="card-icon" src="imgs/${product}.png" />
        <div class="card-price">${products[product]}</div>
        <button class="button-add">add</button>
        </div>`
    }).join(' ')

    $catalogue.insertAdjacentHTML('beforeend', htmlCard)
    const addBtns = $catalogue.querySelectorAll('.button-add');
    const  handleClick = (event) => {
        var boughtProduct = event.target.parentElement.querySelector('.card-name')
        let name = boughtProduct.textContent
        name in cart ? cart[name] += 1: cart[name] = 1
        totalCount()
        $cart.style.display = 'none';
    }
    addBtns.forEach(button => {
        button.addEventListener('click', handleClick)
    })
}
function showCart() {
    $cart.style.display = 'flex';
    $cartList.style.display = 'flex';
    $send.style.display ='none';
    $delivery.style.display = 'none'
    $cartList.innerHTML = ''
    if (Object.keys(cart).length === 0){
        $cartList.innerHTML = 'cart is empty, nothing to deliver'
        for (let i=0; i < $navBtns.length; i++){
            $navBtns[i].style.display = 'none'
        }
    }
    else {
        Object.entries(cart).forEach(([key, value]) => $cartList.innerHTML += `${key}: ${value}<br/>`);
        $navBtns[0].style.display = 'inline'
        $navBtns[1].style.display = 'none'
        $navBtns[2].style.display = 'none'

    }
}
function closeCart(e) {
    if(e.type == 'click' || e.key === 'Escape') {
        $cart.style.display = 'none';
    }
}
function nextDelivery(e){
    if(e.type == 'click') {
        $cartList.style.display = 'none';
        $delivery.style.display = 'flex';
        $navBtns[0].style.display = 'none'
        $navBtns[1].style.display = 'inline'
    } 
}
function nextSend(e){
    if(e.type == 'click') {
        $delivery.style.display = 'none';
        $send.style.display = 'flex';
    }
}
function totalCount() {
    let total = 0
    Object.entries(cart).forEach(([key, value]) => total += products[key] * value);
        $total.textContent = `${total.toFixed(2)} руб`
    }

function clearCart() {
    $total.textContent = 'cart is empty'
    cart = {}
}

$closeCartBtn.addEventListener('click', closeCart)
document.addEventListener('keydown', closeCart)
$NextDeliveryBtn.addEventListener('click', nextDelivery)
$NextSendBtn.addEventListener('click', nextSend)
$clearCartBtn.addEventListener('click', clearCart)
$showCartBtn.addEventListener('click', showCart)

drawProducts();
