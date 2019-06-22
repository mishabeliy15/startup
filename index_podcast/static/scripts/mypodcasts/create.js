function restorePodcastHeader() {
    $("#content")[0].innerHTML = ` <header>
        <div class="header-center">
            <input id="search-request" class="input-name" type="text" name="search podcasts" value="" maxlength="25" placeholder="Search">
            <input class="input-name-btn" type="button" name="button search" value="&#128269;">
        </div>
        <div class="header-right">
            <input class="add-podcast-btn" type="button" name="button search" value="Сreate a new podcast">
        </div>
    </header>
    <div id="podcast-list" class="podcast-blox">
    </div>`;
    $(".add-podcast-btn").on("click", addPodcast);
    $("#search-request").bind("input", () => drawPodcasts());
}

function get_podcast_url(item) {
    return `/podcasts/user_${item.owner}/${item.id}/`;
}
function get_podcast_edit_url(item) {
    return `/mypodcasts/${item.id}/`;
}

function drawPodcastBlock(item) {
    return `
        <div class="podcast-block">
            <img class="podcast-img" src="/media/${
                item.image
            }" alt="podcast-img">
            <div class="podcast-content">
                <div class="podcast-title">
                    ${item.title}
                </div>
                <div class="podcast-count-episod">
                    ${item.episodes.length}
                </div>
            </div>
            <div class="edit-podcast-btns">
                <a href="${get_podcast_url(item)}">
                    <div class="view-podcast-btn"></div>
                </a>
                <a href="${get_podcast_edit_url(item)}">
                    <div class="edit-podcast-btn"></div>
                </a>
            </div>
        </div>
    `;
}

function drawAddInputs(item) {
    return `
        <div class="input-block">
            <div class="input-title"> ${item} :</div>
            <input id="input-${item}" type="text" class="input-text" required></input>
        </div>
    `;
}

function drawPodcasts(items = podcast_list.results) {
    container = document.getElementById("podcast-list");
    container.innerHTML = "";
    let find = new RegExp($("#search-request")[0].value, "i");
    for (let i = 0; i < items.length; i++)
        if (find.test(items[i].title))
            container.innerHTML += drawPodcastBlock(items[i]);
}

function getAndDraw() {
    $.getJSON("/mypodcasts/api/podcasts/", data => {
        console.log(data);
        podcast_list = data;
        restorePodcastHeader();
        drawPodcasts(data.results);
    });
}

function readURL(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();

        reader.onload = function(e) {
            $("#img-preview").attr("src", e.target.result);
            $("#img-preview").show();
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function addPodcast() {
    input_titles = ["Title", "Author"];
    content = $(".content");
    content = document.getElementById("content");
    content.innerHTML = `
                <form id="create-form" action="javascript:submitForm()">
                    <div id="input-form">
                        <div class="create-title">
                            To create a podcast you need to fill in all the fields:
                        </div>
                        <div class="input-block">
                            <div class="input-title">Сover :</div>
                            <div class="input-img">
                                <div class="input-img-text">Get a picture</div>
                                <input name="image" id="input-img" class="input-img-hidden" type="file" name="photo" accept="image/*" alt="success" required/>
                            </div>
                        </div>
                        <div class="input-subtitle">select file less than 1 megabyte</div>
                        <img class="input-block" style="display: none" id="img-preview" alt="Your cover" width="200px" height="200px" />
                    </div>
                </form>`;
    content = document.getElementById("input-form");
    for (let i = 0; i < 2; i++) {
        content.innerHTML += drawAddInputs(input_titles[i]);
    }
    content.innerHTML += `
        <div class="input-block">
            <div class="input-title">Genre :</div>
            <select id="input-Genre">
            </select>
        </div>
        <div class="input-block">
            <div class="input-title">Language:</div>
            <select id="input-Language">
            </select>
        </div>
        <div class="input-title">Description :</div>
        <textarea id="input-description" rows="8" cols="80" class="input-description" required></textarea>
        <div id="input-answ"></div>
        <div class="input-block">
            <div class="input-title">Explicit :</div>
            <input id="explicit" type="checkbox" name="" value="">
        </div>
        <button type=submit class="create-btn">Create</button>
    `;
    genres = {
        "Arts": "Arts",
        "Busines": "Busines",
        "Comedy": "Comedy",
        "Education": "Education",
        "Games & Hobbies": "Games &amp; Hobbies",
        "Government & Organizations": "Government &amp; Organizations",
        "Organizations": "Organizations",
        "Health": "Health",
        "Kids & Family": "Kids &amp; Family",
        "Music": "Music",
        "News & Politics": "News &amp; Politics",
        "Religion & Spirituality": "Religion &amp; Spirituality",
        "Science & Medicine": "Science &amp; Medicine",
        "Society & Culture": "Society &amp; Culture",
        "Sports & Recreation": "Sports &amp; Recreation",
        "TV & Film": "TV &amp; Film",
        "Technology": "Technology"
    };
    genere_block = $("#input-Genre")[0];
    for (let i in genres) {
        genere_block.innerHTML += `<option>${i}</option>`;
    }
    languages = {
        "Russian": "ru",
        "English": "en"
    };
    language_block = $("#input-Language")[0];
    for (let i in languages) {
        language_block.innerHTML += `<option>${i}</option>`;
    }
    $("#input-img").on("change", function() {
        readURL(this);
    });
}

function submitForm() {
    input_ = ["input-img", "input-Title", "input-Author", "input-description"];
    input_v = [];
    true_v = [];
    for (let i = 0; i < input_.length; i++) {
        input_v[i] = document.getElementById(input_[i]).value;
        if (input_v[i] != "") {
            true_v[i] = true;
        } else {
            true_v[i] = false;
        }
    }
    console.log(true_v);

    if (true_v[0] && true_v[1] && true_v[2] && true_v[3]) {
        sendAddPodcast({
            title: $("#input-Title")[0].value,
            image: $("#input-img")[0].files[0],
            author: $("#input-Author")[0].value,
            description: $("#input-description")[0].value,
            language: languages[$("#input-Language")[0].value],
            category: genres[$("#input-Genre")[0].value],
            explicit: $("#explicit")[0].checked
        });
    } else {
        document.getElementById(
            "input-answ"
        ).innerHTML = `Not all fields are filled!`;
    }
}

function successfully_created() {
    content = $(".content")[0];
    console.log(content);
    content.innerHTML += `
        <div class="window_remove">
            <div class="window_remove_hidden"></div>
            <div class="window_remove_content">
                <div class="window_field">
                    <div class="window_title">
                        Podcast was created successfully!
                    </div>
                    <div class="btn_close">X</div>
                </div>
                <div class="window_field">
                    <div class="">
                        To index a podcast, first you must add an episode to the podcast:
                    </div>
                    <input class="btn_add_episods" type="button" name="add episode" value="Add episods!">
                </div>
                <div class="window_field">
                    <div class="">
                        This is your link to the RSS podcast:
                    </div>
                    <input class="rss_link" type="text" name="RSS link" value="LINK" readonly>
                </div>
                <div class="">
                    You can add your podcast to these services:
                </div>
                <div class="window_group_buttons">
                    <a class="btn-link" href="https://podcastsconnect.apple.com/my-podcasts" target="_blank">
                        <div class="apple-logo"></div>
                    </a>
                    <a class="btn-link" href="" target="_blank">
                        <div class="google-logo"></div>
                    </a>
                    <a class="btn-link" href="https://podcasters.spotify.com/submit" target="_blank">
                        <div class="spotify-logo"></div>
                    </a>
                </div>
                <div class="">
                    You can find these instructions on the podcast edit page.
                </div>
            </div>
        </div>
    `;
}

let CREATED_PODCAST = null;
function sendAddPodcast(item) {
    let formData = new FormData();
    for (let i in item) formData.append(i, item[i]);
    $.ajax({
        url: "/mypodcasts/api/podcasts/",
        type: "POST",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: response => {
            console.log(response);
            CREATED_PODCAST = response;
            successfully_created();
            whait_click_window();
        },
        error: response => {
            console.log(response);
        }
    });
}

function whait_click_window() {
    console.log(1);
    $('.rss_link').on('click', function(event) {
        event.preventDefault();
        let rss_link = $('.rss_link')[0];
        rss_link.select();
        document.execCommand("copy");
    });
    $('.btn_close').on('click', function(event) {
        event.preventDefault();
        getAndDraw();
        console.log(2);
    });
    $('.btn_add_episods').on('click', function(event) {
        event.preventDefault();
        location.href = `/mypodcasts/add-episodes/?podcast=${CREATED_PODCAST.id}`;
    });
}

$(getAndDraw);
