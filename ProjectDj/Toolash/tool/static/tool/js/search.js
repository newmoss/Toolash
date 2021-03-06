const form = document.getElementById('form');
const search = document.getElementById('search');

form.addEventListener('submit', e => {

	checkInputs(e);
});

function checkInputs(e) {
	// trim to remove the whitespaces

	const searchValue = search.value.trim();

	if (searchValue === '') {
		e.preventDefault();
		setErrorFor(search, 'Rellenar campo');
		
	} else {
		setSuccessFor(search);
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
