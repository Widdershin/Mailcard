$(document).ready(function () {
    $(".column-cards").sortable();
    
    $.getJSON('/api/messages', function ( data ) {
        var messageHTML = "";
        $.each(data["messages"], function (key, val) {
            console.log(val);
            messageHTML += "<div class='card'>" + val["from"]["name"] + "</br>" + val["subject"] + "</div>";
        })

        $(".column-cards").append(messageHTML);
    });
});