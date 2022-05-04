$(function(){
    $('#login').on('click', function(e){
        console.log('Log')
        e.preventDefault()
        $.getJSON('/login',
            function(data){
        });
        return false;
    })
    console.log('Ok')
})