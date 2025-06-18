let arr = [1,2,3]
arr.reverse()
console.log(arr)

let soma = arr.reduce(function(acumulador, atual) {
    console.log("ac: "+ acumulador)
    console.log("at: "+ atual)
    return acumulador + atual
})
console.log("soma: " +soma)
console.log(arr)