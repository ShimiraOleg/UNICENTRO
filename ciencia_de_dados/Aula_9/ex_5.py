import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("aulajotair-firebase.json")
firebase_admin.initialize_app(cred)

bucket = storage.bucket("aulajotair.appspot.com")
blob = bucket.blob(f"uploads/{"teste.txt"}")
blob.upload_from_filename("teste.txt", content_type="text/plain")
