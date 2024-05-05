let count = 1;
$(document).ready(function () {
    $('#add_item').click(function () {
        count++;
        $("#count").text(count);
        $('ul.my_list').append('<li>Item</li>');
    });
    $('#remove_item').click(function () {
        count--;
        $("#count").text(count);
        $('ul.my_list li').last().remove();
    });
    $('#clear_list').click(function () {
        count = 0;
        $("#count").text(count);
        $('ul.my_list').empty();
    });
    
});