$(document).ready(function() {
    // $('.btn_connect').on('click', function() {
    //     $('.btn_connect').hide();
    //     $('.form-souscri').hide();
    //     $('.form-connection').show(750);
    //     $('.form-connection').css('display', 'flex').css('justify-content', 'center')
    //     $('.btn_souscri').show();
    //     $('.btn_connect_inscri').show();
    //     $('.alert_forgot').hide();
    // });
    ///////////////////////////////////////////////////////////

    // Bouton de connexion et ses cas -- Connexion à l accueil

    $('.btn_connection').on('click', function() {
        const PassUserjs = $('.PassUser').val()
        const NomUserjs = $('.NomUser').val()
        if (NomUserjs == '' && PassUserjs == '') {
            $('.btn_connect').show();
            $('.form-souscri').show(650);
            $('.form-connection').hide();
            $('.btn_connect_inscri').hide();
        } else if (NomUserjs == '' && PassUserjs !== '') { $('.NomUser').css('border-bottom-color', 'rgb(255,72, 72)'); } else if (NomUserjs != '' && PassUserjs == '') { $('.PassUser').css('border-bottom-color', 'rgb(255,72, 72)'); }
        //else{alert(NomUserjs);alert(PassUserjs)}

    });
    ////////////////////////////////////////////////////////////

    // function inscrire() {
    //     alert('Bonjour')
    //     $('.btn_connect').show();
    //     $('.form-souscri').hide();
    //     $('.form-connection').show();
    //     $('.btn_souscri').show();
    //     $('.btn_connect_inscri').hide();
    //     // $('.btnInscrire').on('click', function() {
    //     //     $('.btn_connect').show();
    //     //     $('.form-souscri').hide();
    //     //     $('.form-connection').show();
    //     //     $('.btn_souscri').show();
    //     //     $('.btn_connect_inscri').hide();
    //     // });
    // }

    // $('.btn_connect').on('click', function() {
    //     $('.form-connection').show()
    //     // var fenetre='../html/Connection.html'
    //     // window.open(fenetre)
    //     // if (window.open(fenetre)){}
        
    // });





    $('.btn_connect_inscri').on('click', function() {
        $('.btn_connect').show();
        $('.form-souscri').show(650);
        $('.form-connection').hide();
        $('.btn_souscri').show();
        $('.btn_connect_inscri').hide();
    });

    $('.forgot').on('click', function() {
        $('.alert_forgot').toggle(100);
        $('.cls_forgot').css('display', 'flex').css('justify-content', 'flex-end').css('font-style', 'normal').css('cursor', 'pointer').css('font-size', '20px');
        $('.alert_forgot').css('display', 'block').css('background-color', 'rgb(235, 255, 235)')
        $('.content_forgot').css('display', 'block').css('font-style', 'italic').css('line-height', '.7em;').css('margin-bottom', '1em');
    });

    $('.cls_forgot').on('click', function() {
        $('.alert_forgot').hide();
    });

    $('.btn_connection').on('click', function() {
        NomUser = $('.NomUser').val();
        $('.nomUser').text() = NomUser

        //alert(NomUser)
    });
    //////////////////////////////////////////////////////

    /*Validation Form  Inscription */
    $('#nomInscri').on('change', function() {
        $('#nomInscri').css('border-bottom-color', 'rgb(72, 72,255)')
    });
    $('.prenomInscri').on('change', function() {
        $('.prenomInscri').css('border-bottom-color', 'rgb(72, 72,255)')
    });
    $('.dateInscri').on('change', function() {
        $('.dateInscri').css('border-bottom-color', 'rgb(72, 72,255)')
    });
    $('.codeInscri').on('change', function() {
        $('.codeInscri').css('border-bottom-color', 'rgb(72, 72,255)')
    });
    $('.MotPasseInscri').change(function() {
        if ($('.MotPasseInscri').val == '') { $('.MotPasseInscri').css('border-bottom-color', 'rgb(255,72, 72)') } else { $('.MotPasseInscri').css('border-bottom-color', 'rgb(72, 72,255)') }
    })


    function data() {
        $('.btn_souscri').on('click', function() {

            const nomsInscrijs = $('.nomsInscri').val();
            const prenomInscrijs = $('.prenomInscri').val();
            const dateInscrijs = $('.dateInscri').val();
            const codeInscrijs = $('.codeInscri').val();
            const MotPasseInscrijs = $('.MotPasseInscri').val()

            if (nomsInscrijs != '' && prenomInscrijs != '' && dateInscrijs != '' && codeInscrijs != '' && MotPasseInscrijs != '') { alert('Val') }
            if (nomsInscrijs == '' && prenomInscrijs == '' && dateInscrijs == '' && codeInscrijs == '' && MotPasseInscrijs == '') {
                $('.inpt_souscri').css('border-bottom-color', 'rgb(255,72, 72)')
            }
            eel.inscription(nomsInscrijs, prenomInscrijs, dateInscrijs, codeInscrijs, MotPasseInscrijs)
            eel.hello('Ok')
        });
    }


    ////////////////////////////////////////////////////

    ////*  */////





    ////////////////////////////////////////////

    /*Paramètres*/

    $('.modifMotPasse').on('click', function() {
        $('.formMotPasse').toggle(250);
    });

    $('.modifGalerie').on('click', function() {
        $('.formModifGalerie').toggle(250);
        $('.formSuppGalerie').hide();
    });

    $('.suppGalerie').on('click', function() {
        $('.formSuppGalerie').toggle(250);
        $('.formModifGalerie').hide();
    });
    //////////

    $('.modifProfil').on('click', function() {
        $('.formModifProfil').toggle(250);
        $('.formSuppProfil').hide();
    });

    $('.suppProfil').on('click', function() {
        $('.formSuppProfil').toggle(250);
        $('.formModifProfil').hide();
    });
    //////////

    $('.modifTel').on('click', function() {
        $('.formModifTel').toggle(250);
        $('.formSuppTel').hide();
    });

    $('.suppTel').on('click', function() {
        $('.formSuppTel').toggle(250);
        $('.formModifTel').hide();
    });
    ////////////

    $('.modifPhoto').on('click', function() {
        $('.formModifPhoto').toggle(250);
        $('.formSuppPhoto').hide();
    });

    $('.suppPhoto').on('click', function() {
        $('.formSuppPhoto').toggle(250);
        $('.formModifPhoto').hide();
    });
    ///////

    $('.carousel').carousel()
    



});