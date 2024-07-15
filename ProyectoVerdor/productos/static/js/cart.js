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

function submitCart() {
  const cartItemsInput = document.getElementById('cart-items-input');
  cartItemsInput.value = cart.map(item => `${item.name},${item.price},${item.quantity}`).join(';');
  document.getElementById('cart-form').submit();
}

var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;

//Validacion JQUERY login

$(document).ready(function(){
    $("#bEnviar").click(function(){
        var correo = $("#correo").val();
        var password = $("#password").val();

        if(correo == "" || !expr.test(correo)){
            $("#mensajecorreo").fadeIn();
            return false;
        }else{
            $("#mensajecorreo").fadeOut();
            if(password == ""){
                $("#mensajepassword").fadeIn();
                return false;
            }
        }
    });

});

//Desactiva el btn al no aceptar terminos

function check(checkbox){
    document.getElementById('bRegistro').disabled = !checkbox.checked;
}

//Validacion JQUERY registro

$(document).ready(function(){
    $("#bRegistro").click(function(){
        var correo = $("#correo").val();
        var confcorreo = $("#confcorreo").val();
        var password = $("#password").val();
        var nombre = $("#nombre").val();
        var appat = $("#appat").val();
        var apmat = $("#apmat").val();
        var nac =$("#nac").val();
        var rut = $("#rut").val();
        var fono = $("#fono").val();
        var check = $("#check:checked")

        if(correo == "" || !expr.test(correo)){
            $("#mensajecorreo").fadeIn();
            return false;
        }else{
            $("#mensajecorreo").fadeOut();
                if(password == ""){
                    $("#mensajepassword").fadeIn();
                    return false;
                }else{
                    $("#mensajepassword").fadeOut();
                    if(nombre == ""){
                        $("#mensajenombre").fadeIn();
                        return false;
                    }else{
                        $("#mensajenombre").fadeOut();
                        if(appat == ""){
                            $("#mensajeapellido").fadeIn();
                            return false
                        }else{
                            $("#mensajeapellido").fadeOut();
                            if(apmat == ""){
                                $("#mensajeapellidoma").fadeIn();
                                return false;
                            }else{
                                $("#mensajeapellidoma").fadeOut();
                                if(nac == ""){
                                    $("#mensajenac").fadeIn();
                                    return false;
                                }else{
                                    $("#mensajenac").fadeOut();
                                    if(rut == ""){
                                        $("#mensajerut").fadeIn();
                                        return false;
                                    }else{
                                        $("#mensajerut").fadeOut();
                                        if(fono == ""){
                                            $("#mensajefono").fadeIn();
                                            return false;
                                        }else{
                                            $("#mensajefono").fadeOut();
                                        }
                                    } 
                                }
                            }
                        }
                    }
                }
            }
        

    });
})
