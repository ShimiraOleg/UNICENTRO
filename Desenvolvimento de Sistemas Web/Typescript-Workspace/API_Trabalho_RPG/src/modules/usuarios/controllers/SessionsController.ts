import { NextFunction, Request, Response } from "express";
import CreateSessionsService from "../services/CreateSessionsService";

export default class SessionsController{
    public async create(request: Request, response: Response, next: NextFunction) : Promise<Response| void>{
        try{
            const {email, senha} = request.body;
            const createSession = new CreateSessionsService();
            const usuario = await createSession.execute({email, senha});
            return response.json(usuario);
        } catch(err){
            next(err);
        }
    }
}