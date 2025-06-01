import { getCustomRepository } from "typeorm";
import Usuario from "../typeorm/entities/Usuario";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";
import path from "path";
import uploadConfig from "@config/upload";
import fs from "fs";

interface IRequest{
    usuario_id: string;
    avatarFileName: string;
}

export default class UpdateUsuarioAvatarService{
    public async execute({usuario_id, avatarFileName}: IRequest) : Promise<Usuario>{
        const usuariosRepository = getCustomRepository(UsuariosRepository);
        const usuario = await usuariosRepository.findById(usuario_id);
        if(!usuario){
            throw new AppError('Usuário não encontrado.');
        }
        if(usuario.avatar){
            const usuarioAvatarFilePath = path.join(uploadConfig.directory, usuario.avatar);
            const usuarioAvatarFileExists = await fs.promises.stat(usuarioAvatarFilePath);
            if(usuarioAvatarFileExists){
                await fs.promises.unlink(usuarioAvatarFilePath);
            }
        }
        usuario.avatar = avatarFileName;
        await usuariosRepository.save(usuario);
        return usuario;
    }
}