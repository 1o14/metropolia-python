// Kuvadata
const picArray = [
    {
        title: "Sunset",
        medium_image: "file:///C:/Users/biank/Downloads/sunset.jpg", // Local path for sunset medium image
        large_image: "file:///C:/Users/biank/Downloads/sunset.jpg",  // Local path for sunset large image
        caption: "Beautiful sunset.",
        description: "A peaceful view of the sunset."
    },
    {
        title: "Mountains",
        medium_image: "file:///C:/Users/biank/Downloads/mountain.jpg", // Local path for mountain medium image
        large_image: "file:///C:/Users/biank/Downloads/mountain.jpg", // Local path for mountain large image
        caption: "Snowy mountains.",
        description: "The highest peaks covered in snow."
    }
];

const section = document.getElementById("articles");
const dialog = document.getElementById("imageModal");
const modalImage = document.getElementById("modalImage");
const closeModal = document.getElementById("closeModal");

//Luo artikkelit
picArray.forEach((item) => {
    const article = document.createElement("article");
    article.className = "card";

    article.innerHTML = `
        <h2>${item.title}</h2>
        <figure>
            <img src="${item.medium_image}" alt="${item.title}">
            <figcaption>${item.caption}</figcaption>
        </figure>
        <p>${item.description}</p>
    `;

    article.addEventListener("click", () => {
        modalImage.src = item.large_image;
        modalImage.alt = item.title;
        dialog.showModal();
    });

    section.appendChild(article);
});

// Sulkee modalin
closeModal.addEventListener("click", () => {
    dialog.close();
});
