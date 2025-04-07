document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("nav-toggle");
    const navLinks = document.getElementById("nav-links");

    if (toggleBtn && navLinks) {
        // Toggle the "active" class on the nav-links when the toggle button is clicked
        toggleBtn.addEventListener("click", () => {
            navLinks.classList.toggle("active");
        });

        // Close the menu when a link is clicked
        navLinks.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                navLinks.classList.remove("active");
            });
        });
    }
});
