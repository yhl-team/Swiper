

$(function () {
//        发送验证码
    $('#sendvcode').click(function () {

        $.ajax({
            type:'get',
            url: 'http://127.0.0.1:8000/api/user/submit/vcode/',
            data: {phone:$('.phone').val()}, //参数
            success:function (data) {
                console.log('success');
                console.log(data);

            },
            error:function (e) {
                console.log('error');
                console.log(e);

            }
        })

    })


})