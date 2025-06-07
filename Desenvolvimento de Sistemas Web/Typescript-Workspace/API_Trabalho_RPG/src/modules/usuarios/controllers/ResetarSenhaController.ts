import { NextFunction, Request, Response } from "express";
import ResetSenhaService from "../services/ResetSenhaService";

export default class ResetarSenhaController{
    public async create(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const { token, senha } = request.body;
            const resetarSenha = new ResetSenhaService();
            await resetarSenha.execute({ token, senha });
            return response.status(204).json();
        }catch(err){
            next(err);
        }
    }
}