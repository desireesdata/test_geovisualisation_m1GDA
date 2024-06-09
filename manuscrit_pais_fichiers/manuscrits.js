function initmanuscrits() {
    pag('manuscrits');

    $(document).ready(function() {
        $('#delcity .submit').attr('disabled', true);
        $('#dellibr .submit').attr('disabled', true);
        $('#delfons .submit').attr('disabled', true);
        $('#formcity .submit').attr('disabled', true);
    });

    $('#formcity input').keyup(function() {
        var disabled = false;
        $('.required').each(function(i,el) { if (!$(el).val()) disabled = true; });
        $('#formcity .submit').attr('disabled', disabled);
    });

    $('#delcity .del').on('click', function() {
        if ($('#delcity .del').is(":checked"))
            $('#delcity .submit').attr('disabled', false);
        else
            $('#delcity .submit').attr('disabled', true);
    });

    $('#dellibr .del').on('click', function() {
        if ($('#dellibr .del').is(":checked"))
            $('#dellibr .submit').attr('disabled', false);
        else
            $('#dellibr .submit').attr('disabled', true);
    });

    $('#delfons .del').on('click', function() {
        if ($('#delfons .del').is(":checked"))
            $('#delfons .submit').attr('disabled', false);
        else
            $('#delfons .submit').attr('disabled', true);
    });
    let advertenciaciutat = document.getElementById('advertenciaciutat');
    if (advertenciaciutat) {
        preparaadvertencia(advertenciaciutat, 'city', 'input',
            "/50]");
        preparaadvertencia(advertenciaciutat, 'cityint', 'input',
            "/50]");
    }
    let advertenciabiblioteca = document.getElementById('advertenciabiblioteca');
    if (advertenciabiblioteca) {
        preparaadvertencia(advertenciabiblioteca, 'fullibr', 'input',
            "/111]");
        preparaadvertencia(advertenciabiblioteca, 'libr', 'input',
            "/11]");
        preparaadvertencia(advertenciabiblioteca, 'notes', 'textarea',
            "");
    }
    let advertenciafons = document.getElementById('advertenciafons');
    if (advertenciafons) {
        preparaadvertencia(advertenciafons, 'fons', 'input',
            "/100] Deixeu-lo en blanc si no té nom");
        preparaadvertencia(advertenciafons, 'notes', 'textarea',
            "");
    }
}
