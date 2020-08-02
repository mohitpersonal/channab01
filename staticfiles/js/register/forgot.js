function MobileforgotCheck(){
    var legal =$("#forgot_mobile_number").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#forgot_mobile_number").removeClass("has-success");
        $("#forgot_mobile_number").addClass("has-error");
        $("#forgot_mobile_label").show();
        $("#forgot_mobile_label").text("This Field is required");
        return false;
    }
    else{
        if (legal.match(letterNumber)) {
            if (legal.length > 15 || legal.length < 10) {
                $("#forgot_mobile_number").addClass("has-error");
                $("#forgot_mobile_label").show();
                $("#forgot_mobile_label").text("It must contains only 10 to 15 numbers");
                return false;
            }
            else{
                $("#forgot_mobile_number").removeClass("has-error");

                $("#forgot_mobile_label").hide();
                $("#forgot_mobile_label").text("");
                return true;
            }
        }else{
            $("#forgot_mobile_label").show();
            $("#forgot_mobile_number").addClass("has-error");
            $("#forgot_mobile_label").text("It must contains only numbers");
            return false;
        }
    }
}

$("#forgot_mobile_number").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


///////////


$(document).on('submit', '#ForgotSubmitForm', function(){
    if (MobileforgotCheck()  == true) {
        return true;
    } else {
        MobileforgotCheck();
        return false;
    }

}) 