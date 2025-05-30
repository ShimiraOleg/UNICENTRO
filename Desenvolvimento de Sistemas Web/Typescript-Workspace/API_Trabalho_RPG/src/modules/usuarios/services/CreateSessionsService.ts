import { getCustomRepository } from "typeorm";
import Usuario from "../typeorm/entities/Usuario";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";
import { compare } from "bcryptjs";
import { sign } from "jsonwebtoken";
import auth from "@config/auth";

interface IRequest{
    email: string;
    senha: string;
}

interface IResponse{
    usuario: Usuario;
    token: string;
}

export default class CreateSessionsService{
    public async execute({email, senha} : IRequest) : Promise<IResponse>{
        const usuarioRepository = getCustomRepository(UsuariosRepository);
        const usuario = await usuarioRepository.findByEmail(email);
        if(!usuario){
            throw new AppError('Combinação errada de senha/email', 401);
        }
        const senhaConfirmed = await compare(senha, usuario.senha);
        if(!senhaConfirmed){
            throw new AppError('Combinação errada de senha/email', 401);
        }
        const token = sign({}, auth.jwt.secret, {
            subject: usuario.id,
            expiresIn: '1h'
        });
        return {usuario, token};
    }
}