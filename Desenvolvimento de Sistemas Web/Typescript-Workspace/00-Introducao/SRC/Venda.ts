import cliente from "./Cliente";
import produto from "./Produto";

export default class Venda{
    private _codigo: number;
    private _data: number;
    private _cliente: cliente;
    private _produtos: produto[];

    constructor(codigo: number, data: number, cliente: cliente){
        this._codigo = codigo;
        this._data = data;
        this._cliente = cliente;
    }

    get codigo(): number{
        return this._codigo;
    }

    get data(): number{
        return this._data;
    }

    get cliente(): cliente{
        return this._cliente;
    }

    get produtos(): produto[]{
        return this._produtos;
    }

    set codigo(codigo: number){
        this._codigo = codigo;
    }

    set data(data: number){
        this._data = data;
    }
    set clente(cliente: cliente){
        this._cliente = cliente;
    }

    set produtos(produtos: produto[]){
        this._produtos = produtos;
    }

    calcularTotal(produtos: produto[]){
        let total: number = 0;
        for(var i = 0; i < produtos.length; i++){
            total =+ produtos[i].valor;
        }
        return total;
    }
}