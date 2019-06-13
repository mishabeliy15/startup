function addPodcast(item) {
    $("#podcasts")[0].innerHTML += `
                <div class="card container-fluid" style="width: 18rem;display: inline-block">
                  <img src="/media/${item.image}" class="card-img-top" alt="...">
                  <div class="card-body">
                    <h5 class="card-title">${item.title}</h5>
                    <p class="card-text">${item.description}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                  </div>
                </div>`;
}

$(() => {
    $.getJSON("/mypodcasts/api/podcasts/", (data) => {
        $("#podcasts").empty();
        console.log(data);
        data.results.forEach(i => addPodcast(i));
    });
});