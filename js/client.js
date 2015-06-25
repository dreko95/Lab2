var state = 'WORK';
var task = "", full_text = "";

function how_much_subs(sub, ful){
    var count;
    for(var count=-1,index=-2; index != -1; count++,index=ful.indexOf(sub,index+1) );

    return count;
}

function work() {
    while (state != 'STOP') {
        var requestGET = new XMLHttpRequest();
        requestGET.open("GET", "/ClientData", false);
        requestGET.send();

        var answer = JSON.parse(requestGET.responseText);

        task = answer['task'];
        full_text = answer['full_text'];
        state = answer['state'];

        if (state == 'WORK') {
            postMessage([task.length, full_text.length]);

            var result = how_much_subs(task, full_text);

            var requestPOST = new XMLHttpRequest();
            requestPOST.open("POST", "/ClientData", false);
            requestPOST.send("result=" + result);
        }
        else {
            break;
        }
    }
}

work();