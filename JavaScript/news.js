document.addEventListener('DOMContentLoaded', function() {
    const newsContainer = document.getElementById('newsContainer');

    // Dummy-Daten für die News (kann durch echte Daten ersetzt werden)
    const newsItems = [
        {
            title: "1.35 - 23/06/2024 - Neue Funktionen für die Website der KI-Fortschritte und Anwendungen",
            content: "In den letzten Entwicklungsphasen wurden mehrere wichtige Änderungen am Projekt vorgenommen. Zunächst wurden verschiedene Fehler behoben, die während der Tests identifiziert wurden. Diese Fehlerbehebungen waren entscheidend, um die Stabilität und Zuverlässigkeit der Anwendung sicherzustellen. Darüber hinaus wurde eine neue Funktion implementiert, die es Benutzern ermöglicht, Bilder zu vergrößern, indem sie mit der Maus darüber schweben. Diese Funktion verbessert die Benutzerfreundlichkeit erheblich und bietet eine interaktivere Erfahrung beim Betrachten von Bildmaterial. Ein weiterer signifikanter Schritt war die Überarbeitung der Navigationmenüs. Diese wurden in ein Dropdown-Menü umgewandelt, was die Navigation durch die Anwendung vereinfacht und Platz auf der Benutzeroberfläche spart. Diese Änderung trägt dazu bei, dass die Benutzer intuitiv durch die verschiedenen Abschnitte der Anwendung navigieren können. Diese jüngsten Verbesserungen stellen sicher, dass das Projekt nicht nur funktionaler, sondern auch benutzerfreundlicher wird, indem sie häufige Probleme lösen und die Navigation erleichtern.",
            date: "23. Juni 2024"
        },
        {
            title: "1.0 - Webseite veröffentlicht",
            content: "Neue Webseite unter https://ki.bbd-8.org/ verfügbar",
            data: "19/06/2024",
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