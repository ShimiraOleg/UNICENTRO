import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("aulajotair-firebase.json")
app = firebase_admin.initialize_app(cred)

print(app)

db = firestore.client()
db.collection('usuarios').document('user_001').set({
    'nome': 'João Silva',
    'email': 'joao@email.com',
    'idade': 30
})