var  conn = null;

function connect() {
    disconnect();

    var transports = ["websocket"];
    conn = new SockJS("http://" + window.location.host + "/real/time", transports);
    log("warning", "connecting....");

    conn.onopen = function () {
        console.log("connect success!");
        log("success", "connect success!");
    };
    conn.onmessage = function (e) {
        //console.log(e.data)
        update_ui(e);
    };

    conn.onclose = function () {
        console.log("connect close！")
        log("danger", "连接断开！");
    };

    setInterval(function () {
        conn.send("system");
    },1000);
    
}

function disconnect() {
    if (conn != null) {
        log("danger", "connection close！");
        conn.close();
        conn = null;
    }
}


if (conn == null) {
    connect();
} else {
    disconnect();
}