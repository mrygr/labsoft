// Objeto para almacenar productos en el carrito
var cart = [];

// Función para agregar un producto al carrito
function addToCart() {
    var size = document.getElementById('size').value;
    var quantity = parseInt(document.getElementById('quantity').value);

    if (size && quantity > 0) {
        var product = {
            size: size,
            quantity: quantity
        };

        cart.push(product);
        updateCartContent();
    }
}

// Función para actualizar el contenido visual del carrito
function updateCartContent() {
    var cartContent = document.getElementById('cart-content');
    cartContent.innerHTML = '';

    for (var i = 0; i < cart.length; i++) {
        var product = cart[i];
        var productElement = document.createElement('div');
        productElement.textContent = `Talla: ${product.size}, Cantidad: ${product.quantity}`;
        cartContent.appendChild(productElement);
    }
}
