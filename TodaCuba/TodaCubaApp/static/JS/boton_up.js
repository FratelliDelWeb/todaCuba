document.getElementById("boton_subir").addEventListener("click", scrollUp);

function scrollUp() {
    var desplazamiento = document.documentElement.scrollTop;
    if (desplazamiento > 0) {
        window.requestAnimationFrame(scrollUp);
        window.scrollTo(0, desplazamiento - (desplazamiento / 10));
    }

}

botonUP = document.getElementById("boton_subir");

window.onscroll = function() {
    var scroll = document.documentElement.scrollTop;

    if (scroll > 800) {
        botonUP.style.transform = "scale(1)";
    } else if (scroll < 800) {
        botonUP.style.transform = "scale(0)";
    }

}


$(document).ready(function() {
    // Selecciona todas las miniaturas
    var miniaturas = $('.miniatura');
    
    // Agrega un controlador de eventos para cada miniatura
    miniaturas.on('click', function() {
      // Obtiene el ID de la casa correspondiente
      var casaId = $(this).attr('id').split('-')[1];
      
      // Obtiene el número de la miniatura clickeada
      var miniaturaNum = $(this).attr('id').split('-')[2];
      
      // Obtiene la URL de la miniatura clickeada
      var url = $(this).attr('src');
      
      // Cambia la fuente de la imagen principal correspondiente a la miniatura clickeada
      $('#imagen-principal-' + casaId).attr('src', url);
    });
  });