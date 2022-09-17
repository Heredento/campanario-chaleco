// selección de plantillas de eventos
function seventos() { // nombre funcion
    var value = $('#evento').val(); // id del select
    var div = $("#eventosid"); //id del contenido
    switch (value){
        case "1":
            div.html('<input class="set-time" type="time" name="time" required>');
            break;
        case "2":
            div.html('<input class="set-time" type="time" name="time" required>');
            break;

        case "3":
            div.html('<input class="set-time" type="time" name="time" required>');
            break;

        case "4":
            div.html('<input class="set-time" type="datetime-local" name="time" required>');
            break;

        case "5":
            div.html('<input type="week" class="set-time" name="week" required> <input type="time" class="set-time" name="time" required>'
            );
            break;
    }
  }

// canciones