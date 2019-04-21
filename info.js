function show (data) {
    for (var i = 0; i < data.length; ++i) {
        $("#product").append(`
            <b>${data[i]['title']}</b><i> ${data[i]['price']}</i><br>
            <small>${data[i]['release_date']} F: ${data[i]['favouriteCount']}</small><br>`)
    } 
}

$(document).ready ( () =>
    $.ajax({  
        type: "Get",  
        url:"http://solelinks.com/api/releases?page=1&upcoming=true.json",
        error: function(request) {
            alert("Connection error");
        },
        success: function(res) {
            show(res['data']['data']);
            console.log(res['data']['data'])
        }
    })
);
