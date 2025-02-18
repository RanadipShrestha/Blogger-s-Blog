// script.js
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Check for saved theme in localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.classList.add(savedTheme);
        themeToggle.textContent = savedTheme === 'dark-mode' ? '☀️' : '🌙';
    }

    // Toggle theme on button click
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        const isDarkMode = body.classList.contains('dark-mode');
        themeToggle.textContent = isDarkMode ? '☀️' : '🌙';
        localStorage.setItem('theme', isDarkMode ? 'dark-mode' : '');
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const blogPosts = document.querySelectorAll('.blog-post');

    searchInput.addEventListener('input', () => {
        const searchText = searchInput.value.toLowerCase();

        blogPosts.forEach(post => {
            const title = post.querySelector('.content').textContent.toLowerCase();
            if (title.includes(searchText)) {
                post.style.display = 'block';
            } else {
                post.style.display = 'none';
            }
        });
    });
});




//For FAQ
document.addEventListener("DOMContentLoaded", function () {
    const accordionItems = document.querySelectorAll(".accordion-item");

    // Hide all accordion content by default
    accordionItems.forEach((item) => {
        item.classList.remove("active"); // Ensure no item starts as active
        const content = item.querySelector(".accordion-content");
        content.style.display = "none"; // Hide content
    });

    accordionItems.forEach((item) => {
        const header = item.querySelector(".accordion-header");

        header.addEventListener("click", function () {
            const content = item.querySelector(".accordion-content");

            // Close all other accordions
            accordionItems.forEach((i) => {
                if (i !== item) {
                    i.classList.remove("active");
                    i.querySelector(".accordion-content").style.display = "none";
                }
            });

            // Toggle the clicked accordion
            if (content.style.display === "none") {
                content.style.display = "block"; // Show content
                item.classList.add("active");
            } else {
                content.style.display = "none"; // Hide content
                item.classList.remove("active");
            }
        });
    });
});





document.addEventListener('DOMContentLoaded', function () {
    const userButton = document.getElementById('user-button');
    const dropdownMenu = document.getElementById('dropdown-menu');

    // Toggle the dropdown menu when the user button is clicked
    userButton.addEventListener('click', function (e) {
        e.stopPropagation(); // Prevent click event from bubbling up
        dropdownMenu.classList.toggle('hidden');
    });

    // Close the dropdown if the user clicks outside the menu
    document.addEventListener('click', function () {
        dropdownMenu.classList.add('hidden');
    });
});