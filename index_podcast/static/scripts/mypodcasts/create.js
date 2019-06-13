$('#add-form').submit(function (e) {
    let formData = new FormData($(this));
    formData.append('title', $('#title')[0].value);
    formData.append('image', $('#image')[0].files[0]);
    formData.append('description', $('#description')[0].value);
    $.ajax({
        url: '/mypodcasts/api/podcasts/',
        type: 'POST',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: (response) => {
            console.log(response);
            alert("Podcast has been created!");
            $(location).attr('href', '/');
        },
        error: (response) => {
            console.log(response)
        }
    });
    e.preventDefault();
});