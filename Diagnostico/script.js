/* Pregunta: ¿Cuál es la función de 'document.getElementById' en JavaScript? */ /* para ejecución del archivo */
function checkAnswer() {
    /* Pregunta: ¿Qué hace 'prompt' y cómo se puede usar en lugar de 'alert'? */ /* para notificaciones o ventanas*/
    let answer = prompt("Enter your answer:");

    /* Pregunta: ¿Cuál es el propósito de la instrucción 'if' en este fragmento de código? */ /* para condiciones*/
    if (answer.toLowerCase() === 'paris') {
        alert("Correct!");
    } else {
        alert("Try again!");
    }
}

/* Pregunta: ¿Cómo se puede manipular el DOM usando JavaScript para cambiar el contenido de un elemento? */ /* */
document.getElementById("question").innerText = "What is the capital of Spain?";