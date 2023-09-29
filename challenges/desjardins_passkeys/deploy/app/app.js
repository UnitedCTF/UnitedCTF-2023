import Passage from "@passageidentity/passage-node";
import { createRequire } from "module";
const require = createRequire(import.meta.url);

require('dotenv').config()
const https = require("https");
const fs = require("fs");
const express = require('express')
const app = express()
const port = process.env.PORT
app.set('views', './frontend');
app.engine('html', require('ejs').renderFile);

// Passage requires an App ID and, optionally, an API Key
const passageConfig = {
  appID: process.env.PASSAGE_APP_ID,
  apiKey: process.env.PASSAGE_API_KEY,
};

app.get('/', (req, res) => {
	res.render('index.html');
})

// example of passage middleware
let passage = new Passage(passageConfig);
let passageAuthMiddleware = (() => {
    return async (req, res, next) => {
        try {
            let userID = await passage.authenticateRequest(req);
            if (userID) {
              // user authenticated
              res.userID = userID;  
              next();
            }
        } catch(e) {
            // failed to authenticate
            // we recommend returning a 401 or other "unauthorized" behavior
            console.log(e);
            res.status(401).send('Could not authenticate user!');
        }
    }
})();

app.get('/flag', passageAuthMiddleware, async(req, res) => {
  try {
    let userID = res.userID;
    let passageUser = await passage.user.get(userID);
    console.log('user', passageUser)
    if (passageUser.login_count <= 1) {
      res.render('first_signup.html')
    } else if (!passageUser.webauthn) {
      res.send('not registred using webauthn')
    } else if(passageUser.webauthn_types.includes('passkey')) {
      res.render('flag_passkey.html');
    } else if (passageUser.webauthn_types.includes('platform')) {
      res.render('flag_platform.html')
    }
  } catch (err) {
    console.log('error', err);
  }
})

https.createServer({
  
    key: fs.readFileSync("key.pem"),
    cert: fs.readFileSync("cert.pem"),

}, app).listen(port, '0.0.0.0', () => {
  console.log(`Example app listening on port ${port}`)
})