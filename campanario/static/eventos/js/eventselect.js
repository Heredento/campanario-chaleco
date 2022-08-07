// selección de plantillas de eventos
function seventos() { // nombre funcion
    var value = $('#evento').val(); // id del select
    var div = $("#eventosid"); //id del contenido
    switch (value){
        case "1":
            div.html('<input type="time" name="time" required>');
            break;
        case "2":
            div.html('<input type="time" name="time" required>');
            break;

        case "3":
            div.html('<input type="time" name="time" required>');
            break;

        case "4":
            div.html('<input type="datetime-local" name="time" required>');
            break;

        case "5":
            div.html('<input type="week" name="week" required> <input type="time" name="time" required>'
            );
            break;
    }
  }

// canciones