let play_index = -1;
let audio = new Audio();
let episodes = null;


function loadPodcast() {
    $.getJSON(`/mypodcasts/api/podcasts/${PODCAST_ID}`, {
        'user_id': USER_ID
    }, (data) => {
        console.log(data);
        episodes = data.episodes;
    });
}

$(loadPodcast);

$('.btn-paly').on('click', function (event) {
    event.preventDefault();
    $(this).toggleClass('icon-play');
    $(this).toggleClass('icon-pause');
    if (+this.id !== play_index) {
        play_index = +this.id;
        console.log(`play: ${play_index}`);
        audio.pause();
        audio.src = '/media/' + episodes[play_index].audio_file;
        audio.play();
    } else if (audio.paused) {
        console.log(`play: ${play_index}`);
        audio.play();
    } else {
        console.log(`pause: ${play_index}`);
        audio.pause();
    }
});