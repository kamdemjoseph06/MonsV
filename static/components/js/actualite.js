$(document).ready(function() {
    // $('.lastStory').on('click', function() {
    //     $('.lastStoryMenu').toggle();
    //     $('.video').show(550);
    //     $('.videoContent').hide();
    //     $('.image').show(550);
    //     $('.imageContent').hide();
    // });

    $('.pagination').on('click', function() {
        $('.videoContent').show();
    });

    $('.barMenux').off('click').on('click', function() {
        $('.barMenu').toggle(700);
        $('.barMenux').hide(700);
        $('.navMenu').hide(700);
    });


    $('.barMenu').off('click').on('click', function() {
        $('.barMenu').hide(450);
        $('.barMenux').show(550);
        $('.navMenu').show(550).css('position', 'absolute').css('z-index', ' 9999').css('flex-direction', 'column').css('', '').css('', '').css('', '').css('', '');
    });

    // $('.lastStory').on('click', function() {
    //     $('.lastStoryMenu').show(550).css('margin-top', '1.3em');
    //     $('.video').show(550);
    //     $('.videoContent').hide();
    // });

    // $('.video').on('click', function() {
    //     $('.videoContent').toggle(550).css('margin-top', '1.3em');
    // });

    // $('.image').on('click', function() {
    //     $('.imageContent').toggle(550).css('margin-top', '1.3em');
    // });






    setInterval(() => {
        fetch('/actualite')
            .then(res => res.json())
            .then(data => console.log(data));
        alert(data)
    }, 3000); // toutes les 3 secondes

});