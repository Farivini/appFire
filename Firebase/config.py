import pyrebase

firebaseConfig = {
  "apiKey": "sua api",
  "authDomain": "firebaseapp.com",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": "",
  "databaseURL": ""
}
fire = pyrebase.initialize_app(firebaseConfig)
auth = fire.auth()