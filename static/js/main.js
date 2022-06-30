const uploadForm = document.getElementById('upload-form')
const input = document.getElementById('id_file_name')
const alerBox = document.getElementById('alert-box')
const progressBar = document.getElementById('progress-bar')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', () => {
	progressBar.classList.remove('d-none')
    const file_data = input.files[0]
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('file_name', file_data)
    $.ajax({
        type:'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: fd,
        beforeSend: function(){
        },
        xhr: function(){
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', e=>{
                    progressBar.innerHTML =`<div id="spinner-border" class="spinner-border spinner-border-sm" role="status">
                                                <span class="visually-hidden">Loading...</span>
                                            </div>
                                            <div id="spinner-grow" class="spinner-grow spinner-grow-sm" role="status">
                                                <span class="visually-hidden">Loading...</span>
                                            </div>`
            })
            return xhr
        },
        success: function(response){
            console.log('response! ',response.message)
            alerBox.innerHTML =`<div class="alert alert-info" role="alert">
                                         ${response.message}
                                </div>`
            const spinnerBorder = document.getElementById('spinner-border')
            const spinnerGrow = document.getElementById('spinner-grow')
            spinnerBorder.classList.add('d-none')
            spinnerGrow.classList.add('d-none')

            setTimeout(function() {alerBox.classList.add('d-none');},8000);
            input.value=null;
        },
        error: function(error){
            // console.log('Erro FORA DE IF ! ',error)
            if (error==undefined){
                // console.log('Erro responseJSON.message! ',error.responseJSON.message)
                alerBox.innerHTML =`<div class="alert alert-danger" role="alert">
                                            ${error.responseJSON.message}
                                    </div>`
                setTimeout(function() {alerBox.classList.add('d-none');},10000);
                progressBar.classList.add('d-none')
                input.value=null;
            } else {
                // console.log('Erro responseJSON.message! ',error.responseJSON.message)
                alerBox.innerHTML =`<div class="alert alert-danger" role="alert">
                                            ${error.responseJSON.message}
                                    </div>`
                setTimeout(function() {alerBox.classList.add('d-none');},10000);
                progressBar.classList.add('d-none')
                input.value=null;
            }
        },
        cache: false,
        contentType: false,
        processData: false,
        

    })



})
