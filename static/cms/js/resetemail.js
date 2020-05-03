
$(function(){
    $('#get_vcode').click(function(event){
        var v_code = $("input[name=newemail]").val();
        if(! v_code){
            zlalert.alertInfoToast('请输入邮箱');
            return;
        };
        zlajax.get({
            'url': '/cms/email_captcha/',
            'data': {
                'email': v_code
            },
            'success': function(data){
                if (data['code'] == 200){
                    zlalert.alertSuccessToast('邮件发送成功, 请注意查收!')
                }else{
                    zlalert.alertInfo(data['message'])
                }
            },
            'fail': function(error){
                zlalert.alertNetworkError();
            }
        })

    });

});


$(function(){
    $('#submit').click(function(event){
        event.preventDefault();

        var emailE = $("input[name='newemail']");
        var captchE = $("input[name='captcha']");

        var email = emailE.val();
        var captcha = captchE.val();

        zlajax.post({
            'url': '/cms/resetemail/',
            'data': {
                'email': email,
                'captcha': captcha
            },
            'success': function(data){
                if (data['code'] == 200){
                    zlalert.alertSuccessToast('邮箱修改成功');
                    emailE.val('');
                    captchE.val('');
                }else{
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail': function(error){
                zlalert.alertNetworkError();
            }
        })
        
    })
})