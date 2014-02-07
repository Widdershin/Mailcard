$(document).ready(function () {
    $(".column-cards").sortable();
    
    function displayMessages () {
        $.getJSON('/api/messages', function ( data ) {
            var messageHTML = "";
            $.each(data["messages"], function (key, val) {
                console.log(val);
                messageHTML += "<div class='card'>" + val["from"]["name"] + "</br>" + val["subject"] + "</div>";
            })

            $(".column-cards").append(messageHTML);
        });
    }

    displayMessages();

    $("#update").click(function () {

        $.post('/api/messages/update', function () {
            $(".column-cards").empty();
        });
        displayMessages();
    })
});