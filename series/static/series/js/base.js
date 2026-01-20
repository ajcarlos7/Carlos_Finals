document.getElementById("signup-btn")?.addEventListener("click", () => {
    document.getElementById("popup").classList.add("active");
});

document.querySelector(".close-btn")?.addEventListener("click", () => {
    document.getElementById("popup").classList.remove("active");
});

document.getElementById("show-signup")?.addEventListener("click", () => {
    loginForm.style.display = "none";
    signupForm.style.display = "block";
});

document.getElementById("show-login")?.addEventListener("click", () => {
    signupForm.style.display = "none";
    loginForm.style.display = "block";
});
