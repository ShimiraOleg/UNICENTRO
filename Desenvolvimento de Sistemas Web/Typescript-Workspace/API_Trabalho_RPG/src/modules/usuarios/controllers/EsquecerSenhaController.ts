import { NextFunction, Request, Response } from "express";
import SendSenhaEsquecidaEmailService from "../services/SendSenhaEsquecidaEmailService";

export default class EsquecerSenhaController{
    public async create(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const { email } = request.body;
            const sendSenhaEsquecidaEmailService = new SendSenhaEsquecidaEmailService();
            await sendSenhaEsquecidaEmailService.execute({email});
            return response.status(204).json();
        }catch(err){
            next(err);
        }
    }
}