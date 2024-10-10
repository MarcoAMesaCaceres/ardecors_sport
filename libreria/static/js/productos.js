//Variable que mantiene el estado visible del carrito
var carritoVisible = false;

//Espermos que todos los elementos de la pàgina cargen para ejecutar el script
if(document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
}else{
    ready();
}

function ready(){
    
    //Agregremos funcionalidad a los botones eliminar del carrito
    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for(var i=0;i<botonesEliminarItem.length; i++){
        var button = botonesEliminarItem[i];
        button.addEventListener('click',eliminarItemCarrito);
    }

    //Agrego funcionalidad al boton sumar cantidad
    var botonesSumarCantidad = document.getElementsByClassName('sumar-cantidad');
    for(var i=0;i<botonesSumarCantidad.length; i++){
        var button = botonesSumarCantidad[i];
        button.addEventListener('click',sumarCantidad);
    }

     //Agrego funcionalidad al buton restar cantidad
    var botonesRestarCantidad = document.getElementsByClassName('restar-cantidad');
    for(var i=0;i<botonesRestarCantidad.length; i++){
        var button = botonesRestarCantidad[i];
        button.addEventListener('click',restarCantidad);
    }

    //Agregamos funcionalidad al boton Agregar al carrito
    var botonesAgregarAlCarrito = document.getElementsByClassName('boton-item');
    for(var i=0; i<botonesAgregarAlCarrito.length;i++){
        var button = botonesAgregarAlCarrito[i];
        button.addEventListener('click', agregarAlCarritoClicked);
    }

    //Agregamos funcionalidad al botón comprar
    document.getElementsByClassName('btn-pagar')[0].addEventListener('click',pagarClicked)
}
//Eliminamos todos los elementos del carrito y lo ocultamos
function pagarClicked() {
    // Obtener el total del carrito
    var total = document.getElementsByClassName('carrito-precio-total')[0].innerText;

    // Inicializar el mensaje
    var mensaje = "HOLA¡ Me interesa estos artículos de ardecors. El total de mi compra es: " + total + "\n\nArtículos en el carrito:\n";

    // Obtener todos los elementos del carrito
    var carritoItems = document.getElementsByClassName('carrito-item');

    // Recorrer cada artículo y agregar la información al mensaje
    for (var i = 0; i < carritoItems.length; i++) {
        var item = carritoItems[i];
        var titulo = item.getElementsByClassName('carrito-item-titulo')[0].innerText;
        var cantidad = item.getElementsByClassName('carrito-item-cantidad')[0].value;
        var precio = item.getElementsByClassName('carrito-item-precio')[0].innerText;
        var imagenSrc = item.getElementsByTagName('img')[0].src;

        // Agregar la información del artículo al mensaje
        mensaje += `\n- ${titulo}\n  Cantidad: ${cantidad}\n  Precio: ${precio}\n  Imagen: ${imagenSrc}\n`;
    }

    // Construir el enlace de WhatsApp
    var numeroWhatsApp = "3508765092"; // Número de WhatsApp sin el signo "+"
    var enlace = "https://api.whatsapp.com/send?phone=" + numeroWhatsApp + "&text=" + encodeURIComponent(mensaje);

    // Abrir el enlace de WhatsApp en una nueva ventana
    window.open(enlace, '_blank');
}


//Funciòn que controla el boton clickeado de agregar al carrito
function agregarAlCarritoClicked(event){
    var button = event.target;
    var item = button.parentElement;
    var titulo = item.getElementsByClassName('titulo-item')[0].innerText;
    var precio = item.getElementsByClassName('precio-item')[0].innerText;
    var imagenSrc = item.getElementsByClassName('img-item')[0].src;
    console.log(imagenSrc);

    agregarItemAlCarrito(titulo, precio, imagenSrc);

    hacerVisibleCarrito();
}

//Funcion que hace visible el carrito
function hacerVisibleCarrito(){
    carritoVisible = true;
    var carrito = document.getElementsByClassName('carrito')[0];
    carrito.style.marginRight = '0';
    carrito.style.opacity = '1';

    var items =document.getElementsByClassName('contenedor-items')[0];
    items.style.width = '60%';
}

//Funciòn que agrega un item al carrito
function agregarItemAlCarrito(titulo, precio, imagenSrc){
    var item = document.createElement('div');
    item.classList.add = ('item');
    var itemsCarrito = document.getElementsByClassName('carrito-items')[0];

    //controlamos que el item que intenta ingresar no se encuentre en el carrito
    var nombresItemsCarrito = itemsCarrito.getElementsByClassName('carrito-item-titulo');
    for(var i=0;i < nombresItemsCarrito.length;i++){
        if(nombresItemsCarrito[i].innerText==titulo){
            alert("El item ya se encuentra en el carrito");
            return;
        }
    }

    var itemCarritoContenido = `
        <div class="carrito-item">
            <img src="${imagenSrc}" width="80px" alt="">
            <div class="carrito-item-detalles">
                <span class="carrito-item-titulo">${titulo}</span>
                <div class="selector-cantidad">
                    <i class="fa-solid fa-minus restar-cantidad"></i>
                    <input type="text" value="1" class="carrito-item-cantidad" disabled>
                    <i class="fa-solid fa-plus sumar-cantidad"></i>
                </div>
                <span class="carrito-item-precio">${precio}</span>
            </div>
            <button class="btn-eliminar">
                <i class="fa-solid fa-trash"></i>
            </button>
        </div>
    `
    item.innerHTML = itemCarritoContenido;
    itemsCarrito.append(item);

    //Agregamos la funcionalidad eliminar al nuevo item
     item.getElementsByClassName('btn-eliminar')[0].addEventListener('click', eliminarItemCarrito);

    //Agregmos al funcionalidad restar cantidad del nuevo item
    var botonRestarCantidad = item.getElementsByClassName('restar-cantidad')[0];
    botonRestarCantidad.addEventListener('click',restarCantidad);

    //Agregamos la funcionalidad sumar cantidad del nuevo item
    var botonSumarCantidad = item.getElementsByClassName('sumar-cantidad')[0];
    botonSumarCantidad.addEventListener('click',sumarCantidad);

    //Actualizamos total
    actualizarTotalCarrito();
}
// Aumento en uno la cantidad del elemento seleccionado
function sumarCantidad(event) {
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = parseInt(selector.getElementsByClassName('carrito-item-cantidad')[0].value); // Convertir a número
    cantidadActual++; // Incrementar la cantidad
    selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
    actualizarTotalCarrito();
}

// Resto en uno la cantidad del elemento seleccionado
function restarCantidad(event) {
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = parseInt(selector.getElementsByClassName('carrito-item-cantidad')[0].value); // Convertir a número
    cantidadActual--;
    if (cantidadActual >= 1) {
        selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
        actualizarTotalCarrito();
    }
}

//Elimino el item seleccionado del carrito
function eliminarItemCarrito(event){
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();
    //Actualizamos el total del carrito
    actualizarTotalCarrito();

    //la siguiente funciòn controla si hay elementos en el carrito
    //Si no hay elimino el carrito
    ocultarCarrito();
}
//Funciòn que controla si hay elementos en el carrito. Si no hay oculto el carrito.
function ocultarCarrito(){
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    if(carritoItems.childElementCount==0){
        var carrito = document.getElementsByClassName('carrito')[0];
        carrito.style.marginRight = '-100%';
        carrito.style.opacity = '0';
        carritoVisible = false;
    
        var items =document.getElementsByClassName('contenedor-items')[0];
        items.style.width = '100%';
    }
}
// Actualizamos el total de Carrito
function actualizarTotalCarrito() {
    // Seleccionamos el contenedor carrito
    var carritoContenedor = document.getElementsByClassName('carrito')[0];
    var carritoItems = carritoContenedor.getElementsByClassName('carrito-item');
    var total = 0;

    // Recorremos cada elemento del carrito para actualizar el total
    for (var i = 0; i < carritoItems.length; i++) {
        var item = carritoItems[i];
        var precioElemento = item.getElementsByClassName('carrito-item-precio')[0];

        // Quitamos el símbolo peso y el punto de miles
        var precio = parseFloat(precioElemento.innerText.replace('$', '').replace(/\./g, '')); // Asegurarse de remover los puntos de miles

        var cantidadItem = item.getElementsByClassName('carrito-item-cantidad')[0];
        var cantidad = parseInt(cantidadItem.value); // Asegurarse de convertir a número

        total += (precio * cantidad); // Sumar el precio por la cantidad
    }

    // Redondeamos el total a 2 decimales
    total = Math.round(total * 100) / 100;

    // Actualizamos el texto del total en el carrito
    document.getElementsByClassName('carrito-precio-total')[0].innerText = '$' + total.toLocaleString("es") + ",00";
}

document.addEventListener('DOMContentLoaded', function() {
    const itemsPorPagina = 8; // Cambiado a 8 productos por página
    let paginaActual = 1;
    const items = document.querySelectorAll('.contenedor-items .item'); // Selecciona los elementos de producto
    const totalPaginas = Math.ceil(items.length / itemsPorPagina);

    // Muestra los elementos en la página actual
    function mostrarItems() {
        const inicio = (paginaActual - 1) * itemsPorPagina;
        const fin = inicio + itemsPorPagina;

        // Oculta todos los elementos
        items.forEach((item, index) => {
            if (index >= inicio && index < fin) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });

        // Actualiza la información de la página
        document.getElementById('page-info').textContent = `Página ${paginaActual} de ${totalPaginas}`;

        // Deshabilitar botones si estamos en la primera o última página
        document.getElementById('prev-page').disabled = paginaActual === 1;
        document.getElementById('next-page').disabled = paginaActual === totalPaginas;
    }

    // Manejo del botón de la página anterior
    document.getElementById('prev-page').addEventListener('click', function() {
        if (paginaActual > 1) {
            paginaActual--;
            mostrarItems();
        }
    });

    // Manejo del botón de la página siguiente
    document.getElementById('next-page').addEventListener('click', function() {
        if (paginaActual < totalPaginas) {
            paginaActual++;
            mostrarItems();
        }
    });

    // Mostrar la primera página cuando se carga el contenido
    mostrarItems();
});
// Función para verificar el stock disponible de un artículo
function verificarStock(articleId, cantidadSolicitada, callback) {
    fetch(`/verificar-stock/${articleId}/?cantidad=${cantidadSolicitada}`)
        .then(response => response.json())
        .then(data => {
            if (data.disponible) {
                callback(true); // Stock disponible
            } else {
                alert("No hay suficiente stock disponible.");
                callback(false); // Stock no disponible
            }
        })
        .catch(error => {
            console.error('Error al verificar el stock:', error);
            callback(false);
        });
}





