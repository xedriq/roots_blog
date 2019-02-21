$(document).ready(function(){
    
    $('#add-comment').each(function () {
        $(this).on('click', function (e) {                   
            e.preventDefault();
            var url = $(this).attr('href'); 
            $.get(url, function (data) {
                $('#comment-form .content').html(data);
                $("#comment-form").modal({closable:true,observeChanges:true}).modal('show');
            });
        });              
    });
});