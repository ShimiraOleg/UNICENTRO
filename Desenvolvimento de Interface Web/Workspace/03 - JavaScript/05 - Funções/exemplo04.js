function fn(cb){
    console.log('Executar função de callback')
    console.log(typeof cb)
    cb() 
}

function callback(){
    console.log("Função passada como parâmetro")
}

fn(callback)

const objeto = {
    nome : "teste",
    callback
}
