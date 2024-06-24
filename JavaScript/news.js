document.addEventListener('DOMContentLoaded', function() {
    const newsContainer = document.getElementById('newsContainer');

    // Dummy-Daten für die News (kann durch echte Daten ersetzt werden)
    const newsItems = [
        {
            title: "Veröffentlichung von Deep Seek v2: Kostenlos und Open Source!",
            content: "Deep Seek v2 ist jetzt offiziell verfügbar und erleichtert die Suche nach Code und mathematischen Inhalten erheblich. Diese fortschrittliche Suchtechnologie ist kostenlos und Open Source, sodass jeder den Quellcode einsehen und zur Weiterentwicklung beitragen kann.",
            date: "Veröffentlicht am 24.06.2024 um 20:00 Uhr"
        },

    ];

    newsItems.forEach(news => {
        const article = document.createElement('article');
        article.innerHTML = `
            <h2>${news.title}</h2>
            <p>${news.content}</p>
            <p>${news.date}</p>
        `;
        newsContainer.appendChild(article);
    });
});
