function calcularIMC(peso, altura){
    if(peso === undefined || altura === undefined){
        throw Error("valores inválidos")
    }
    return peso / (altura * altura)
}

function classificaIMC(imc){
    if(imc <= 16.9) return 'imc muito baixo'
    if(imc <= 18.4) return 'baixo'
    if(imc <= 24.9) return 'normal'
    if(imc <= 29.9) return 'acima do peso'
    if(imc <= 34.9) return 'obesidade grau 1'
    if(imc <= 34.9) return 'obesidade grau 2'
}

let imc = calcularIMC(95, 2.03)
console.log(imc)
console.log(classificaIMC(imc))