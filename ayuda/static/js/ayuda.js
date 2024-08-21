document.addEventListener("DOMContentLoaded", function() {
    // Obtener todas las preguntas
    var questions = document.querySelectorAll(".question h3");

    // Agregar un evento de clic a cada pregunta
    questions.forEach(function(question) {
        question.addEventListener("click", function() {
            // Alternar la visibilidad del contenido de la respuesta
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    });
});