const q = document.querySelector('.q')

function handleEvent(e) {
	if (e.keyCode === 113) {
		q.classList.add('active');
	}
}

q.addEventListener('keyup', handleEvent)