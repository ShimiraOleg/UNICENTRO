function operacoesComDoisNumeros(num1, num2) {    
    if (isNaN(num1) || isNaN(num2)) {
        console.log("Erro: Por favor, digite números válidos.");
        return;
    }
    
    const soma = num1 + num2;
    const subtracao = num1 - num2;
    const multiplicacao = num1 * num2;
    const divisao = num2 !== 0 ? num1 / num2 : "Divisão por zero!";
    const resto = num2 !== 0 ? num1 % num2 : "Divisão por zero!";
    
    console.log(`Números: ${num1} e ${num2}`);
    console.log(`Soma: ${soma}`);
    console.log(`Subtração: ${subtracao}`);
    console.log(`Multiplicação: ${multiplicacao}`);
    console.log(`Divisão: ${divisao}`);
    console.log(`Resto da divisão: ${resto}`);
}

function verificarMaioridade(idade) {    
    if (isNaN(idade) || idade < 0) {
        console.log("Erro: Por favor, digite uma idade válida.");
        return;
    }
    
    if (idade >= 18) {
        console.log(`Idade: ${idade} anos - Você é maior de idade.`);
    } else {
        console.log(`Idade: ${idade} anos - Você é menor de idade.`);
    }
}

function contadorDeUmAteN(n) {
    if(n === undefined){
        throw Error("valor inválido")
    }
    
    if (isNaN(n) || n <= 0) {
        console.log("Erro: Por favor, digite um número inteiro positivo.");
        return;
    }
    
    console.log(`Contando de 1 até ${n}:`);
    for (let i = 1; i <= n; i++) {
        console.log(i);
    }
}

function somaNumeroImpares() {
    const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
    let soma = 0;
    let impares = [];
    
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 !== 0) {
            soma += array[i];
            impares.push(array[i]);
        }
    }
    
    console.log(`Array: [${array.join(', ')}]`);
    console.log(`Números ímpares: [${impares.join(', ')}]`);
    console.log(`Soma dos números ímpares: ${soma}`);
}

function calcularIMC(peso, altura) {
    if(peso === undefined || altura === undefined){
        throw Error("valores inválidos")
    }    
    const imc = peso / (altura * altura);
    let classificacao;
    
    if (imc < 18.5) {
        classificacao = "Abaixo do peso";
    } else if (imc < 25) {
        classificacao = "Peso normal";
    } else if (imc < 30) {
        classificacao = "Sobrepeso";
    } else if (imc < 35) {
        classificacao = "Obesidade grau 1";
    } else if (imc < 40) {
        classificacao = "Obesidade grau 2";
    } else {
        classificacao = "Obesidade grau 3";
    }
    
    console.log(`Peso: ${peso} kg`);
    console.log(`Altura: ${altura} m`);
    console.log(`IMC: ${imc.toFixed(2)}`);
    console.log(`Classificação: ${classificacao}`);
}

function numeroParOuImpar(numero) {
    if (numero % 2 === 0) {
        console.log(`O número ${numero} é par.`);
    } else if (numero % 2 !== 0) {
        console.log(`O número ${numero} é ímpar.`);
    } else {
        console.log(`valor inválido`);
    }
}

function contadorRegressivo(num) {
    console.log(`Contagem regressiva de ${num} até 0:`);
    for (let i = num; i >= 0; i--) {
        console.log(i);
    }
}

function mediaDeNotas(nota1, nota2, nota3, nota4) {
    const media = (nota1 + nota2 + nota3 + nota4) / 4;
    console.log(`Notas: ${nota1}, ${nota2}, ${nota3}, ${nota4}`);
    console.log(`Média: ${media.toFixed(2)}`);
    if (media >= 7) {
        console.log("APROVADO");
    } else {
        console.log("REPROVADO");
    }
}

function maiorValorDaLista() {
    const array = [45, 23, 67, 89, 12, 34, 56, 78, 90, 11];
    let maior = array[0];
    for (let i = 1; i < array.length; i++) {
        if (array[i] > maior) {
            maior = array[i];
        }
    }
    
    console.log(`Array: [${array.join(', ')}]`);
    console.log(`Maior número: ${maior}`);
}

function inversorDePalavra(palavra) {
    let palavraInvertida = "";
    for (let i = palavra.length - 1; i >= 0; i--) {
        palavraInvertida += palavra[i];
    }
    
    console.log(`Texto original: "${palavra}"`);
    console.log(`Texto invertido: "${palavraInvertida}"`);
}

operacoesComDoisNumeros(5, 5);
verificarMaioridade(17);
contadorDeUmAteN(5);
somaNumeroImpares();
calcularIMC(110, 2);
numeroParOuImpar(3);
contadorRegressivo(4);
mediaDeNotas(5,6,7,9);
maiorValorDaLista();
inversorDePalavra("Teste");