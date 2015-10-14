$(function() {
    $('#data').editableTableWidget();

    // validation

    // on change
    // first_name, last_name, dob, zip_code
    $('#data td').on('change', function(event, newvalue) {
        var td = $(this);
        var column = td.index();
        console.log(td + ' ' + column);
    })
})
