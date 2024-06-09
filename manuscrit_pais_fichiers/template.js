function init() {
    if (lang === 'ca') {
        $('.english').hide();
        $('.catala').show();
    } else {
        $('.english').show();
        $('.catala').hide();
    }

    let link = document.getElementById('login-link');
    if (link !== null) {
        let back = window.location.pathname;
        back = back.substring(2);
        back = back.substring(back.indexOf('/') + 1);
        link.href = link.getAttribute('href') + '?back=' + back;
    }

    $(document).ready(function() {
        //   $('form:eq(1) *:input[type!=hidden],input[type!=button],input[type!=submit]:first').focus();
        $('form:eq(1) *:input:text:visible:first').focus();
    });
}

function pag(pagina) {
    $('.pag-' + pagina).each(function() {
        this.style.backgroundColor = 'rgb(24, 107, 173)';
        this.style.color = 'white';
    });
}