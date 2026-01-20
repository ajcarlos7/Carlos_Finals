// open popup
document.querySelector("#signup-btn").addEventListener("click", () => {
    document.querySelector("#popup").classList.add("active");
});

// close popup
document.querySelector(".close-btn").addEventListener("click", () => {
    document.querySelector("#popup").classList.remove("active");
});

// switch to signup form
document.querySelector("#show-signup").addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector("#login-form").style.display = "none";
    document.querySelector("#signup-form").style.display = "block";
});

// switch to login form
document.querySelector("#show-login").addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector("#signup-form").style.display = "none";
    document.querySelector("#login-form").style.display = "block";
});
