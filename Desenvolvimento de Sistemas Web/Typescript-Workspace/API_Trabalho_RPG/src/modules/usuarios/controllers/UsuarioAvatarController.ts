import { NextFunction, Request, Response } from "express";
import UpdateUsuarioAvatarService from "../services/UpdateUsuarioAvatarService";


export default class UsuarioAvatarController{
    public async update(request: Request, response: Response, next: NextFunction) : Promise<Response|void>{
        try{
            const updateAvatar = new UpdateUsuarioAvatarService();
            const usuario = updateAvatar.execute({usuario_id: request.usuario.id, avatarFileName: request.file?.filename as string});
            return response.json(usuario);
        } catch (err) {
            next(err);
        }
    }
}