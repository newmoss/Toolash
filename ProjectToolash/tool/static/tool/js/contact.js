$("#mi-formulario").validate({
    rules: {
        nombres: {
            required: true,
            minlength: 3
        },
        apellidos: {
            required: true,
            minlength: 3
        },
        email: {
            required: true,
            email: true
        },
        asunto: {
            required: true,
            minlength: 3
        },
        mensaje: {
            required: true,
            
        }
    }, //rules
    messages: {
        nombres: {
            required: 'Ingrese su nombre',
            minlength: 'Caracteres insuficientes'
        },
        apellidos: {
            required: 'Ingrese su apellido',
            minlength: 'Caracteres insuficientes'
        },
        email: {
            required: 'Ingresa un correo',
            email: 'Formato de correo no válido'
        },
        asunto: {
            required: 'Ingrese un asunto',
            minlength: 'Cantidad de digitos insuficiente'
        },
        mensaje: {
            required: 'Ingrese un mensaje'
        }
    }//messages
}); //$('#mi-formulario').validate


$("#guardar").click(function () {
    if ($("#mi-formulario").valid() == false) {
        return;
    }

    let nombres = $("#nombres").val()
    let apellidos = $("#apellidos").val()
    let email = $("#email").val()
    let asunto = $("#asunto").val()
    let mensaje = $("#mensaje").val()
})

