"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Endereco = /** @class */ (function () {
    function Endereco(rua, numero, cidade, estado) {
        this._rua = rua;
        this._numero = numero;
        this._cidade = cidade;
        this._estado = estado;
    }
    Object.defineProperty(Endereco.prototype, "rua", {
        get: function () {
            return this._rua;
        },
        set: function (rua) {
            this._rua = rua;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Endereco.prototype, "numero", {
        get: function () {
            return this._numero;
        },
        set: function (numero) {
            this._numero = numero;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Endereco.prototype, "cidade", {
        get: function () {
            return this._cidade;
        },
        set: function (cidade) {
            this._cidade = cidade;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Endereco.prototype, "estado", {
        get: function () {
            return this._estado;
        },
        set: function (estado) {
            this._estado = estado;
        },
        enumerable: false,
        configurable: true
    });
    return Endereco;
}());
exports.default = Endereco;
