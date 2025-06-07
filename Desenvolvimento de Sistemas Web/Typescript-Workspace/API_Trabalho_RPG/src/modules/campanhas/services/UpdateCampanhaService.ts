import { getCustomRepository } from "typeorm";
import Campanha from "../typeorm/entities/Campanha";
import CampanhasRepository from "../typeorm/repositories/CampanhasRepository";
import UsuariosRepository from "@modules/usuarios/typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";

interface IRequest{
    campanha_id: string;
    nome: string;
    descricao?: string;
    sistema_rpg: string;
    nivel_max: number;
    status: string;
    mestre_id: string;
}

export default class UpdateCampanhaService{
    public async execute({campanha_id, nome, descricao, sistema_rpg, nivel_max, status, mestre_id}: IRequest): Promise<Campanha>{
        const campanhasRepository = getCustomRepository(CampanhasRepository);

        const campanha = await campanhasRepository.findById(campanha_id);
        if(!campanha){
            throw new AppError('Campanha não encontrado.');
        }
        if(campanha.mestre_id !== mestre_id){
            throw new AppError('Você não tem permissão para editar esta campanha.', 403);
        }
        if(nome && nome !== campanha.nome){
            const campanhaNome = await campanhasRepository.findByName(nome);
            if(campanhaNome && campanhaNome.id !== campanha_id){
                throw new AppError('Já existe uma campanha com esse nome.');
            }
        }
        campanha.nome = nome;
        campanha.descricao = descricao;
        campanha.sistema_rpg = sistema_rpg;
        campanha.nivel_max = nivel_max;
        campanha.status = status;
        await campanhasRepository.save(campanha);
        return campanha;
    }

}