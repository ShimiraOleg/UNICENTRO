import { getCustomRepository } from "typeorm";
import Usuario from "../typeorm/entities/Usuario";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";
import { hash } from "bcryptjs";

interface IRequest{
    nome: string;
    email: string;
    senha: string;
    descricao?: string;
}

export default class CreateUsuarioService{
    public async execute({nome, email, senha, descricao}: IRequest) : Promise<Usuario>{
        const usuariosRepository = getCustomRepository(UsuariosRepository);
        const emailExists = await usuariosRepository.findByEmail(email);
        if(emailExists){
            throw new AppError('O endereço de Email já está sendo usado');
        }
        const hashedPassword = await hash(senha, 8)
        const usuario = usuariosRepository.create({nome, email, senha : hashedPassword, descricao});
        await usuariosRepository.save(usuario);
        return usuario;
    }
}