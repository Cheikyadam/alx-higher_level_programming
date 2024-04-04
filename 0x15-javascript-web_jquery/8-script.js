$.get({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    dataType: "json",
    success: function(data) {
        $.each(data.results, function(index, element) {
	    $('UL#list_movies').append('<li>'+element.title+'</li>');
        });
    },
    error: function(jqXHR, textStatus, errorThrown) {
        alert("Error:", textStatus, errorThrown);
    }
});
