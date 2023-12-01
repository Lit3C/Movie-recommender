function storeImageURL(url) {
    // Effectuez une requête AJAX pour envoyer l'URL au serveur
    $.ajax({
        url: "{% url 'store_image_url' %}",  // Assurez-vous de définir une URL pour gérer le stockage côté serveur
        type: "POST",
        data: {'url': url},
        dataType: "json",
        success: function(data) {
            console.log(data.message);
        },
        error: function(error) {
            console.error("Erreur lors du stockage de l'URL : ", error);
        }
    });
}