$(document).ready(function () {
    $(".card-column").append("<div class='card'>test</div>")
    $(".card-column").append("<div class='card'>blah blah</div>")
    $(".card-column").append("<div class='card'>blah blah</div>")
    $(".card-column").append("<div class='card'>blah foo</div>")
    $(".card-column").append("<div class='card'>this one is a bit longer</div>")
    $(".card-column").sortable();
});