
$("#nav-menu-btn").click(function () {
    $("#menu-bar").slideToggle(400);
});

// to adjust header according to screen size
$(document).ready(function ($) {
    var alterClass = function () {
        var ww = document.body.clientWidth;
        if (ww > 901) {
            console.log(true);
            $("#menu-bar").toggle(false, 500);
            $("#menu-bar").show()
        //  for dropdown
        $("#link-to-hover").hover(function () {
            var dataValue = "#" + $(this).attr("data")
            $(dataValue).fadeIn(400)
        }, function () {
            var dataValue = "#" + $(this).attr("data")
            $(dataValue).fadeOut(200)
        });
        }
        else {
            $("#menu-bar").hide()
            $("#link-to-hover").hover(function () {
                var dataValue = "#" + $(this).attr("data")
                $(dataValue).fadeIn(300)
            }, function () {
                var dataValue = "#" + $(this).attr("data")
                $(dataValue).fadeOut(100)
            });
        }

    };
    $(window).resize(function () {
        alterClass();
    });
    alterClass();
});



// Ye pura nav ke liye hai
