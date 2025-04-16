document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("nav-toggle");
    const navLinks = document.getElementById("nav-links");
  
    // Toggle meny på klikk
    toggleBtn.addEventListener("click", () => {
      navLinks.classList.toggle("active");
    });
  
    // Fjern .active hvis skjermen blir bredere enn 768px
    window.addEventListener("resize", () => {
      if (window.innerWidth > 768 && navLinks.classList.contains("active")) {
        navLinks.classList.remove("active");
        console.log("Removed .active on resize >768px");
      }
    });
  });
  
  function openModal() {
    const modal = document.getElementById("pdfModal");
    modal.classList.add("show");
    document.body.classList.add("modal-open");
  }
  
  function closeModal() {
    const modal = document.getElementById("pdfModal");
    modal.classList.remove("show");
    document.body.classList.remove("modal-open");
  }
  
  
  window.onclick = function (event) {
    const modal = document.getElementById("pdfModal");
    if (event.target === modal) {
      closeModal();
    }
  };
  
  
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeModal();
    }
  });
  