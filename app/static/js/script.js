const button = document.getElementById("team-dropdown-button");
const dropdown = document.getElementById("team-dropdown");
const overlay = document.getElementById("overlay");

if (button && dropdown) {
    button.addEventListener("click", (e) => {
        e.stopPropagation();
        dropdown.classList.toggle("hidden");
        overlay.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
        if (!dropdown.contains(e.target) && !button.contains(e.target)) {
            dropdown.classList.add("hidden");
            overlay.classList.add("hidden");
        }
    });
}
