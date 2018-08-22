function showCommentForm() {
    if (document.getElementById("comment-form").style.display === "block") {
        document.getElementById("comment-form").style.display = "none";
        document.getElementById("toggle-icon").classList.toggle("fa-caret-down");
        document.getElementById("toggle-icon").classList.toggle("fa-caret-right");
    } else {
        document.getElementById("comment-form").style.display = "block";
        document.getElementById("toggle-icon").classList.toggle("fa-caret-down");
        document.getElementById("toggle-icon").classList.toggle("fa-caret-right");
    }
}
function animateDiv() {
    var animatediv = document.getElementById("wheel")
    if (animatediv.classList.contains('animate-notifications')) {
        animatediv.classList.remove('show-notifications')
        animatediv.classList.remove('animate-notifications')
        animatediv.classList.add('animate-reverse');
    }
    else if (animatediv.classList.contains('animate-reverse')) {
        animatediv.classList.remove('animate-reverse')
        animatediv.classList.add('animate-notifications')
        animatediv.classList.add('show-notifications');
    }
    else {
        animatediv.classList.add('animate-notifications')
        animatediv.classList.add('show-notifications');
    }
};
