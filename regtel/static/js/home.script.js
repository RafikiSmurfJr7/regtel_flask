$(document).ready(function(){
    $('#table').DataTable({
        responsive:true
        
    });
});

$('#addFile').on('click', function(e){
    e.preventDefault();
    $('#addFile2').click();
});

$('#guardarRegisto').on('click', (e)=>{
    $('#formAddRegisto').submit()    
});

$("#formAddRegisto").validate({
    rules: {
      nome: {
        required: true,
      },/*
      email:{
        required: true,
        email: true
      },*/
      nTelPessoal:{
        required: true,
        number: true,
        minlength: 9,
        maxlength: 9
      },/*
      dataNasc:{
        required: true,
        date:true
      },/*
      funcao:{
        required: true,
      },*/
      entidade:{
        required: true,
      }
    },
    messages: {
      nome: {
        required: "Preenchimento obrigatório"
      },
      email:{
        required: "Preenchimento obrigatório",
        email: "Insira um endereço de email válido"
      },
      nTelPessoal:{
        required: "Preenchimento obrigatório",
        
        minlength: jQuery.validator.format("O número tem de ter pelo menos {0} algarismos!"),
        maxlength: jQuery.validator.format("O número tem de ter no maximo {0} algarismos!")
      },
      dataNasc:{
        required: "Data inválida"
      },
      funcao:{
        required: "Preenchimento obrigatório",
      },
      entidade:{
        required: "Preenchimento obrigatório",
      }

    },
    errorPlacement: function(error, element) {
        if (element.attr('name') == 'nome') {
          error.insertAfter("#inputGroupNome");
        } else if(element.attr('name') == 'email'){
            error.insertAfter("#inputGroupEmail");
        }else if(element.attr('name') == 'nTelPessoal'){
            error.insertAfter("#inputGroupNum");
        }else if(element.attr('name') == 'dataNasc'){
            error.insertAfter("#inputGroupDataNasc");
        }else if(element.attr('name') == 'funcao'){
            error.insertAfter("#inputGroupFunc");
        }else if(element.attr('name') == 'entidade'){
            error.insertAfter("#inputGroupEntidade");
        }else {
          error.insertAfter(element);
        }
      }
  });

function clickRemoveRecord(id){
    $('#btRemoverRegisto').on('click', (e)=>{
        e.preventDefault();
        location=`/delete/${id}`
    });
}

const errorToast = $('#errorToast')

$(document).ready(()=>{
    const toast = new bootstrap.Toast(errorToast)
    toast.show()
})

    

