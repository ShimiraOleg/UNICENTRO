import { getCustomRepository } from "typeorm";
import Usuario from "../typeorm/entities/Usuario";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";

export default class ListUsuarioService{
    public async execute(): Promise<Usuario[]>{
        const usuarioRepository = getCustomRepository(UsuariosRepository);
        const usuarios = await usuarioRepository.find();
        return usuarios;
    }
}