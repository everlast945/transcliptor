$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('sidebar').toggleClass('active');
        $('content').toggleClass('active_sidebar');
        $('header').toggleClass('active_sidebar');
    });

});