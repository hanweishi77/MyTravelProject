
$(function(){
    //获取按钮元素
    const btn = document.querySelector("#btn-captcha")
    //新增节点
    const div = document.createElement('div')
     div.style.color = "red"
    // 查找父节点，追加节点在最后
    const search_div = document.querySelector("#login  div.email ")
    search_div.append(div)
    //jquery按钮绑定点击事件，处理函数
    $(btn).click(function(event){
        // 阻止默认事件,如表单提交
        event.preventDefault()
        //获取输入的邮箱
        let email = $("input[name='email']").val()

        //使用ajax 发送验证码
        $.ajax({
            url: "/mail/captcha?email=" + email,
            method: "GET",
            dataType:"json",
            success: function(res){
                console.log(res.ok)
                if(res.ok === 1){
                    //写入信息
                    div.innerHTML = ""
                    //倒计时长:60s
                    let i = 60
                    //按钮禁用
                    btn.disabled = true
                    //倒计时
                    let timer=setInterval(function (){
                        $(btn).text(`重新获取${i}s`)
                        i--
                        if(i<=0){
                            clearInterval(timer)
                            $(btn).text("获取验证码")
                            btn.disabled = false
                        }
                    },1000)
                }
                else{
                    //写入信息
                    div.innerHTML = "邮箱已被注册"
                }
            },
            fail:function(error){
               console.log(error)
            },
        })
    })

});