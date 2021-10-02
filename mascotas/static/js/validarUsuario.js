  
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono:  /^\x2b569[0-9]{8}$/i, // 7 a 14 numeros.
    rut: /^[0-9]{6,8}[-|‐]{1}[0-9kK]{1}$/,
}

const campos = {

    rut: false,
    nombre: false,
    apellido: false,
	correo: false,
	telefono: false,
	fecha: false
}

const validarFormulario = (e) => {
	switch (e.target.id) {

        case "rut":
			validarCampo(expresiones.rut, e.target, 'rut');
		break;
        case "nombre":
			validarCampo(expresiones.nombre, e.target, 'nombre');
		break;
        case "apellido":
			validarCampo(expresiones.nombre, e.target, 'apellido');
		break;
		case "correo":
			validarCampo(expresiones.correo, e.target, 'correo');
		break;
		case "telefono":
			validarCampo(expresiones.telefono, e.target, 'telefono');
		break;
		case "fecha":

			validarFecha();
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}


const validarFecha = () => {
	const inputFecha = document.getElementById('fecha').value;
	const hoy  = new Date();
	const fechaIn = new Date(inputFecha);
	hoy.setHours(0,0,0,0);

	if(fechaIn > hoy){
		document.getElementById(`grupo__fecha`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__fecha`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__fecha i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__fecha i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__fecha .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos['fecha'] = false;
	} else {
		document.getElementById(`grupo__fecha`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__fecha`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__fecha i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__fecha i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__fecha .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos['fecha'] = true;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
	


	if(campos.rut && campos.nombre && campos.apellido && campos.correo && campos.telefono && campos.fecha){
		
		return true
	} else {
		return false
	}
});


    
