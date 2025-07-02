let numero = 16
console.log(numero.toString())
console.log(numero.toString(2))
console.log(numero.toString(16))
numero = 123456.789
console.log(numero.toLocaleString("pt-br"))
console.log(numero.toLocaleString("pt-br", {style: "currency", currency:"BRL"}))
console.log(Number.MIN_VALUE)
console.log(Number.MAX_VALUE)
console.log(isNaN("Teste"))
console.log(isNaN(1))