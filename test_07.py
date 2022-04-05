# Date: 06/04/2022
# This will test firebase Move-I-love
# -----------------------------------------------------
# TEST SUCCESSFULLY

import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDZbOm0SpVvvhGfnobnZTGv6MvApC2p6AA",
  "authDomain": "movies-i-love-30945.firebaseapp.com",
  "databaseURL": "https://movies-i-love-30945-default-rtdb.firebaseio.com",
  "projectId": "movies-i-love-30945",
  "storageBucket": "movies-i-love-30945.appspot.com",
  "messagingSenderId": "649726111436",
  "appId": "1:649726111436:web:ae793845f75bfa3337dc69",
  "measurementId": "G-BFKEBZSQGY"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# push data
data = {
    "name": "John",
    "age": 20,
    "address": ["New York", "Los Angeles"]
}
db.push(data)
