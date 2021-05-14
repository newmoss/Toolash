const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');

form.addEventListener('submit', e => {
	
	checkInputs(e);
});

function checkInputs(e) {
	// trim to remove the whitespaces
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();


	if (emailValue === '') {
		setErrorFor(email, 'No puede dejar el email en blanco');
		e.preventDefault();
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'No ingreso un email válido');
		e.preventDefault();
	} else {
		setSuccessFor(email);
	}
	if (passwordValue === '') {
		setErrorFor(password, 'Debe ingresar una contraseña.');
		e.preventDefault();
	} else if (passwordValue.length<4){
		setErrorFor(password,'Minimo 4 digitos');
		e.preventDefault();
	} else {
		setSuccessFor(password);
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