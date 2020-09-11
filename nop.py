#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
import SMSBroadcastReceiver

class SMSBroadcastReceiver:

    otpReceiver.OTPReceiveListener = null

    def _init_OTPListener(receiver, OTPReceiveListener):
        this.otpReceiver = receiver

    def override_fun_onReceive(context, intent):
        if 'SmsRetriever.SMS_RETRIEVED_ACTION' in intent.action:
            val_extras = intent.extras
            val_status = extras.get(SmsRetriever.EXTRA_STATUS) as Status

            if status.statusCode:
                print('CommonStatusCodes.SUCCESS => {

                    // Get SMS message contents
                    var otp: String = extras.get(SmsRetriever.EXTRA_SMS_MESSAGE) as String

                    val pattern = Pattern.compile("(\\d{6})")
                    val matcher = pattern.matcher(otp)

                    // Extract one-time code from the message and complete verification
                    var value = ""
                    if (matcher.find()) {
                        System.out.println(matcher.group(1))
                        value = matcher.group(1)
                    }

                    println("message : $value")
                    otpReceiver?.onOTPReceived(value)
                }

                CommonStatusCodes.TIMEOUT ->
                    // Waiting for SMS timed out (5 minutes)
                    otpReceiver?.onOTPTimeOut()
            }
        }
    }

    interface OTPReceiveListener {

        fun onOTPReceived(otp: String)

        fun onOTPTimeOut()
    }

}
