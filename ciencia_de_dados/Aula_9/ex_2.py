import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("aulajotair-firebase.json")
firebase_admin.initialize_app(cred)

novo_usuario = auth.create_user(
    display_name='João Silva',
    email='joao@email.com',
    password="senhada42"
)
    
print(f"Usuário criado com UID: {novo_usuario.uid}")

usuario = auth.get_user(novo_usuario.uid)
print(f"Nome: {usuario.display_name}")
print(f"E-mail: {usuario.email}")
print(f"UID: {usuario.uid}")
print(f"Criado em: {usuario.user_metadata.creation_timestamp}")