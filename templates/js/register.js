document.getElementById("user").focus();

function showPassword(n){
    inp = document.getElementById("senha");
    inp2 = document.getElementById("senha2")
    if(n == 1){
        if (inp.type === "password"){
            inp.type="text";
            inp.focus();
        }else{
            inp.type="password";
            inp.focus();
        }
    }else if(n == 2){
        if (inp2.type === "password"){
            inp2.type="text";
            inp2.focus();
        }else{
            inp2.type="password";
            inp2.focus();
        }
    }
    
}