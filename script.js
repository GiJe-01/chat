// script.js
document.addEventListener("DOMContentLoaded", function() {
    const passwordModal = document.getElementById("passwordModal");
    const postsContainer = document.getElementById("posts");

    function openPasswordModal() {
        passwordModal.classList.add("show");
    }

    function checkPassword() {
        const passwordInput = document.getElementById("passwordInput").value;
        if (passwordInput === "yourPassword") {
            passwordModal.classList.remove("show");
        } else {
            alert("パスワードが正しくありません。");
        }
    }

    function submitPost() {
        const postContent = document.getElementById("postContent").value;
        if (postContent.trim() === "") {
            alert("投稿内容を入力してください。");
            return;
        }

        const postElement = document.createElement("div");
        postElement.classList.add("post");
        postElement.textContent = postContent;
        postsContainer.prepend(postElement);
        document.getElementById("postContent").value = "";
    }

    function init() {
        openPasswordModal();
    }

    init();
    window.submitPost = submitPost;
    window.checkPassword = checkPassword;
});
