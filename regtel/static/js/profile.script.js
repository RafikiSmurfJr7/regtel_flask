//abrir input de ficheiro para submeter fotografias
$('#file1').on('click',(e) => {
    e.preventDefault();
    $('#file2').click();
});

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
    
});
