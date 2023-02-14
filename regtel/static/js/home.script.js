$(document).ready(function(){
    $('#table').DataTable({
        responsive:true
        
    });
});

$('#addFile').on('click', function(e){
    e.preventDefault();
    $('#addFile2').click();
});

$('#guardarRegisto').on('click', ()=>{
    

    let nome = $('#formAddRegisto input[name=nome').val();

    let email = $('#formAddRegisto input[name=email').val();
    
    let date = $('#formAddRegisto input[name=date').val();

    let nPessoal = $('#formAddRegisto input[name=nTelPessoal').val();

    let nTrab = $('#formAddRegisto input[name=nTelTrab').val();

    let funcao = $('#formAddRegisto input[name=funcao').val();

    let entidade = $('#formAddRegisto input[name=entidade').val();
    
    var arr = [nome,email,date,nPessoal,nTrab,funcao,entidade]

    for(c=0;c<=arr.length;c++){
        if(arr[0].length < 0){
            return
        }
    }
    
    $('#formAddRegisto').submit()
});
