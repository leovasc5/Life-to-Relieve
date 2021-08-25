document.getElementById("user").focus();

function showPassword(){
    inp = document.getElementById("senha");
    if (senha.type === "password"){
        senha.type="text";
        senha.focus();
    }else{
        senha.type="password";
        senha.focus();
    }
}