import { NextFunction, Request, Response } from "express";
import ShowPerfilService from "../services/ShowPerfilService";
import UpdatePerfilService from "../services/UpdatePerfilService";

export default class PerfilController{
    public async show(request: Request, response: Response, next: NextFunction){
        const showPerfil = new ShowPerfilService();
        const usuario_id = request.usuario.id;
        const usuario = await showPerfil.execute({usuario_id});
        return response.json(usuario);
    }
    
    public async update(request: Request, response: Response, next: NextFunction){
        const usuario_id = request.usuario.id;
        const {nome, email, senha, senha_antiga, descricao} = request.body;
        const updatePerfil = new UpdatePerfilService();
        const usuario = await updatePerfil.execute({usuario_id, nome, email, senha, senha_antiga, descricao});
        return response.json(usuario);
    }

}