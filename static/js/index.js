$( document ).ready(function(){


    // $("a.doc-symbol").hover(function(){
    //     // Hover over code
    //     var doc_symbol = $(this).attr('id');
    //     console.log(doc_symbol);

    //     // var title = getTitle(doc_symbol);
    //     var url = "http://127.0.0.1:5000/metadata?tag=title&doc_symbol=" + doc_symbol;
    //     $.get({
    //         url: url,
    //         error: function(msg) {
    //             console.log(msg);
    //         },
    //         success: function(data) {
    //             var html = $.parseHTML(data);
    //             var json = $(html).find("pre").text();
    //             var obj = jQuery.parseJSON(json);
    //             var title = obj.title;

    //             var str = "Document Symbol: " + doc_symbol + " \nTitle: " + title;
    //             $("div.contents").html("<p>" + str + "</p>");
    //         }
    //     });
    // });    
});
