function formatarNome(nomeCompleto){
    nomeCompleto = nomeCompleto.trim()
    let primeiroEspaco = nomeCompleto.indexOf(" ")
    if (primeiroEspaco < 0){
        return nomeCompleto
    }
    let primeiroNome = nomeCompleto.slice(0, primeiroEspaco)
    let sobrenome = nomeCompleto.slice(primeiroEspaco + 1)
    return sobrenome+", "+primeiroNome
}

console.log(formatarNome("Mateus"))
console.log(formatarNome("Mateus Lopes"))
console.log(formatarNome("Mateus de Oliveira Lopes"))