import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBu9e3ZgeIPidNAGxLe2OHvBE2Wjdcsa1E",
  "authDomain": "python-project-ad7c5.firebaseapp.com",
  "projectId": "python-project-ad7c5",
  "databaseURL": "https://python-project-ad7c5-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "python-project-ad7c5.firebasestorage.app",
  "messagingSenderId": "542898118820",
  "appId": "1:542898118820:web:672fe0469ebcd235db0631",
  "measurementId": "G-BCNQBHWNM3"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()