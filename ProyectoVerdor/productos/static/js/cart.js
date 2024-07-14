let carro = []
let totalPrice = 0;
function addToCart(productName, productPrice) {
  // Añadir producto al carrito
  carro.push({ name: productName, price: productPrice });
  // Actualizar el precio total
  totalPrice += productPrice;
  // Actualizar la interfaz de usuario
  updateCartUI();
}

function updateCartUI() {
  const cartItemsElement = document.getElementById('cart-items');
  const totalPriceElement = document.getElementById('total-price');

  // Limpiar la lista del carrito
  cartItemsElement.innerHTML = '';

  // Añadir cada producto del carrito a la lista
  carro.forEach(item => {
    const tr = document.createElement('tr');

    const tdName = document.createElement('td');
    tdName.textContent = item.name;
    tr.appendChild(tdName);

    const tdPrice = document.createElement('td');
    tdPrice.textContent = `$${item.price.toFixed(0)}`;
    tr.appendChild(tdPrice);

    const tdQty = document.createElement('td');
    tdQty.textContent = `1`;
    tr.appendChild(tdQty);

    cartItemsElement.appendChild(tr);
  });

  // Actualizar el precio total
  totalPriceElement.textContent = totalPrice.toFixed(0);
}
