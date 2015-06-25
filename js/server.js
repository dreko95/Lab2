function update(){
    setInterval(function()
    {
        updateServer();
    }, 500);
}


function updateServer(){
    $.get('/ServerData', function(entry)
    {
        $('#stat-percent').html(entry['percent']);
        $('#stat-clients').html(entry['clients']);
        $('#stat-time').html(entry['time']);
        $('#stat-result').html(entry['result']);
    });
}