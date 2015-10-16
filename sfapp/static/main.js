fields = ['first_name', 'last_name', 'dob', 'zip_code'];

function validate_date(dateVal){

  var dateVal = dateVal;

  if (dateVal == null)
      return false;

  var validatePattern = /^(\d{4})(\/|-)(\d{1,2})(\/|-)(\d{1,2})$/;

      dateValues = dateVal.match(validatePattern);

      if (dateValues == null)
          return false;

  var dtYear = dateValues[1];
      dtMonth = dateValues[3];
      dtDay=  dateValues[5];

   if (dtMonth < 1 || dtMonth > 12)
      return false;
   else if (dtDay < 1 || dtDay> 31)
     return false;
   else if ((dtMonth==4 || dtMonth==6 || dtMonth==9 || dtMonth==11) && dtDay ==31)
     return false;
   else if (dtMonth == 2){
     var isleap = (dtYear % 4 == 0 && (dtYear % 100 != 0 || dtYear % 400 == 0));
     if (dtDay> 29 || (dtDay ==29 && !isleap))
            return false;
  }

 return true;
}

function validate_create() {
    // check each field
    if ($('input[name="first_name"]').val().length < 1) {
        $('#create-error').text("First Name is a required field.");
        $('#create-error').show();
        return false;
    }
    if ($('input[name="last_name"]').val().length < 1) {
        $('#create-error').text("Last Name is a required field.");
        $('#create-error').show();
        return false;
    }
    if (!validate_date($('input[name="dob"]').val())) {
        $('#create-error').text("Date of Birth format: YYYY-MM-DD.");
        $('#create-error').show();
        return false;
    }
    if ($('input[name="zip_code"]').val().length < 1 || !$.isNumeric($('input[name="zip_code"]').val())) {
        $('#create-error').text("Zip Code must be numeric.");
        $('#create-error').show();
        return false;
    }


    $('#create-error').hide();
    return true;
}

$(function() {
    $('#data').editableTableWidget();

    // validation
    $('#data td').on('validate', function(event, newvalue) {
        var td = $(this);
        var field = fields[td.index()];

        if (field == 'zip_code') {
            if (!$.isNumeric(newvalue)) return false;
        }
        if (field == 'dob') {
            // format must be year-month-day
            return validate_date(newvalue);
        }
    });



    // on change
    // first_name, last_name, dob, zip_code
    $('#data td').on('change', function(event, newvalue) {
        var td = $(this);
        var field = fields[td.index()];
        var person_id = td.closest('tr').attr("name");
        //console.log(person_id + ' ' + field + ': ' + newvalue);
        //console.log(event);

        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({id: parseInt(person_id), field: field, value: newvalue}),
            dataType: 'json',
            url: '/update',
            success: function(e) {
                console.log(e);
            }
        })
    });

    // delete
    $('.del').on('click', function(event) {
        var person_id = $(this).closest('tr').attr("name")
        if (confirm("Are you sure you want to delete this row?")) {
            $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({id: parseInt(person_id)}),
                dataType: 'json',
                url: '/delete',
                success: function(e) {
                    window.location.reload()
                }
            });
        }
    });

    $('#add').on('click', function(event) {
        $('#create').toggle("slide", { direction: "right" }, 500);
    });

    $('#close').on('click', function(event) {
        $('#create').toggle("slide", { direction: "right" }, 500);
    })

    //$('input[name="submit"]').on('click', function(event) {
    //    validate_create();
    //})

    $('#create input[type="submit"]').click(function(event) {
        if(validate_create()) {
            // if the form validates, let's submit it
            // gather data
            var first_name = $('#create input[name="first_name"]').val()
            var last_name = $('#create input[name="last_name"]').val()
            var dob = $('#create input[name="dob"]').val()
            var zip_code = $('#create input[name="zip_code"]').val()
            $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({first_name: first_name, last_name: last_name, dob: dob, zip_code: parseInt(zip_code)}),
                dataType: 'json',
                url: '/create',
                success: function(e) {
                    window.location.reload();
                }
            });
        }
    })
})
