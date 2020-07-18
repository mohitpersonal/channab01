  function PasswordLogin(){
    var password= $("#loginPassword").val();
    if(password.length == '' || password.length == null) {
        $("#loginPassword").addClass("has-error");
        $("#login_password_label").show();

        $("#login_password_label").text("This Field is required");
        return false;
    }
    else{
        if(password.length < 6){
            $("#loginPassword").addClass("has-error");
            $("#login_password_label").show();

            $("#login_password_label").text("It must contains minmum 6 characters");
            return false;
        }
        else{
        
        $("#loginPassword").removeClass("has-error");
        $("#login_password_label").hide();
        $("#login_password_label").text("");
        return true;
        }
        }
    }
$("#loginPassword").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

///////////////
function MobileLoginCheck(){
    var legal =$("#login_mobile_number").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#login_mobile_number").removeClass("has-success");
        $("#login_mobile_number").addClass("has-error");
        $("#mobile_login_label").show();
        $("#mobile_login_label").text("This Field is required");
        return false;
    }
    else{
        if (legal.match(letterNumber)) {
            if (legal.length > 15 || legal.length < 10) {
                $("#login_mobile_number").addClass("has-error");
                $("#mobile_login_label").show();
                $("#mobile_login_label").text("It must contains only 10 to 15 numbers");
                return false;
            }
            else{
                $("#mobile_login_label").removeClass("has-error");

                $("#mobile_login_label").hide();
                $("#mobile_login_label").text("");
                return true;
            }
        }else{
            $("#mobile_login_label").show();
            $("#login_mobile_number").addClass("has-error");
            $("#mobile_login_label").text("It must contains only numbers");
            return false;
        }
    }
}

$("#login_mobile_number").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


///////////


$(document).on('submit', '#loginFormSubmit', function(){
    if (PasswordLogin()  &&
        MobileLoginCheck() == true) {
        return true;
    } else {
        PasswordLogin();
        MobileLoginCheck();

        return false;
    }

}) 

