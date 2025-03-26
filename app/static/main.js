// Toggle mobile navbar
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("nav-toggle");
    const navLinks = document.getElementById("nav-links");
  
    if (toggleBtn && navLinks) {
      toggleBtn.addEventListener("click", () => {
        navLinks.classList.toggle("active");
      });
    }
  });
  