$(document).ready(()=>{
    try {
      const errorToast = $('#errorToast')
      const toast = new bootstrap.Toast(errorToast)
      toast.show()  
    }catch(err) {
      let error = err 
    }
    
})