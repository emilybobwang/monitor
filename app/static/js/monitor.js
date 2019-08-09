var  conn = null;

//progress bars
function progress_status(val) {
    var data = "";
    if (val >= 0 && val < 25) {
        data = " bg-success";
    } else if (val >= 25 && val < 50) {
        data = "";
    } else if (val >= 50 && val < 75) {
        data = " bg-warning";
    } else if (val >= 75 && val <= 100) {
        data = " bg-success";
    }
    return data
}

function log(cls, msg) {
    document.getElementById("monitor_status").innerHTML = "<div class='alert alert-" + cls + "'>" + msg + "</div>";
}

function update_ui(e) {
    var data = e.data;
    data = JSON.parse(data);
    /*avg CPU*/
    option_cpu_avg.series[0].data[0] = (data['cpu']['percent_avg'] / 100).toFixed(4);
    option_cpu_avg.title[0].text = data['dt'] + "-CPU usage";
    myChart_cpu_avg.setOption(option_cpu_avg);
    /* per cpu */
    var cpu_per = "";
    for (var k in data['cpu']['percent_per']) {
        var num = parseInt(k);
        cpu_per += "<tr><td class='text-primary' style='width: 30%'>CPU" + num + "</td>";
        cpu_per += "<td><div class='progress'><div class='progress-bar progress-bar-striped progress-bar-animated" + progress_status(data['cpu']['percent_per'][k]) + "' role='progressbar' aria-valuenow='" + data['cpu']['percent_per'][k] + "' aria-valuemin='0' aria-valuemax='100' style='width: " + data['cpu']['percent_per'][k] + "%'>" + data['cpu']['percent_per'][k] + "%</div></div></td></tr>";
    }
    document.getElementById("tb_cpu_per").innerHTML = cpu_per;

}

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
        log("danger", "connection close！");
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