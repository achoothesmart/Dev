document.addEventListener("DOMContentLoaded", function () {
    const videoPlayer = document.getElementById("video-player");
    const playlist = document.getElementById("playlist");

    const videoFiles = [
        "video1.mp4",
        "video2.mp4",
        "video3.mp4"
        // Add more video file names as needed
    ];

    videoFiles.forEach(function (videoFile) {
        const listItem = document.createElement("li");
        const link = document.createElement("a");
        link.href = `videos/${videoFile}`;
        link.textContent = videoFile;
        link.addEventListener("click", function (e) {
            e.preventDefault();
            videoPlayer.src = this.href;
            videoPlayer.play();
        });
        listItem.appendChild(link);
        playlist.appendChild(listItem);
    });
});
