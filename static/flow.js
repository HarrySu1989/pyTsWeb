// script src="/static/flow.js"></script>
$(document).ready(function () {
  $('#button-flow-begin').click(function () {
    var count1 = 0
    var heading = document.getElementById('div-flow-status');
    heading.innerHTML ="准备开始"  // 更新页面内容
    var timer = setInterval(function () {
      $.ajax({
        url: '/flow/update',  // 请求的URL
        type: 'POST',  // 请求类型
        contentType: 'application/json',  // 发送数据的内容类型
        data: JSON.stringify({count: count1}),  // 发送的数据（这里为空对象，只是示例）
        success: function (response) {  // 请求成功时的回调函数
          var log = response.new_content
          if (log == "完成") {
            clearInterval(timer);
          }
          heading.innerHTML=log;  // 更新页面内容
        },
        error: function (xhr, status, error) {  // 请求失败时的回调函数
          console.error('Ajax请求失败:', status, error);
          heading.innerHTML="Ajax请求失败"
          clearInterval(timer);
        }
      });
      count1 += 1
    }, 1000)

  });
});