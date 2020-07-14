function CommentAdd(){
    var phone = $("#comments").val()
    if (phone.length == null || phone.length == '') {
        $("#comments").removeClass("has-success");
        $("#comments").addClass("has-error");
        $("#comment_text_label").show();
        $("#comment_text_label").text("required");
        return false;
    } else {
        $("#comments").addClass("has-success");
        $("#comment_text_label").hide();
        $("#comment_text_label").text("");
        return true;
    }
}

///////


$(document).on('submit','#ajax_comment_form', function(e){
    if (CommentAdd() == true){
        $(".loader").show();
        e.preventDefault();
        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success: function (data) {
                console.log(data);
                $(".loader").hide();
                var response = JSON.parse(data);
                window.location.reload();
            },
            error: function () {
                window.location.reload();
            }
        });
    }
    else{
        CommentAdd();
        return false;
       
    }
})
