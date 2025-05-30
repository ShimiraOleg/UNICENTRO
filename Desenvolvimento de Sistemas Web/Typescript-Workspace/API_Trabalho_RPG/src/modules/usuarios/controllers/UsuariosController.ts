import { NextFunction, Request, Response } from "express";
import ListUsuarioService from "../services/ListUsuarioService";
import CreateUsuarioService from "../services/CreateUsuarioService";

export default class UsuariosController{
    public async index(request: Request, response: Response, next: NextFunction) : Promise<Response | void>{
        try{
            const listUsuario = new ListUsuarioService();
            const usuarios = await listUsuario.execute();
            return response.json(usuarios);
        }catch(err){
            next(err);
        }
    }

    public async create(request: Request, response: Response, next: NextFunction) : Promise<Response | void>{
        try{
            const {nome, email, senha, descricao} = request.body;
            const createUsuario = new CreateUsuarioService();
            const usuario = await createUsuario.execute({nome, email, senha, descricao})
            return response.json(usuario);
        }catch(err){
            next(err);
        }
    }
}