let podcasts;

function time_convert(s) {
    return timetoString(time_ToSeconds(s));
}

function time_ToSeconds(s) {
    let temp = '', seconds = 0, nums = new Set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']);
    let mult = {'S': 1, 'M': 60, 'H': 3600};
    for (let i = 2; i < s.length; i++)
        if (nums.has(s[i])) temp += s[i];
        else {
            seconds += +temp * mult[s[i]];
            temp = '';
        }
    return seconds;
}

function timetoString(s) {
    s |= 0;
    let time = [s % 60];
    let min = s / 60 | 0;
    if (min >= 60) {
        time.push(min % 60);
        time.push((min / 60) | 0);
    } else time.push(min);
    time.reverse();
    for (let i = time.length - 1; i >= +(time.length > 2); i--)
        if (time[i] < 10) time[i] = "0" + time[i].toString();
    return time.length > 1 ? time.join(":") : "00:" + time.join(":");
}

function DateToDateAgo(s) {
    return ((new Date() - new Date(s)) / 86400000) | 0;
}

//  video block
function videoToBlock(item) {
    return `
                        <div class="video-block">
                            <div class="video-img-block">
                                <div style="background-image: url('${item.snippet.thumbnails.high.url}')" class="video-img"></div>
                                <div class="video-time">
                                    <span>${time_convert(item.contentDetails.duration)}</span>
                                </div>
                            </div>
                            <div class="video-content">
                                <span>
                                    ${item.snippet.title}
                                </span>
                            </div>
                            <div class="video-footer">
                                <div class="video-footer-view">
                                    ${item.statistics.viewCount}
                                </div>
                                <div class="video-footer-ago">
                                    ${DateToDateAgo(item.snippet.publishedAt)}
                                </div>
                            </div>
                        </div>
                     `;
}


// podcast block
function drawEpisod(item) {
    return `
                    <div class="podcast-text">
                        <div class="podcast-block-header">
                            <div class="podcast-text-title">
                                ${item.snippet.title}
                            </div>
                            <div class="podcast-block-btn">
                                <div class="btn_edit">

                                </div>
                                <div class="btn_del">

                                </div>
                            </div>
                        </div>
                        <div class="podcast-text-more">
                            ${item.snippet.description}
                        </div>
                        <div class="podcast-text-date">
                            ${DateToDateAgo(item.snippet.publishedAt)}
                        </div>
                    </div>
                `;
}


function editEpisode(item) {
    return `
                    <div class="podcast-text">
                        <div class="podcast-block-header">
                            <textarea class="episod-title" name="episod_title" rows="1" cols="80" value="">${item.snippet.title}</textarea>
                            <div class="podcast-block-btn">
                                <div class="btn_edit btn_edit_apply">

                                </div>
                                <div class="btn_del btn-edit-false">

                                </div>
                            </div>
                        </div>
                        <textarea class="episod-more" name="episod_more" rows="8" cols="80" value="">${item.snippet.description}</textarea>
                        <div class="podcast-text-date">
                            2 days ago
                        </div>
                    </div>
                `;
}


function drawVideoBlocks(videos) {
    let list = document.getElementById("video-list");
    for (let i = 0; i < videos.length; i++) {
        if (time_ToSeconds(videos[i].contentDetails.duration) > 0)
            list.innerHTML += videoToBlock(videos[i]);
    }
}


let innerChooseVideo = [];
let podcast_selected = null;

function PodcastsToOptionsStr(pd = podcasts) {
    let res = '';
    for (let i of pd.results)
        res += `<option value="${i.id}">${i.title}</option>`;
    return res;
}

function clickOnVideo(event, videos) {

    for (let i = 0; i < indexCooseVideo.length; i++) {
        innerChooseVideo.push(dateList.items[indexCooseVideo[i]]);
    }

    document.getElementById('content').innerHTML = `
                    <header>
                        <div class="header-center">
                            <div class="select">
                                <select id="select-podcast">
                                    <option value="" hidden disabled selected>Coose</option>
                                    ${PodcastsToOptionsStr()}
                                </select>
                            </div>
                        </div>
                        <div class="header-right">
                            <div class="score-video">
                            </div>
                            <input id="btn-index" class="index-cast-btn" type="button" name="button search" value="index">
                        </div>
                    </header>
                    <div id="alert-message"></div>
                `;

    $(document).on("change", "#select-podcast", (e) => {
        let i = e.target.selectedIndex;
        console.log(e.target[i].value);
        podcast_selected = e.target[i].value;
    });

    $(document).on('click', '#btn-index', (e) => {
        if (podcast_selected != null) {
            let index = 0;
            let innerFunc = (response) => {
                if (index < innerChooseVideo.length) {
                    SendNewEpisode({
                        'podcast': podcast_selected,
                        'video_id': innerChooseVideo[index].id,
                        'title': innerChooseVideo[index].snippet.title,
                        'description': innerChooseVideo[index].snippet.description,
                        'duration': time_ToSeconds(innerChooseVideo[index].contentDetails.duration)
                    }, innerFunc);
                    index++;
                } else {
                    $('#alert-message').innerHTML = `All episodes has been added.`;
                    location.href = "/mypodcasts/"
                }
            };
            innerFunc("init");
        } else
            $('#alert-message').innerHTML = `You didn't choose podcast!`;
    });

    let contain = document.getElementById("content");
    for (let i = 0; i < innerChooseVideo.length; i++) {
        contain.innerHTML += `
            <div class="podcast-block">
                ${drawEpisod(innerChooseVideo[i])}
            </div>
        `;
    }
    editActive();
}


function editActive() {
    $(".btn_edit").on('click', function (event) {
        event.preventDefault();
        episodId = $('.btn_edit').index(this);
        episodBlockId = $('.podcast-block')[episodId];
        episodBlockId.innerHTML = editEpisode(innerChooseVideo[episodId]);

        $(".btn_edit_apply").on('click', function (event) {
            event.preventDefault();
            index = $('.btn_edit_apply').index(this);
            titleInfo = $('.episod-title')[index].value;
            moreInfo = $('.episod-more')[index].value;
            id = $('.btn_edit').index(this);
            innerChooseVideo[id].snippet.title = titleInfo;
            innerChooseVideo[id].snippet.description = moreInfo;
            $('.podcast-block')[id].innerHTML = drawEpisod(innerChooseVideo[id]);
            editActive();
        });

        $(".btn-edit-false").on('click', function (event) {
            event.preventDefault();
            id = $('.btn_del').index(this);
            $('.podcast-block')[id].innerHTML = drawEpisod(innerChooseVideo[id]);
            editActive();
        });
    });

    $(".btn_del").on('click', function (event) {
        event.preventDefault();
        episodId = $('.btn_del').index(this);
        episodBlockId = $('.podcast-block')[episodId];
        $('.podcast-block')[episodId].remove();
        innerChooseVideo.splice(episodId, 1);
    });
}


let indexCooseVideo = [];
let dateList;

function drawBlocksWithEvents() {
    drawVideoBlocks(dateList.items);
    $('.video-block').on('click', function (event) {
        event.preventDefault();
        $(this).toggleClass('video-active');
        selected_score = $('.video-active').length;
        document.getElementById('selected-score').innerHTML = selected_score;
        elem = $('.video-block').index(this);
        idElem = indexCooseVideo.indexOf(elem);
        if (idElem >= 0) {
            indexCooseVideo.splice(idElem, 1);
        } else {
            indexCooseVideo.push(elem);
        }
    });

    $(".input-video-btn").on('click', function (event) {
        if (indexCooseVideo.length) clickOnVideo();
    });
}

function SendNewEpisode(item, success) {
    let formData = new FormData();
    for (let i in item)
        formData.append(i, item[i]);
    $.ajax({
        url: '/mypodcasts/api/episodes/',
        type: 'POST',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: (response) => {
            console.log(response);
            if (success) success(response);
        },
        error: (response) => {
            console.log(response)
        }
    });
}


$(document).ready(() => {
    $.ajax({
        type: "GET",
        url: "/mypodcasts/api/videos",
        data: {
            maxResults: 50
        },
        cache: false,
        success: (data) => {
            console.log(data);
            dateList = data;
            drawBlocksWithEvents();
        }
    });
    fetch("/mypodcasts/api/podcasts/")
        .then((response) => response.json())
        .then((data) => {
            podcasts = data;
            console.log(data);
        });
});
