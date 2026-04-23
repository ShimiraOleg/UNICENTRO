import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("aulajotair-firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
 
consulta = (
    db.collection("produto").where("preco", ">", 100)
)
 
resultados = consulta.stream()
 
print(f"=== Produtos com preços maiores que 100 reais ===")
encontrou = False
for doc in resultados:
    dados = doc.to_dict()
    nome = dados.get("nome", "(sem nome)")
    preco = dados.get("preco", 0)
    print(f"{nome}: R$ {preco:.2f}")
    encontrou = True
 
if not encontrou:
    print("Nenhum produto encontrado.")
