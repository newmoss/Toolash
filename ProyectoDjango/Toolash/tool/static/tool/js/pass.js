const form = document.getElementById('form');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {

	checkInputs(e);
});

function checkInputs(e) {
	// trim to remove the whitespaces

	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();

	if (passwordValue === '') {
		setErrorFor(password, 'Debe ingresar una contraseña.');
		e.preventDefault();
	} else {
		setSuccessFor(password);
	}
	//pass coincidan
	if (password2Value === '') {
		setErrorFor(password2, 'Debe ingresar una contraseña nuevamente');
		e.preventDefault();
	} else if (passwordValue !== password2Value) {
		setErrorFor(password, 'Las contraseñas no coinciden');
		e.preventDefault();
		setErrorFor(password2, 'Las contraseñas no coinciden');
		e.preventDefault();
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
