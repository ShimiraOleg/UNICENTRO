import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("aulajotair-firebase.json")
firebase_admin.initialize_app(cred)

topico = "noticias_gerais"
mensagem = messaging.Message(
    title="Nova atualização",
    body="Esse aplicativo possui uma nova versão",
    topic=topico
)

response = messaging.send(mensagem)
print(f"Notificação enviada com sucesso!")
print(f"\nTópico: {topico}")
print(f"Message ID: {response}")
