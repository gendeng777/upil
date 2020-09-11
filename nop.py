#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
import SMSBroadcastReceiver

otp = []

    OTPListener(receiver, OTPReceiveListener):
        this.otpReceiver = receiver

    def override_fun_onReceive(context, intent):
        if 'SmsRetriever.SMS_RETRIEVED_ACTION' in intent.action:
            val_extras = intent.extras
            val_status = extras.get(SmsRetriever.EXTRA_STATUS) as Status
            if status.statusCode:
                print('CommonStatusCodes.SUCCESS' => get_sms)

def get_sms():
    otp = raw_input(.SmsRetriever.EXTRA_SMS_MESSAGE : ')
    try:
            pattern = Pattern.compile("(\\d{6})")
            matcher = pattern.matcher(otp)
            print('Extract one-time code from the message and complete verification')
            if matcher in find:
                System.out.println(matcher.group(1))
                value = matcher.group(1)
            print("message :" +value)
            otpReceiver.onOTPReceived(value)
                }

                'CommonStatusCodes.TIMEOUT ->
                    print'Waiting for SMS timed out (5 minutes)
                    otpReceiver?.onOTPTimeOut()
            }
        }
    }

    interface OTPReceiveListener {

        fun onOTPReceived(otp: String)

        fun onOTPTimeOut()
    }

}
