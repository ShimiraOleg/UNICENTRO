import firebase_admin
from firebase_admin import exceptions as firebase_exceptions
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("aulajotair-firebase.json")
firebase_admin.initialize_app(cred)

email = "usuario_invalido@exemplo.com"
uid_inexistente = "uid_que_nao_existe_000"
 
try:
    usuario = auth.create_user(
        email=email,
        password="senha123",
        display_name="Usuário com Tratamento"
    )
    print(f"Usuário criado: {usuario.uid}")
 
except firebase_exceptions.FirebaseError as e:
        print(f"[ERRO Firebase] Ao criar usuário: {e.code} — {e}")
except Exception as e:
        print(f"[ERRO inesperado] Ao criar usuário: {e}")
 
try:
    usuario = auth.get_user(uid_inexistente)
    print(f"Usuário encontrado: {usuario.display_name}")
 
except auth.UserNotFoundError:
    print(f"[AVISO] Usuário com UID '{uid_inexistente}' não encontrado.")
except firebase_exceptions.FirebaseError as e:
    print(f"[ERRO Firebase] Ao buscar usuário: {e.code} — {e}")
except Exception as e:
    print(f"[ERRO inesperado] Ao buscar usuário: {e}")
