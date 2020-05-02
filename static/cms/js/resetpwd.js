
$(function () {
    $('#submit').click(function (event) {

        // 阻止表单提交按钮的默认功能
        event.preventDefault();

        var oldpwd = $('input[name=oldpwd]').val();
        var newpwd1 = $('input[name=newpwd1]').val();
        var newpwd2 = $('input[name=newpwd2]').val();

        zlajax.post({
            'url': '/cms/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd1': newpwd1,
                'newpwd2': newpwd2,
            },
            'success': function(data){
                console.log(data);
            },
            'fail': function(error){
                console.log(error);
            }
        })

    })
})