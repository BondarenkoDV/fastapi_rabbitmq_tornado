jQuery.validator.addMethod("checkMask", function (value, element) {
    return /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/g.test(value);
});
$("#formValidation").validate({
    rules: {
        last_name: {
            required: true,
            minlength: 2,
            maxlength: 25
        },
        first_name: {
            required: true,
            minlength: 3,
            maxlength: 25
        },
        patronymic: {
            required: true,
            minlength: 2,
            maxlength: 25
        },
        phone: {
            checkMask: true,
        },
        message: {
            required: false,
            maxlength: 500,
        }
    },
    messages: {
        last_name: {
            required: "Введите фамилию",
            minlength: jQuery.validator.format("Меньше {0} символов"),
            maxlength: jQuery.validator.format("Больше {0} символов")
        },
        first_name: {
            required: "Введите имя",
            minlength: jQuery.validator.format("Меньше {0} символов"),
            maxlength: jQuery.validator.format("Больше {0} символов")
        },
        patronymic: {
            required: "Введите отчество",
            minlength: jQuery.validator.format("Меньше {0} символов"),
            maxlength: jQuery.validator.format("Больше {0} символов")
        },
        phone: {
            checkMask: "Введите номер телефона"
        },
        message: {
            maxlength: jQuery.validator.format("Обращение не может быть больше {0} символов")
        }
    },
    submitHandler: function (form) {
        form.submit();
    }
});

$('.js-phone').mask("+7(999) 999-99-99", { autoclear: false })
