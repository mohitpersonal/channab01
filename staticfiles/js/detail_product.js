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




//////


//
var radios = document.getElementsByName('star');

for (var i = 0, length = radios.length; i < length; i++) {
  if (radios[i].checked) {
    // do whatever you want with the checked radio
    alert(radios[i].value);

    // only one radio can be logically checked, don't check the rest
    break;
  }
}
///////////////
$(document).on('submit','#ajax_comment_form', function(e){
    if (CommentAdd() == true){
        if ($('#star1:checked').length > 0) {
           var star_count = 1
        }
        else if($('#star2:checked').length > 0){
            var star_count = 2
        }
        else if($('#star3:checked').length > 0){
            var star_count = 3
        }
        else if($('#star4:checked').length > 0){
            var star_count = 4
        }
        else if($('#star5:checked').length > 0){
            var star_count = 5
        }

        $(".loader").show();
        e.preventDefault();
        

        var formdata = new FormData();
        var star_count =  star_count;
        var text_area = $("#comments").val();
        var post_id = $("#post_id").val();
        type_dict = {} ; 
        type_dict['star_count'] = star_count ;
        type_dict['text_area'] = text_area ;
        type_dict['post_id'] = post_id ;
        formdata.append('type_dict', JSON.stringify(type_dict));
        

        var Url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            data: formdata,
            url: Url,
            cache : false,
            processData : false, 
            contentType : false,
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




/////

