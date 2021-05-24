class GoodsItem {
    constructor(title, price) {
      this.title = title;
      this.price = price;
    }
    render() {
      return `<div class="goods-item"><div class="icon"></div><h3>${this.title}</h3><p>${this.price}</p><button>Добавить</button></div>`;
    }
  }

class GoodsList {
  constructor() {
    this.goods = [];
  }
  fetchGoods() {
    this.goods = [
      { title: 'Shirt', price: 150 },
      { title: 'Socks', price: 50 },
      { title: 'Jacket', price: 350 },
      { title: 'Shoes', price: 250 },
    ];
  }
  render() {
    let listHtml = '';
    this.goods.forEach(good => {
      const goodItem = new GoodsItem(good.title, good.price);
      listHtml += goodItem.render();
    });
    document.querySelector('.goods-list').innerHTML = listHtml;
  }
  countTotalSum() {
    let totalSum = this.goods.reduce((acc, product) => acc += product.price, 0);
    alert(`Общая сумма товаров: ${totalSum}`);
  }
}

class CartList {
  constructor(){}
  add(){}
  remove(){}
  checkout(){}
  render(){}
}

class CartItem {
  constructor(){}
  render(){}
}

const list = new GoodsList();
list.fetchGoods();
list.render();
list.countTotalSum();
