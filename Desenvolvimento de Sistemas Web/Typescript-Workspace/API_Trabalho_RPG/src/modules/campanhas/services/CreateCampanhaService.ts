import { getCustomRepository } from "typeorm";
import Campanha from "../typeorm/entities/Campanha";
import CampanhasRepository from "../typeorm/repositories/CampanhasRepository";
import UsuariosRepository from "@modules/usuarios/typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";

interface IRequest{
    nome: string;
    descricao?: string;
    sistema_rpg: string;
    nivel_max: number;
    status: string;
    mestre_id: string;
}

export default class CreateCampanhaService{
    public async execute({nome, descricao, sistema_rpg, nivel_max, status, mestre_id}: IRequest): Promise<Campanha>{
        const campanhasRepository = getCustomRepository(CampanhasRepository);
        const usuariosRepository = getCustomRepository(UsuariosRepository);

        const mestre = await usuariosRepository.findById(mestre_id);
        if(!mestre){
            throw new AppError('Usuario não encontrado.');
        }

        const campanhaExists = await campanhasRepository.findByName(nome);
        if(campanhaExists){
            throw new AppError('Já existe uma campanha com esse nome.');
        }
        const campanha = campanhasRepository.create({nome, descricao, sistema_rpg, nivel_max, status, mestre_id});
        await campanhasRepository.save(campanha);
        return campanha;
    }

}