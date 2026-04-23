import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

def atualizar_produto(produto_id: str, novo_preco: float):
    ref = db.collection("produto").document(produto_id)
    doc = ref.get()
    if not doc.exists:
        print("O Produto não existe no banco de dados")
        return
    
    ref.update({"preco": novo_preco})
    print(f"Produto '{produto_id}' atualizado | R${novo_preco:.2f}")

cred = credentials.Certificate("aulajotair-firebase.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

atualizar_produto(produto_id="produto_01", novo_preco=499.99)