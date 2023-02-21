//abrir input de ficheiro para submeter fotografias
$('#file1').on('click',(e) => {
    e.preventDefault();
    $('#file2').click();
});
/*
$('#btEditarSobre').on('click',(e)=>{
    e.preventDefault();
    
    id = $('#btEditarSobre').attr('reg-id')
    text = $('#textSobre').val()
    if(text == '')return
    for(c = 0;c<text.length;c++){

        if(text[c] == '\n'){
            text = text.replace('\n', '<br>')
        }
    }
    $.ajax({
        type: "POST",
        url: `/profile/edit/about/${id}`,
        data: {
            'id':id,
            'text':text
        },
        dataType: "json",
        success: (data)=> {
            
        }
    });


    if($('#textSobre').val() != 0)
        $('#sobre').html(text)  
    
});*/

$('#btEditarSobre').on('click',(e)=>{
    e.preventDefault();
    $('#formEditSobre').submit();

})

$("#formEditSobre").validate({
    rules:{
        sobre:{
            required:true,
        },
    },
    messages:{
        sobre:{
            required: 'Campo obrigatório'
        }
    }

    

});

$('#btEditarDados').on('click',(e)=>{
    e.preventDefault();
    $('#formEditData').submit();
});

$('#formEditData').validate({
    rules:{
        nome:{
            required:true,
        },
        email:{
            required:false,
            email:true,
        },
        telemovel:{
            required: true,
            number: true,
            minlength: 9,
            maxlength: 9
        },
        entidade:{
            required:true
        }
    },
    messages:{
        nome:{
            required: 'Campo obrigatório'
        },
        telemovel:{
            required: "Preenchimento obrigatório",
            minlength: jQuery.validator.format("O número tem de ter pelo menos {0} algarismos!"),
            maxlength: jQuery.validator.format("O número tem de ter no maximo {0} algarismos!")
        },
        entidade:{
            required:'Campo obrigatório'
        },
        email:{
            email:'Insira um endereço de email valido',
        },
    },
    errorPlacement: function(error, element) {
        if (element.attr('name') == 'nome') {
          error.insertAfter("#inputGroupNome");
        }else if(element.attr('name') == 'telemovel'){
            error.insertAfter("#inputGroupTel");
        }else if(element.attr('name') == 'entidade'){
            error.insertAfter("#inputGroupEntidade");
        }else {
          error.insertAfter(element);
        }
      }
});

$('#btRemoverSobre').on('click',()=>{
    let id = $('#btRemoverSobre').attr('reg-id')
    location.href=`/profile/delete/about/${id}`
});

$(document).ready(()=>{
    try{
        const errorToast = $('#errorToast')
        const toast = new bootstrap.Toast(errorToast)
        toast.show()
    }catch(err){
        let error = err
    }
    
})