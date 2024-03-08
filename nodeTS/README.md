# OTPless SDK integration in Node TS

This is a demo for [OTPless](https://otpless.com) Backend SDK integration in Node TypeScript.

>> To integrate the same using JavaScript, check out [nodeJS](/nodeJS/) directory.

## Follow the steps below to get started

***Pre-requisites:* - [Node](https://nodejs.org) installed**

### Step 1: Run the server

1. Open a new terminal in [nodeTS](/nodeTS/) directory.
2. Open [src>constants](./src/constants/index.ts) file and
   - Set the constants with your credentials.
3. Install and run

    ```bash
    npm i && npm run dev
    ```

### Step 2: Send requests to the server

- **Thats it**. Open [src>auth](./src/auth/index.ts) file and use the functions from [auth](./src/auth/index.ts#L5) class.
- Uncomment the function you want to test in [index.ts](./src/index.ts) file.
- Pass the values for the required parameters if any and hit `save` to send requests.
- You will get a successful or error logs on your console.

## OTPless Package usage

```bash
npm i -S otpless-node-js-auth-sdk
```

```js
//Ignore types for this file
//@ts-ignore
import { UserDetails } from 'otpless-node-js-auth-sdk'

// Send a magic link
await UserDetails.magicLink(mobile, email, redirectURI, channel, clientId, clientSecret)

// Verify code from magic link's approved redirected URI's params
await UserDetails.verifyCode(code, clientId, clientSecret)

// Verify token from frontend (OTPless)
await UserDetails.verifyToken(token, clientId, clientSecret)

// Send OTP
await UserDetails.sendOTP(sendTo, orderId, hash, clientId, clientSecret, channel, otpLength)

// Resend OTP
await UserDetails.resendOTP(orderId, clientId, clientSecret)

// Verify OTP
await UserDetails.verifyOTP(sendTo, orderId, otp, clientId, clientSecret)
```

### Check out [Official Documentation](https://otpless.com/platforms/node) for more details

## Thank you

