$('#showNum').html('0%');
document.getElementById('pro-con').style.width = '0%';

let t1 = window.setInterval(refreshCount, 1000);
var num = 0;
var p_count = 1;

function refreshCount() {
    $.get('/console/log/', {'num': num}, function (data) {
            let pro = document.getElementById('pro-con');
            let showNum = document.getElementById('showNum');
            if (data['code'] === 2) {
                showNum.innerText = '100%';
                pro.style.width = '100%';
                window.clearInterval(t1);
                alert('Super Spider 运行结束');
                $('small span:first').remove();
                $('small').append('<span>运行完毕!</span>');
                return false
            } else {
                num = data['progress'];
                var logs = data['logs'];
                if (data['code'] === 1) {
                    p_count += logs.length;
                    for (var i = 0; i < logs.length; i++) {
                        var log = "<p>" + logs[i] + "</p>";
                        $('#spider_log').append(log);
                        console.log(p_count);
                        if (p_count > 16) {
                            var remove_p = p_count - 16;
                            p_count -= remove_p;
                            for (var c = 0; c < remove_p; c++) {
                                $('div#spider_log p:first').remove()
                            }
                        }
                    }
                }
                if (num > 100) {
                    num = 100;
                }
                if (num < 0) {
                    num = 0;
                }
                showNum.innerText = num + '%';
                pro.style.width = num + '%';
            }
        }
    )
}