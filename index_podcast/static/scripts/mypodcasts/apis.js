function GetPodcasts(params) {
    let p = {
        dataType: "json",
        url: "/mypodcasts/api/podcasts/",
        cashe: false
    };
    Object.assign(p, params);
    $.ajax(p);
}

function GetPodcast(id, success, error) {
    $.getJSON(`/mypodcasts/api/podcasts/${id}/`, data => {
        console.log(data);
        if(success)
            success(data);
    }).fail(resp =>{
        if(error)
            error(resp);
    });
}

function PatchPodcast(id, item, success, error) {
    let formData = new FormData();
    for (let i in item) formData.append(i, item[i]);
    $.ajax({
        url: `/mypodcasts/api/podcasts/${id}/`,
        type: "PATCH",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: response => {
            console.log(response);
            if(success)
                success(response);
        },
        error: response => {
            console.log(response);
            if(error)
                error(response);
        }
    });
}

function PatchEpisode(id, item, success, error) {
    let formData = new FormData();
    for (let i in item) formData.append(i, item[i]);
    $.ajax({
        url: `/mypodcasts/api/episodes/${id}/`,
        type: "PATCH",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: response => {
            console.log(response);
            if(success)
                success(response);
        },
        error: response => {
            console.log(response);
            if(error)
                error(response);
        }
    });
}

function DeleteEpisode(id, success, error) {
    $.ajax({
        url: `/mypodcasts/api/episodes/${id}/`,
        type: "DELETE",
        cache: false,
        success: () => {
            if(success)
                success();
        },
        error: response => {
            console.log(response);
            if(error)
                error(response);
        }
    });
}

function DeletePodcast(id, success, error) {
    $.ajax({
        url: `/mypodcasts/api/podcasts/${id}/`,
        type: "DELETE",
        cache: false,
        success: () => {
            if(success)
                success();
        },
        error: response => {
            console.log(response);
            if(error)
                error(response);
        }
    });
}