new WOW().init();

var wow = new WOW(
    {
        boxClass: 'wow',      // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset: 0,          // distance to the element when triggering the animation (default is 0)
        mobile: true,       // trigger animations on mobile devices (default is true)
        live: true,       // act on asynchronously loaded content (default is true)
        callback: function (box) {
            // the callback is fired every time an animation is started
            // the argument that is passed in is the DOM node being animated
        },
        scrollContainer: null // optional scroll container selector, otherwise use window
    }
);
wow.init();


const url_of_this_page = window.location.href;


// takes care of voting
function vote_here(name, value) {
    let data = {
        Name: name,
        Value: value
    };
    $(document).ready(function () {
        $.ajax({
            type: "POST",
            url: url_of_this_page,
            dataType: 'json',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            data: JSON.stringify(data),

            success: function () {
                console.log("up voottteeeee!!!!")
            },
            error: {
                function() {
                    console.log("#.ajax == failure");
                },
            },
        });

    });

    let current_number = parseInt(document.getElementById(value).innerText);

    if (name === 'up_voted_It') {
        current_number = current_number + 1;
        document.getElementById(value).innerHTML = (current_number);
    } else if (name === 'down_voted_It') {
        current_number = current_number - 1;
        document.getElementById(value).innerHTML = (current_number);
    } else {

    }
}




function comment(name, post_ID) {

    let data = {
        Name: name,
        post_ID: post_ID,
        Comment: document.getElementById(post_ID + "_comment").value,
    };
    console.log(data);


    $(document).ready(function () {
        $.ajax({
            type: "POST",
            url: url_of_this_page,
            dataType: 'json',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            data: JSON.stringify(data),

            success: function () {
                console.log("success")
            },
            error: {
                function() {
                    console.log("#.ajax == failure");
                },
            },
        });

    });
}





// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');

// gets how much characters are left
let maxLength = 240;
$('#main-text').keyup(function () {
    let length = $(this).val().length;
    let lengths = maxLength - length;
    $('#chars').text(lengths);
});

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}