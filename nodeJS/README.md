# OTPless SDK integration in Node JS

This is a demo for [OTPless](https://otpless.com) Backend SDK integration in NodeJS.

>> To integrate the same in TypeScript, check out [nodeTS](/nodeTS/) directory.

## Follow the steps below to get started

***Pre-requisites:* - [Node](https://nodejs.org) installed**

### Step 1: Run the server

1. Open a new terminal in [nodeJS](/nodeJS/) directory.
2. Create a new File `.env` in the root directory and copy and paste contents of `.env.example`
3. Replace the values of each env variables with your own.
4. Install the required dependencies

    ```bash
    npm i
    ```

5. Start the server

    ```bash
    npm run dev
    ```

### Step 2: Send requests to the server(using Postman)

- Import the [Request Collection Config](./assets/OTPless-Node-API.postman_collection.json) file in your Postman Client APP.
- `CTRL+O` > Drop the file in the Popup window > Import.
- Set the `Current Value` for the `Variables` in the root of the collection.
- **Thats it!** Open the requests provide required data in the body or params, and Hit Send Request.
- You will get a successful or error response based on your request.

## OTPless Package use

```bash
npm i -S otpless-node-js-auth-sdk
```

```js
import { UserDetails } from 'otpless-node-js-auth-sdk'

// Send a magic link
await UserDetails.magicLink(mobile, email, redirectURI, channel, clientId, clientSecret)

// Verify code from magic link's approved redirected URI's params
await UserDetails.verifyCode(code, clientId, clientSecret)

// Verify token from OTPless frontend SDK
await UserDetails.verifyToken(token, clientId, clientSecret)

// Send OTP
await UserDetails.sendOTP(phoneNumber, email, channel, hash, orderId, expiry, otpLength, clientId, clientSecret)

// Resend OTP
await UserDetails.resendOTP(orderId, clientId, clientSecret)

// Verify OTP
await UserDetails.verifyOTP(email, phoneNumber, orderId, otp, clientId, clientSecret)
```

> Note: Arguments for all methods are positional and should be in the same order, to skip optional arguments use `null` or `undefined`.

### Check out [Official Documentation](https://otpless.com/platforms/node) for more details

## Thank you
