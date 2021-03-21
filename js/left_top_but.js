    $("<i id='iframe-refresh' style='z-index: 999;' onclick='location.reload();'></i>").appendTo($("body"));
    $('#iframe-refresh').fadeIn();	

    $('<i id="back-to-top" onclick="history.back()"></i>').appendTo($('body'));
    $('#back-to-top').fadeIn();	

    console.log('include')