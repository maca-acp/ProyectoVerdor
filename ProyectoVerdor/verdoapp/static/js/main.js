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
