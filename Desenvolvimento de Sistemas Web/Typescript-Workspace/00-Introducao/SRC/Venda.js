"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Venda = /** @class */ (function () {
    function Venda(codigo, data, cliente) {
        this._codigo = codigo;
        this._data = data;
        this._cliente = cliente;
    }
    Object.defineProperty(Venda.prototype, "codigo", {
        get: function () {
            return this._codigo;
        },
        set: function (codigo) {
            this._codigo = codigo;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Venda.prototype, "data", {
        get: function () {
            return this._data;
        },
        set: function (data) {
            this._data = data;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Venda.prototype, "cliente", {
        get: function () {
            return this._cliente;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Venda.prototype, "produtos", {
        get: function () {
            return this._produtos;
        },
        set: function (produtos) {
            this._produtos = produtos;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Venda.prototype, "clente", {
        set: function (cliente) {
            this._cliente = cliente;
        },
        enumerable: false,
        configurable: true
    });
    Venda.prototype.calcularTotal = function (produtos) {
        var valor;
        valor = produtos[1].valor;
        return valor;
    };
    return Venda;
}());
exports.default = Venda;
