// Data array
const picArray = [
    {
        title: "Sunset",
        medium_image: "sunset.jpg",
        caption: "Beautiful sunset.",
        description: "A peaceful view of the sunset."
    },
    {
        title: "Mountains",
        medium_image: "mountains.jpg",
        caption: "Snowy mountains.",
        description: "The highest peaks covered in snow."
    }
];

// Select the section where articles will be added
const section = document.getElementById("articles");

// Loop through picArray to create articles
picArray.forEach(item => {
    // Create article element
    const article = document.createElement("article");
    article.className = "card";

    // Add inner content based on task structure
    article.innerHTML = `
        <h2>${item.title}</h2>
        <figure>
            <img src="${item.medium_image}" alt="${item.title}">
            <figcaption>${item.caption}</figcaption>
        </figure>
        <p>${item.description}</p>
    `;

    // Append article to section
    section.appendChild(article);
});
