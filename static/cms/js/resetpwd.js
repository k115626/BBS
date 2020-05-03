
$(function () {
    $('#submit').click(function (event) {

        // 阻止表单提交按钮的默认功能
        event.preventDefault();

        var oldpwdE = $('input[name=oldpwd]');
        var newpwd1E = $('input[name=newpwd1]');
        var newpwd2E = $('input[name=newpwd2]');        

        var oldpwd = oldpwdE.val();
        var newpwd1 = newpwd1E.val();
        var newpwd2 = newpwd2E.val();

        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd1': newpwd1,
                'newpwd2': newpwd2,
            },
            'success': function(data){
                if (data['code'] == 200){
                    zlalert.alertSuccessToast('密码修改成功');
                    oldpwdE.val('');
                    newpwd1E.val('');
                    newpwd2E.val('');
                }else{
                    var message = data['message'];
                    zlalert.alertInfo(message);
                }
            },
            'fail': function(error){
                zlalert.alertNetworkError();
            }
        })

    })
})