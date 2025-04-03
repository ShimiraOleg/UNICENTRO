"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Produto = /** @class */ (function () {
    function Produto(codigo, descricao, valor) {
        this._codigo = codigo;
        this._descricao = descricao;
        this._valor = valor;
    }
    Object.defineProperty(Produto.prototype, "codigo", {
        get: function () {
            return this._codigo;
        },
        set: function (codigo) {
            this._codigo = codigo;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Produto.prototype, "descricao", {
        get: function () {
            return this._descricao;
        },
        set: function (descricao) {
            this._descricao = descricao;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Produto.prototype, "valor", {
        get: function () {
            return this._valor;
        },
        set: function (valor) {
            this._valor = valor;
        },
        enumerable: false,
        configurable: true
    });
    return Produto;
}());
exports.default = Produto;
