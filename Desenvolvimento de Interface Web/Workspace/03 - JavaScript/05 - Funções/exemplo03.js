function somar(n1,n2){
    return n1 + n2
}

console.log(somar(1,2))

function somar2(arr){
    let total = 0
    for(let i = 0; i < arr.length; i++){
        total += arr[i]
    }
    return total
}

console.log(somar2([1,2,3]))

function somar3(){
    let total = 0
    for(let i = 0; i < arguments.length; i++){
        total += arguments[i]
    }
    return total
}

console.log(somar2([1,2,3,4,5]))
