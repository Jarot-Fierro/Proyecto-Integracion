const messageAlert = document.querySelector('.alert');
const buttonCloseAlert = document.querySelector('.close');

buttonCloseAlert.addEventListener('click', ()=>{
    messageAlert.classList.add('display-none')
})