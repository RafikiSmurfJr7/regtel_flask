$(document).ready(()=>{

    $('#msgToast').toast({
        delay: 2000
    })
    $('#msgToast').toast('show')
})

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))