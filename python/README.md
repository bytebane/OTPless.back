# OTPless SDK integration in Python(FastAPI)

## Follow the steps below to get started

***Pre-requisites:* - [Python](https://www.python.org) installed**

1. Create an account on [OTPless](https://otpless.com/login)
2. Fill in the credentials(`CLIENT_ID` and `CLIENT_SECRET`)
   1. Visit Otpless [docs](https://otpless.com/platforms/sign-in) and copy the `Client Id` and `Client Secret`
   2. Paste the credentials [CLIENT_ID](main.py#L8), [CLIENT_SECRET](main.py#L9).
3. Replace the [REDIRECT_URI](main.py#L11) with a URL of your choice.
4. Create a virtual environment (Optional)

    > windows

    ```bash
    python -m venv .venv && .venv\Scripts\activate
    ```

    > linux

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

5. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

6. Check out `Known bugs and solutions` section and fix them in [`OTPlessAuthSDK.py`](.venv\Lib\site-packages\OTPLessAuthSDK.py)

7. Run

    ```bash
    uvicorn main:app --reload
    ```

### Try out the endpoints in the [Swagger UI](http://127.0.0.1:8000/docs)

## Known bugs and solutions

1. **Send Magic Link** via **SMS** - **OTPless** returns `Error: 'destinationUri'`

    ***Solution:***
    - in [OTPLessAuthSDK.py](.venv\Lib\site-packages\OTPLessAuthSDK.py) replace line `215` with the following

    ```py
    if 'destinationUri' in req_id is not None:
        user_detail.destination_uri = req_id['destinationUri']
    ```

2. **Send OTP** - **OTPless** returns `Error: send_otp() missing 1 required positional argument: 'templateId'`

    ***Solution:***
    - in [OTPLessAuthSDK.py](.venv\Lib\site-packages\OTPLessAuthSDK.py) replace line `35` with the following

    ```py
    return send_otp(phoneNumber,email,channel,hash, orderId,expiry,otpLength,client_id,client_secret,"")
    ```

    > Note: Just adding `hash` after `channel`, which is missing in the original code

### Check out [Official Documentation](https://otpless.com/platforms/python) for more details

## Thank you
