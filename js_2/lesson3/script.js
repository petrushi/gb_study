const API = 'https://raw.githubusercontent.com/GeekBrainsTutorial/online-store-api/master/responses';

class Catalog {
    constructor(cart, container = '#products') {
        this.container = container
        this.cart = cart
        this.products = []
        this.cards = []
        this._getProducts()
            .then(data => {
                this.products = [...data]
                this.render()
            })
            .then(() => this._init())
    }
    async _getProducts() {
        try {
            const result = await fetch(`${API}/catalogData.json`)
            return result.json()
        } catch (error) {
            console.log(error)
        }
    }
    async _init() {
        document.querySelector(this.container).addEventListener('click', e => {
            if (e.target.classList.contains('buy-btn')) {
                this.cart.add(this.products.find(product => product.id_product === +e.target.dataset['id']))
            }
        })
    }
    calcSum() {
        return this.cards.reduce((accum, item) => accum += item.price, 0)
    }
    render() {
        let block = document.querySelector(this.container)
        for (let product of this.products) {
            const productObj = new ProductItem(product)
            this.cards.push(productObj)
            block.insertAdjacentHTML('beforeend', productObj.render())
        }
    }
}

class ProductItem {
    constructor(product, img = 'https://place-hold.it/150') {
        this.product_name = product.product_name
        this.price = product.price
        this.img = img
        this.id_product = product.id_product
    }
    render() {
        return `<div class="products-item" data-id="${this.id_product}">
        <img src=${this.img}>
        <h3>${this.product_name}</h3>
        <p>${this.price}</p>
        <button class="card-btn buy-btn" data-id="${this.id_product}"
        data-name="${this.product_name}" data-price="${this.price}">Добавить</button>
        </div>`
    }
}

class Cart {
    constructor(container = '#cart-body', preview = '#cart-preview') {
        this.container = container
        this.preview = preview
        this.amount = 0
        this.quantity = 0
        this.products = []
        this.cards = []
        this._getProducts()
            .then(data => {
                this.products = [...data.contents]
                this.quantity = data.countGoods
                this.amount = data.amount
                this.renderBody()
            })
            .then(() => this._init())
    }
    async _getProducts() {
        try {
            const result = await fetch(`${API}/getBasket.json`)
            return result.json()
        }
        catch (error) {
            console.log(error)
        }
    }
    async _init() {
        document.querySelector(this.container).addEventListener('click', e => {
            if (e.target.classList.contains('remove-btn')) {
                this.remove(e.target)
            }
        })
    }
    renderBody() {
        let block = document.querySelector(this.container)
        block.innerHTML = ''
        this.cards = []
        if (this.products.length > 0) {
            for (let product of this.products) {
                const cartObj = new CartItem(product)
                this.cards.push(cartObj)
                block.insertAdjacentHTML('beforeend', cartObj.render())
            }
        } else {
            block.insertAdjacentHTML('beforeend', 'Ваша корзина пуста')
        }
    }
    add(product) {
        let productIndex = this.products.findIndex(card => card.id_product === product.id_product)
        if (productIndex != -1) {
            this.products[productIndex].quantity += 1
        }
        else {
            let cartObj = new CartItem(product)
            this.products.push(cartObj)
        };
        this.renderBody()
    }
    remove(target) {
        let productId = +target.dataset['id']
        let productIndex = this.products.findIndex(product => product.id_product === productId)
        if (this.products[productIndex].quantity === 1) {
            this.products = this.products.filter(product => product.id_product != productId)
        }
        else {
            this.products[productIndex].quantity -= 1
        }
        this.renderBody()
    }

}
class CartItem extends ProductItem {
    constructor(product, img = 'https://place-hold.it/50') {
        super(product, img)
        if (product.quantity) {
            this.quantity = product.quantity
        } else {
            this.quantity = 1
        }
    }
    render() {
        return `<div class="cart-item" data-id="${this.id_product}">
        <img src=${this.img}>
        <h3>${this.product_name}</h3>
        <p>${this.price}</p>
        <p>Кол-во:${this.quantity}</p>
        <button class="card-btn remove-btn" data-id="${this.id_product}">Удалить</button>
        </div>`
    }
}

const cart = new Cart()
const list = new Catalog(cart)
