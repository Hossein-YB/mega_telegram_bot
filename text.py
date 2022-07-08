class Messages:
    START_MSG = "سلام {} به ربات ما خوش امدید"
    PROFILE_MSG = "پروفایل شما: \n ایمیل: {} \n رمز: {}\n "
    DONT_HAVE_ACCOUNT_MSG = "کاربر عزیز شما اکانتی برای ربات تنظیم نکرده اید"
    GET_ACCOUNT_EMAIL_MSG = "برای اضافه کردن اکانت لطفا ایمیلی که با آن در مگا ثبت نام کرده اید رو ارسال کنید"
    IS_NOT_EMAIL_MSG = "لطفا اطلاعات خواسته شده رو با دقت ارسال کنید"
    TIME_OUT_SEND_EMAIL_MSG = "زمان شما برای ارسال ایمیل تمام شد لطفا دوباره از اول اقدام کنید"
    GET_ACCOUNT_PASSWORD_MSG = "لطفا رمز اکانتت رو ارسال کنید"
    SUCCESS_ADD = "کاربر عزیز اکانت شما با موفقیت به ربات اضافه شد"
    NOT_ADD = "اطلاعات وارد شده اشتباه است"

    # change password messages
    WANT_NEW_PASSWD_MSG = "لطفا رمز جدید اکانت را وارد کنید"
    PASSWORD_TRUE = "رمز شما ویرایش شد"
    PASSWORD_WRONG = "رمز وارد شده اشتباه هست"

    # change email messages
    WANT_NEW_EMAIL_MSG = "لطفا ایمیل جدید اکانت را وارد کنید"
    ENTER_NEW_EMAIL = "لطفا یک ایمیل جدید وارد کنید در حال حاضر این ایمیل در ربات وجود دارد"
    EMAIL_TRUE = "ایمیل شما ویرایش شد"
    EMAIL_WRONG = "ایمیل وارد شده اشتباه هست"

    # history messages
    HISTORY_MSG = "10 تا از آخرین فایل های آپلودی های شما \n"


class Buttons:

    start_my_profile = "پروفایل من"
    start_my_profile_call = "my_profile"

    start_add_account = "اضافه کردن اکانت"
    start_add_account_call = "add_account"

    profile_history = 'تاریخچه'
    profile_history_call = "history"

    profile_email = "تغییر ایمیل"
    profile_email_call = "change_email"

    profile_password = "تغییر رمز"
    profile_password_call = "password_change"
