$(document).ready(function(){
    $('#table').DataTable({
        responsive:true
        
    });
});

$('#btAddUser').on('click', (e)=>{
    $('#formAddUser').submit()    
});

$("#formAddUser").validate({
    rules: {
      username: {
        required: true,
      },
      email:{
        required: true,
        email: true
      },
      password:{
        required: true,
        minlength: 8,
        maxlength: 16
      },
      confPassword:{
        equalTo: "#inputpassword"
      },
    },
    messages: {
      username: {
        required: "Preenchimento obrigatório"
      },
      email:{
        required: "Preenchimento obrigatório",
        email: "Insira um endereço de email válido"
      },
      password:{
        required: "Preenchimento obrigatório",
        
        minlength: jQuery.validator.format("A password tem de ter no mínimo {0} caracteres!"),
        maxlength: jQuery.validator.format("A password tem de ter no máximo {0} caracteres!")
      },
      confPassword:{
        equalTo: "As passwords têm de ser iguais"
      },
      

    },
    errorPlacement: function(error, element) {
        if (element.attr('name') == 'username') {
          error.insertAfter("#inputGroupUsername");
        }else if (element.attr('name') == 'email') {
          error.insertAfter("#inputGroupEmail");
        }else if (element.attr('name') == 'password') {
          error.insertAfter("#inputGroupPass");
        }else if (element.attr('name') == 'confPassword') {
          error.insertAfter("#inputGroupConfPass");
        }else {
          error.insertAfter(element);
        }
      }
  });

function clickRemoveUser(id){
  $('#btRemoverUtilizador').on('click',(e)=>{
    e.preventDefault();
    location=`/admin/delete/${id}`
  });
}


$(document).ready(()=>{
    try {
      const errorToast = $('#errorToast')
      const toast = new bootstrap.Toast(errorToast)
      toast.show()  
    }catch(err) {
      let error = err 
    }
    
})

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))