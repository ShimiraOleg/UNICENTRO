import { getCustomRepository } from "typeorm";
import Usuario from "../typeorm/entities/Usuario";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";
import { compare, hash } from "bcryptjs";

interface IRequest{
    usuario_id: string;
    nome: string;
    email: string;
    senha?: string;
    senha_antiga?: string;
    descricao?: string;
}

export default class UpdatePerfilService{
    public async execute({usuario_id, nome, email, senha, senha_antiga, descricao}: IRequest): Promise<Usuario>{
        const usuariosRepository = await getCustomRepository(UsuariosRepository);
        const usuario = await usuariosRepository.findById(usuario_id);
        if(!usuario){
            throw new AppError('Usuário não encontrado.');
        }
        const usuarioUpdateEmail = await usuariosRepository.findByEmail(email);
        if(usuarioUpdateEmail && usuarioUpdateEmail.id !== usuario_id){
            throw new AppError("Já existe um usuário cadastrado com esse email.");
        }
        if(senha && !senha_antiga){
            throw new AppError('A senha antiga é necessária.')
        }
        if(senha && senha_antiga){
            const checkSenhaAntiga = await compare(senha_antiga, usuario.senha);
            if(!checkSenhaAntiga){
                throw new AppError("A senha antiga não corresponde a atual.");
            }
            usuario.senha = await hash(senha, 8)
        }
        usuario.nome = nome;
        usuario.email = email;
        usuario.descricao = descricao;

        await usuariosRepository.save(usuario);
        return usuario;
    }
}