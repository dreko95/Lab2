function client_create(){
    var worker = new Worker("js/client.js");
    worker.onmessage = function(event){
        $('#stat-sub-len').html(event.data[0]);
        $('#stat-full-len').html(event.data[1]);
    };
}