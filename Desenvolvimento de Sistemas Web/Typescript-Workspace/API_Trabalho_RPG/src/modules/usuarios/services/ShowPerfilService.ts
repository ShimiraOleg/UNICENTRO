import AppError from "@shared/errors/AppError"
import Usuario from "../typeorm/entities/Usuario";
import { getCustomRepository } from "typeorm";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";

interface IRequest{
    usuario_id: string;
}

export default class ShowPerfilService{
    public async execute({usuario_id}: IRequest): Promise<Usuario>{
        const usuarioRepository = getCustomRepository(UsuariosRepository);
        const usuario = await usuarioRepository.findById(usuario_id);
        if(!usuario){
            throw new AppError('Usuário não encontrado.');
        }
        return usuario;
    }
}