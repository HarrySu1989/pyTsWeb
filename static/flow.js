// script src="/static/flow.js"></script>
function get_data(count1, heading, button) {
  $.ajax({
    url: '/flow/update',  // 请求的URL
    type: 'POST',  // 请求类型
    contentType: 'application/json',  // 发送数据的内容类型
    data: JSON.stringify({count: count1}),  // 发送的数据（这里为空对象，只是示例）
    success: function (response) {  // 请求成功时的回调函数
      var log = response.new_content
      if (log.toString().startsWith("测试结束")) {
        button.innerHTML = "开始"
      }else if (log === "当前流量仪正在测试") {
        button.innerHTML = "结束"
        alert(log)
      }
      heading.innerHTML = log;  // 更新页面内容
    },
    error: function (xhr, status, error) {  // 请求失败时的回调函数
      console.error('Ajax请求失败:', status, error);
      heading.innerHTML = "Ajax请求失败"
      button.innerHTML = "开始"
    }
  });
}

$(document).ready(function () {
  $('#button-flow-begin').click(function () {
    var count1 = 0
    var heading = document.getElementById('div-flow-status');
    var button = document.getElementById('button-flow-begin');


    if (button.innerHTML === "结束") {
      get_data(-1, heading, button)
      button.innerHTML = "结束申请"
      return;
    } else if (button.innerHTML === "开始") {
      button.innerHTML = "结束"
    } else if (button.innerHTML === "结束申请") {
      return;
    }
    var timer = setInterval(function () {
      get_data(count1, heading, button)
      if (button.innerHTML === "开始") {
        clearInterval(timer);
      }
      count1 += 1
    }, 1000)

  });
});