var validarRegistro= function(){
    var rut = document.getElementById('rut').value;
    var nombres = document.getElementById('first_name').value;
    var apellidos = document.getElementById('last_name').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var fecha = document.getElementById('fecha').value;
    
    var validarNombre = /^[A-Z]+$/i
   
    var validarTelefono =  /^\x2b569[0-9]{8}$/i
    var hoy  = new Date();
    var fechaIn = new Date(fecha);
    hoy.setHours(0,0,0,0);
  

    if(rut == ""){
        document.getElementById('rut').focus();
        return false
    } else {
        if(email == ""){
            document.getElementById('email').focus();
            return false
        } else {
            if(nombres == ""){
                document.getElementById('first_name').focus();
                return false
            } else {
                if(apellidos == ""){
                    document.getElementById('last_name').focus();
                    return false
                } else {
                    if(telefono == ""){
                        document.getElementById('telefono').focus();
                        return false
                    } else {
                        if(fecha == ""){
                            document.getElementById('fecha').focus();
                            return false
                        } 
                    }   
                }   
            }   
        }   
    }

    if (!validarNombre.test(nombres)) {
        document.getElementById('first_name').setCustomValidity("Nombre invalido")
        return false;  
    } 

    if (!validarNombre.test(apellidos)) {
                          
        document.getElementById('last_name').setCustomValidity("Apellido invalido");
        return false;
    }
    if (!validarTelefono.test(telefono)) {
                          
        document.getElementById('telefono').setCustomValidity("Telefono invalido");
        return false;
    }
    if (fechaIn > hoy) {                    
        document.getElementById('fecha').setCustomValidity("La fecha no puede ser mayor a la de hoy");
        return false;
    }
} 