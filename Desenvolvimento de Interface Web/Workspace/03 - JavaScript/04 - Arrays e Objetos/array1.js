const arr = [1, 5, 10, "ola", true]

arr.forEach(function(el, i, arr){
    console.log(i+" - "+el)
})

let arr1 = arr.filter(function(el, i, arr){
    return typeof el === "number"
})
console.log(arr1)
arr1 = arr1.map(function(el, i, arr){
    return el * el
})
console.log(arr1)