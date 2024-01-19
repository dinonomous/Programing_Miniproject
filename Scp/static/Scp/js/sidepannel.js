function changeVideo(event) {
    event.preventDefault();
    var videoUrl = event.target.getAttribute('data-video-url');
    if (videoUrl) {
        document.getElementById('videoIframe').src = videoUrl;
    }
}