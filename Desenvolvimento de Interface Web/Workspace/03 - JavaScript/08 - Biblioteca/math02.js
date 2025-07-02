function getRandomNumber(inicio,fim, integer){
    let r = Math.random() * (fim-inicio+1) + inicio
    return integer ? parseInt(r) : r
}
console.log(getRandomNumber(1,100,true))
console.log(getRandomNumber(1,100,false))