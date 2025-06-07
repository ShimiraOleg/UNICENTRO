import { getCustomRepository } from "typeorm";
import CampanhaRepository from "../typeorm/repositories/CampanhasRepository";
import AppError from "@shared/errors/AppError";

interface IRequest{
    campanha_id: string;
    mestre_id: string;
}

export default class DeleteCampanhaService{
    public async execute({campanha_id, mestre_id} : IRequest): Promise<void>{
        const campanhasRepository = getCustomRepository(CampanhaRepository);

        const campanha = await campanhasRepository.findById(campanha_id);
        if(!campanha){
            throw new AppError('Campanha não encontrada.');
        }
        if(campanha.mestre_id !== mestre_id){
            throw new AppError('Você não tem permissão para deletar esta campanha.', 403);
        }
        await campanhasRepository.remove(campanha);
    }
}