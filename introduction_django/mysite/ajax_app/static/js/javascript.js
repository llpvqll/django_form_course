 $(document).ready(function(){
        $('#add-human').submit(function(e){
            e.preventDefault();
             $.ajax({
                method : "POST" ,
                url : $(this).attr('action'),
                data: {
                    'name' : $('#id_name').val(),
                    'surname' :  $('#id_surname').val(),
                    'birth' :  $('#id_birth').val(),
                    'company' :  $('#id_company').val(),
                    'salary' :  $('#id_salary').val(),
                },
                dataType: 'json',
                success: function(data){
                     $('form')[0].reset();
                     var table_row = '<tr><td>' +
                       data.name + '</td><td>' + data.surname + '</td><td>' +
                       data.birth + '</td><td>' + data.company + '</td><td>' +
                       data.salary + '</td></tr>';

                        $('table').append(table_row);
                }
             })
        })




    function ajax_setup(e){
    e.preventDefault();
            $.ajax({
                method : 'GET' ,
                url : $(this).attr('href'),
                data: "",
                dataType: 'json',
                 success: function (data) {
                 console.log(data);
                 $("#table_id  tr:not(:first-child)").remove();
                 for(var i = 0 ; i < data.elements.length; i++)
                     {
                     var table_row = '<tr><td>' +
                       data.elements[i].name + '</td><td>' + data.elements[i].surname + '</td><td>' +
                       data.elements[i].birth + '</td><td>' + data.elements[i].company + '</td><td>' +
                       data.elements[i].salary + '</td></tr>';

                        $('table').append(table_row);

                     }
                 }

            })
        }


        $('#show_all').click(ajax_setup);
        $('#close_all').click(ajax_setup);

    $('#id_email').on('blur' , validate);
    function validate(){
      var email  =  $('#id_email').val();
      $.ajax({
        method : "GET",
        url: '/ajax_app/validate-email/',
        data: {
          'email': email
        },
        dataType: 'json',
        success: function (data) {
        console.log(data);
          if (data.is_taken) {
            $('#error-mail').text(data.is_taken);
            $('#btn').attr('disabled' , 'disabled');
            }
            else if (data.ok) {
               $('#error-mail').text('');
               $('#btn').removeAttr('disabled');
            }
          },
          error: function(data){
                console.log(data);

          }

      })
    }
  })