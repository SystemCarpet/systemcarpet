const inputjs = document.getElementById('login-email');
let reqEx = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/


inputjs.onchange = function (e) {
 let validEmail = reqEx.test(e.target.value) ? true : false;
    if (validEmail) {
        inputjs.classList.add('bg-green-200');
        inputjs.classList.remove('bg-red-200');
    }else{
        inputjs.classList.add('bg-red-200');
        inputjs.classList.remove('bg-green-200');
    }
    console.log(validEmail);
}

