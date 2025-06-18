const arr = [1, 5, 10, "ola", true]

let sohNumeros = arr.some(function(el){
    return typeof el === "number"
})
console.log(sohNumeros)