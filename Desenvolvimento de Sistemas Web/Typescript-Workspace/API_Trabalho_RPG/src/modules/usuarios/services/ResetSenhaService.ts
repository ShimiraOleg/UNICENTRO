import { getCustomRepository } from "typeorm";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";
import UsuarioTokensRepository from "../typeorm/repositories/UsuarioTokensRepository";
import AppError from "@shared/errors/AppError";
import { addHours, isAfter } from "date-fns";
import { hash } from "bcryptjs";

interface IRequest{
    token: string;
    senha: string;
}

export default class ResetSenhaService{
    public async execute({ token, senha }: IRequest): Promise<void>{
        const usuariosRepository = getCustomRepository(UsuariosRepository);
        const usuariosTokensRepository = getCustomRepository(UsuarioTokensRepository);
        const usuarioToken = await usuariosTokensRepository.findByToken(token);
        if(!usuarioToken){
            throw new AppError('Usuario Token não existe.');
        }
        const usuario = await usuariosRepository.findById(usuarioToken.usuario_id);
        if(!usuario){
            throw new AppError('O usuario não existe.')
        }
        const tokenCreatedAt = usuarioToken.created_at;
        const compareDate = addHours(tokenCreatedAt, 2);
        if(isAfter(Date.now(), compareDate)){
            throw new AppError('O token expirou');
        }
        usuario.senha = await hash(senha, 8);
        await usuariosRepository.save(usuario)
    }
}