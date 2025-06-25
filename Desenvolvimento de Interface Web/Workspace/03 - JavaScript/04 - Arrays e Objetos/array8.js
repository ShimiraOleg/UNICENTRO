const arr1 = new Array(1,2,3)
console.log(arr1)
const arr2 = Array.from(arr1)
console.log(arr2)
const arr3 = Array.of(10)
console.log(arr3)

for(n of arr1){
    console.log(n)
}