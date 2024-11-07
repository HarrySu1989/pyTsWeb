// script src="/static/flow.js"></script>
function get_data(s_flow_type,s_flow_values, heading, button) {
  $.ajax({
    url: '/flow/update',  // 请求的URL
    type: 'POST',  // 请求类型
    contentType: 'application/json',  // 发送数据的内容类型
    data: JSON.stringify({
      s_flow_type: s_flow_type,
      s_flow_values:s_flow_values
    }),  // 发送的数据（这里为空对象，只是示例）
    success: function (response) {  // 请求成功时的回调函数
      var log = response.new_content
      if (log.toString().startsWith("测试结束")) {
        button.innerHTML = "开始"
      } else if (log === "当前流量仪正在测试") {
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

    // # if not url:url= f"""http://{self.values.flow_input_ip}/"""
$(document).ready(function () {
  $('#button-flow-begin').click(function () {
    var s_flow_log = document.getElementById('s_flow_log');
    var button = document.getElementById('button-flow-begin');
    var s_flow_values =`
      http://${document.getElementById('flow_input_ip').value},
      ${document.getElementById('flow_input_order').value},
      ${document.getElementById('flow_input_operator').value},
      ${document.getElementById('flow_input_sec').value}`

    if (button.innerHTML === "结束") {
      get_data("结束申请",s_flow_values, s_flow_log, button)
      button.innerHTML = "结束申请"
      return;
    } else if (button.innerHTML === "开始") {
      get_data(`开始申请`,s_flow_values, s_flow_log, button)
      button.innerHTML = "结束"
    } else if (button.innerHTML === "结束申请") {
      return;
    }
    var timer = setInterval(function () {
      get_data("",s_flow_values, s_flow_log, button)
      if (button.innerHTML === "开始") {
        clearInterval(timer);
      }
    }, 1000)

  });
});