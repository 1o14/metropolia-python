async function fetchTVShows() {

    const response = await fetch('https://api.tvmaze.com/search/shows?q=star');
    const data = await response.json();

    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    data.forEach(tvShow => {
        const article = document.createElement('article');

        const name = document.createElement('h2');
        name.textContent = tvShow.show.name;
        article.appendChild(name);

        const link = document.createElement('a');
        link.href = tvShow.show.url;
        link.target = '_blank';
        link.textContent = 'More Details';
        article.appendChild(link);

        const img = document.createElement('img');
        img.src = tvShow.show.image?.medium || 'default-image.jpg'; // Fallback if no image
        img.alt = tvShow.show.name;
        article.appendChild(img);

        const summary = document.createElement('div');
        summary.innerHTML = tvShow.show.summary;
        article.appendChild(summary);

        resultsDiv.appendChild(article);
    });
}

fetchTVShows();
