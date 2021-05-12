const goods = [
    { title: 'Shirt', price: 150 },
    { title: 'Socks', price: 50 },
    { title: 'Jacket', price: 350 },
    { title: 'Shoes', price: 250 },
];

const renderGoodsItem = (title, price) => `<div class="goods-item">
        <div class="icon"></div><h3>${title}</h3><p>${price}</p><button>Добавить</button>
    </div>`;
// убрал return и скобки, добавил кнопку и иконку

const renderGoodsList = (list = []) => {    // добавил значение по умолчанию - пустой список
    let goodsList = list.map(item => renderGoodsItem(item.title, item.price));
    document.querySelector('.goods-list').innerHTML = goodsList.join('');   // методом join убрал запятые между карточками товаров
}

renderGoodsList(goods);
