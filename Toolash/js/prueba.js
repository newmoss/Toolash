const form = document.getElementById('form');
const nombre = document.getElementById('nombres');
const apellido = document.getElementById('apellidos');
const email = document.getElementById('email');
const telefono = document.getElementById('numero');
const rut = document.getElementById('rut');
const direccion = document.getElementById('direccion');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	e.preventDefault();

	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const nombreValue = nombres.value.trim();
	const apellidoValue = apellidos.value.trim();
	const emailValue = email.value.trim();
	const telefonoValue = numero.value.trim();
	const rutValue = rut.value.trim();
	const direccionValue = direccion.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();

	if (nombreValue === '') {
		setErrorFor(nombre, 'No puede dejar el nombre en blanco');
	} else {
		setSuccessFor(nombre);
	}
	if (apellidoValue === '') {
		setErrorFor(apellido, 'No puede dejar el apellido en blanco');
	} else {
		setSuccessFor(apellido);
	}
	if (emailValue === '') {
		setErrorFor(email, 'No puede dejar el email en blanco');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'No ingreso un email válido');
	} else {
		setSuccessFor(email);
	}
	if (telefonoValue === '') {
		setErrorFor(telefono, 'No puede dejar el telefono en blanco');
	} else {
		setSuccessFor(telefono);
	}
	if (rutValue === '') {
		setErrorFor(rut, 'No puede dejar el rut en blanco');
	} else {
		setSuccessFor(rut);
	}
	if (direccionValue === '') {
		setErrorFor(direccion, 'No puede dejar la direccion en blanco');
	} else {
		setSuccessFor(direccion);
	}
	if (passwordValue === '') {
		setErrorFor(password, 'Password no debe ingresar en blanco.');
	} else {
		setSuccessFor(password);
	}
	//pass coincidan
	if (password2Value === '') {
		setErrorFor(password2, 'Password2 no debe ingresar en blanco');
	} else if (passwordValue !== password2Value) {
		setErrorFor(password, 'Passwords no coinciden');
		setErrorFor(password2, 'Passwords no coinciden');
	} else {
		setSuccessFor(password2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}