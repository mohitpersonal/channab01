$(document).on('click', '#pills-daily-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Daily");
    console.log("sessionStorage is ---------->", set_value)

})
//
$(document).on('click', '#pills-Weekly-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Weekly");

})
//


$(document).on('click', '#pills-Monthly-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Monthly");
})

//
$(document).on('click', '#pills-Yearly-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Yearly");

})
//


//

$(document).ready(function () {
    var milk_tab = sessionStorage.getItem('milk_tab');
    console.log(milk_tab)
    if (milk_tab == 'Daily') {
        $('#pills-daily-tab').addClass("active");
        $('#pills-Weekly-tab').removeClass("active");
        $('#pills-Monthly-tab').removeClass("active");
        $('#pills-Yearly-tab').removeClass("active");

        $('#Health').addClass("show active");
        $('#Weekly').removeClass("show active");
        $('#Monthly').removeClass("show active");
        $('#Yearly').removeClass("show active");
        sessionStorage.clear();
        
    }
   if (milk_tab == 'Weekly') {
         $('#pills-daily-tab').removeClass("active");
        $('#pills-Weekly-tab').addClass("active");
        $('#pills-Monthly-tab').removeClass("active");
        $('#pills-Yearly-tab').removeClass("active");


        $('#Health').removeClass("show active");
        $('#Weekly').addClass("show active");
        $('#Monthly').removeClass("show active");
        $('#Yearly').removeClass("show active");
        sessionStorage.clear();
        
    }
    if (milk_tab == 'Monthly') {
        $('#pills-daily-tab').removeClass("active");
        $('#pills-Weekly-tab').removeClass("active");
        $('#pills-Monthly-tab').addClass("active");
        $('#pills-Yearly-tab').removeClass("active");

        $('#Health').removeClass("show active");
        $('#Weekly').removeClass("show active");
        $('#Monthly').addClass("show active");
        $('#Yearly').removeClass("show active");
        sessionStorage.clear();
    }
    if (milk_tab == 'Yearly') {
        $('#pills-daily-tab').removeClass("active");
        $('#pills-Weekly-tab').addClass("active");
        $('#pills-Monthly-tab').removeClass("active");
        $('#pills-Yearly-tab').removeClass("active");

        $('#Health').removeClass("show active");
        $('#Weekly').removeClass("show active");
        $('#Monthly').removeClass("show active");
        $('#Yearly').addClass("show active");
        sessionStorage.clear();
 
    }
 
})


