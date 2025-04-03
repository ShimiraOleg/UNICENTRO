import cliente from "./cliente";
import endereco from "./endereco";
import produto from "./produto";
import telefone from "./telefone";
import venda from "./venda";

let tel1 = Object.assign(new telefone("42", 99990001, "fixo"));
let tel2 = Object.assign(new telefone("43", 98880001, "celular"));
let end = Object.assign(new endereco("Guarani", 227, "Imbaú", "PR"));
let cli = Object.assign(new cliente("Raul", 10010056712, 15122003, "M", end));
cli.telefones = [tel1, tel2];
let pro1 = Object.assign(new produto(16,"Notebook Acer", 2000));
let pro2 = Object.assign(new produto(17,"Mouse Red Dragon", 300));
let ven = Object.assign(new venda(200, 12152025, cli));
ven.produtos = [pro1, pro2];


console.log(cli)
console.log(ven)

