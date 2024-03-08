from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Union

from OTPLessAuthSDK import OTP
from OTPLessAuthSDK import UserDetail

CLIENT_ID = "PASTE_YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "PASTE_YOUR_CLIENT_SECRET_HERE"
# replace with your Redirect URI (used in magic link)
REDIRECT_URI = "https://your.domain"

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="OTPless demo",
        version="1.0.0",
        summary="A demo integration of OTPless authentication service",
        description="This is a demo integration of OTPless authentication service, for Python(FastAPI). To learn more, visit <a target='_blank' href='https://otpless.com/platforms/python'>Official documentation</a>",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://d1j61bbz9a40n6.cloudfront.net/website/home/v4/logo/black_logo.svg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
def read_root():
    return {
        "Authentication": "OTPless",
        "Endpoints": {
            "Send Magic Link": "/send-mlink/{channel}",
            "Verify Magic Link": "/verify-mlink",
            "Get User Details": "/get-user-details",
            "Send OTP": "/send-otp/{channel}",
            "Verify OTP": "/verify-otp",
            "Resend OTP": "/resend-otp",
        },
        "Channel-Options": ["EMAIL", "SMS", "WHATSAPP", "SMS,WHATSAPP"],
    }


# Send Magic Link
# POST /send-mlink
# Request body: channel: string, mobile_number: string, email: string
@app.post("/send-mlink")
def send_mlink(
    channel: str, mobile_number: Union[str, None] = None, email: Union[str, None] = None
):
    try:
        response = UserDetail.generate_magic_link(
            mobile_number, email, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, channel
        )
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return {"message": "Magic link sent", "response": response}


# Verify Magic Link
# POST /verify-mlink
# Request body: code: string
@app.post("/verify-mlink")
def verify_mlink(code: str):
    try:
        response = UserDetail.verify_code(code, "ef0kpz5g", "ijx4ksmvtozx314n")
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return response


# Send OTP
# POST /send-otp
# Request body: channel: string, mobile_number string, email: string, order_id: str(optional), hash: str(optional), expiry: int(optional), otp_length: int(optional)
@app.post("/send-otp")
def send_otp(
    channel: str,
    mobile_number: Union[str, None] = None,
    email: Union[str, None] = None,
    order_id: Union[str, None] = None,
    hash: Union[str, None] = None,
    expiry: Union[str, None] = None,
    otp_length: Union[str, None] = None,
):
    if email is None and mobile_number is None:
        return {"message": "Either Email or Mobile number must be provided"}
    if expiry is None:
        expiry = 300
    if otp_length is None:
        otp_length = 6
    try:
        response = OTP.send_otp(
            mobile_number,
            email,
            channel,
            order_id,
            hash,
            expiry,
            otp_length,
            CLIENT_ID,
            CLIENT_SECRET,
        )
        # def send_otp(phoneNumber, email, channel,hash, orderId, expiry, otpLength,client_id,client_secret)
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return response


# Resend OTP
# POST /resend-otp
# Request body: order_id: str
@app.post("/resend-otp")
def resend_otp(order_id: str):
    try:
        response = OTP.resend_otp(order_id, CLIENT_ID, CLIENT_SECRET)
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return response


# Verify OTP
# POST /verify-otp
# Request body: order_id: str, otp: str, email: str, phone_number: str
@app.post("/verify-otp")
def verify_otp(
    order_id: str,
    otp: str,
    email: Union[str, None] = None,
    phone_number: Union[str, None] = None,
):
    if email is None and phone_number is None:
        return {"message": "Either Email or Phone number is required"}
    try:
        response = OTP.veriy_otp(
            order_id, otp, email, phone_number, CLIENT_ID, CLIENT_SECRET
        )
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return response


# Verify SDK token
# POST /verify-sdk-token
# Request body: token: string
@app.post("/verify-sdk-token")
def verify_sdk_token(token: str):
    try:
        response = UserDetail.verify_token(token, CLIENT_ID, CLIENT_SECRET)
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return response


# Get User Details
# POST /get-user-details
# Request body: token: string
@app.post("/get-user-details")
def get_user_details(token: str):
    try:
        response = UserDetail.decode_id_token(token, CLIENT_ID, CLIENT_SECRET)
    except Exception as error:
        return {"message": f"Something went wrong, please try again. Error: {error}"}
    return response
