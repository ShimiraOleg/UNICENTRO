const arr1 = [1,2,3]
show(1,2,3)
show(arr1)
show(...arr1)

function show(){
    console.log(arguments)
    console.log(arguments.length)
}

let[n1] = arr1
console.log(n1)
let[n2, n3] = arr1
console.log(n2)
console.log(n3)