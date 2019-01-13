$(function () {

    // login
    var error_name = false;
    var error_password = false;
    var error_ver_code = false;

    $('#username').blur(function () {
        check_username();
    });

    $('#password').blur(function () {
        check_password();
    });

    $('#ver_code').blur(function () {
        check_ver_code();
    });

    function check_username() {
        var len = $('#username').val().length;
        if (len < 5 || len > 20) {
            $('#username').next().html('请输入5-20个字符的用户名').show();
            error_name = true;
        } else {
            $('#username').next().hide();
            error_name = false;
        }
    }

    function check_ver_code() {
        var len = $('#ver_code').val().length;
        if (len !== 4) {
            $('#ver_err').html('验证码错误').show();
            error_name = true;
        } else {
            $('#var_code').next().hide();
            error_name = false;
        }
    }

    function check_password() {
        var len = $('#password').val().length;
        if (len < 8 || len > 20) {
            $('#password').next().html('密码最少8位，最长20位').show();
            error_password = true;
        } else {
            $('#password').next().hide();
            error_password = false;
        }
    }

    $('#login_form').submit(function () {
        check_username();
        check_password();
        check_ver_code();

        return error_name === false && error_password === false && error_ver_code === false;
    });

    // register
    var error_r_name = false;
    var error_r_email = false;
    var error_r_password = false;
    var error_r_confirm_pwd = false;
    var error_r_phone = false;

    $('#r_username').blur(function () {
        check_r_username();
    });

    $('#r_email').blur(function () {
        check_r_email();
    });

    $('#r_password').blur(function () {
        check_r_password();
    });

    $('#r_confirm_pwd').blur(function () {
        check_r_confirm_pwd();
    });

    $('#r_phone').blur(function () {
        check_r_phone();
    });

    function check_r_username() {
        var len = $('#r_username').val().length;
        if (len < 5 || len > 20) {
            $('#register_error').html('请输入5-20个字符的用户名').show();
            error_r_name = true;
        } else {
            $('#r_username').next().hide();
            error_r_name = false;
        }
    }

    function check_r_email() {
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;


        if (re.test($('#r_email').val())) {
            $('#r_email').next().hide();
            error_r_name = false;
        } else {
            $('#register_error').html('你输入的邮箱格式不正确').show();
            error_r_name = true;
        }
    }

    function check_r_password() {
        var len = $('#r_password').val().length;
        if (len < 8 || len > 20) {
            $('#register_error').html('密码最少8位，最长20位').show();
            error_r_password = true;
        } else {
            $('#r_password').next().hide();
            error_r_password = false;
        }
    }

    function check_r_confirm_pwd() {
        var pwd1 = $('#r_password').val();
        var pwd2 = $('#r_confirm_pwd').val();
        if (pwd1 !== pwd2) {
            $('#register_error').html('两次输入的密码不一致').show();
            error_r_name = true;
        } else {
            $('#r_confirm_pwd').next().hide();
            error_r_name = false;
        }
    }

    function check_r_phone() {
        var phone = $('#r_phone').val();
        if (!(/^1[345789]\d{9}$/.test(phone))) {
            $('#register_error').html('手机号输入有误').show();
            error_r_phone = true;
        } else {
            $('#r_phone').next().hide();
            error_r_phone = false;
        }
    }


    $('#register_form').submit(function () {
        check_r_username();
        check_r_email();
        check_r_password();
        check_r_confirm_pwd();
        check_r_phone();

        return error_r_name === false && error_r_email === false && error_r_password === false && error_r_confirm_pwd === false && error_r_phone === false;
    });

    $('#ver_img').click(function () {
        console.log(1);
        $.get('/user/ver/', {}, function (data) {
            var path = '/static/image/vc.png?temp=' + Math.random();
            $('#ver_img').attr('src', path).show();
            console.log(data);
            return false
        });
    });
});