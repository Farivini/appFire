import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDkEx9ftZV0JsnPZHI4uweWxlUN2Rgj0qo",
  "authDomain": "fir-pucpr-319c0.firebaseapp.com",
  "projectId": "fir-pucpr-319c0",
  "storageBucket": "fir-pucpr-319c0.appspot.com",
  "messagingSenderId": "1045479024431",
  "appId": "1:1045479024431:web:d058571d05a033644c63da",
  "measurementId": "G-CDDKCH4MMQ",
  "databaseURL": "https://fir-pucpr-319c0-default-rtdb.firebaseio.com/"
}
fire = pyrebase.initialize_app(firebaseConfig)
auth = fire.auth()