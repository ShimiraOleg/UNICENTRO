"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Telefone = /** @class */ (function () {
    function Telefone(ddd, numero, tipo) {
        this._ddd = ddd;
        this._numero = numero;
        this._tipo = tipo;
    }
    Object.defineProperty(Telefone.prototype, "ddd", {
        get: function () {
            return this._ddd;
        },
        set: function (ddd) {
            this._ddd = ddd;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Telefone.prototype, "numero", {
        get: function () {
            return this._numero;
        },
        set: function (numero) {
            this._numero = numero;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Telefone.prototype, "tipo", {
        get: function () {
            return this._tipo;
        },
        set: function (tipo) {
            this._tipo = tipo;
        },
        enumerable: false,
        configurable: true
    });
    return Telefone;
}());
exports.default = Telefone;
