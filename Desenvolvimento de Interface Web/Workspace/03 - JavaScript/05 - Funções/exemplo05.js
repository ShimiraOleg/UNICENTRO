function fn2(n1){
    return function(n2){
        return n1*n2;
    }
}

const funcao2 = fn2(10)
console.log(funcao2)
const mult = funcao2(2)
console.log(mult)