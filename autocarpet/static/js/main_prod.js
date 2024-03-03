document.getElementById("btn_menu").addEventListener("click" , mostrarMenu)

nav = document.getElementById("sidebar");
background_menu = document.getElementById(backMenu);

function mostrarMenu (){
    nav.style.left = "0px";
    background_menu.style.display = "block";
}

const openModal = document.querySelectorAll('.btn_CA');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal__close');
const closeModal01 = document.querySelector('.modal__close1');
const openModal1 = document.querySelectorAll('.btn_D');
const modalE = document.querySelector('.modalE');
const closeModal1 = document.querySelector('.modalE__close');
const closeModal02 = document.querySelector('.modalE__close1');



openModal.forEach((btn) => {
    btn.addEventListener("click", () => {
      modal.classList.add('modal--show');
    });
  });


closeModal.addEventListener('click', (e)=>{
    e.preventDefault();
    modal.classList.remove('modal--show');
});

closeModal01.addEventListener('click', (e)=>{
  e.preventDefault();
  modal.classList.remove('modal--show');
});


window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.classList.remove('modal--show');
    }
  });


openModal1.forEach((btn) => {
  btn.addEventListener("click", () => {
    modalE.classList.add('modal--show');
  });
});


closeModal1.addEventListener('click', (e)=>{
    e.preventDefault();
    modalE.classList.remove('modal--show');
});

closeModal02.addEventListener('click', (e)=>{
  e.preventDefault();
  modalE.classList.remove('modal--show');
});


window.addEventListener("click", (event) => {
    if (event.target === modalE) {
      modalE.classList.remove('modal--show');
    }
  });


const openModal3 = document.querySelectorAll('.btn_AG');
const modalA = document.querySelector('.modalA');
const closeModal2 = document.querySelector('.modalA__close');
const closeModal03 = document.querySelector('.modalA__close1');

openModal3.forEach((btn) => {
  btn.addEventListener("click", () => {
    modalA.classList.add('modal--show');
  });
});


closeModal2.addEventListener('click', (e)=>{
    e.preventDefault();
    modalA.classList.remove('modal--show');
});

closeModal03.addEventListener('click', (e)=>{
  e.preventDefault();
  modalA.classList.remove('modal--show');
});


window.addEventListener("click", (event) => {
    if (event.target === modalA) {
      modalA.classList.remove('modal--show');
    }
  });


  