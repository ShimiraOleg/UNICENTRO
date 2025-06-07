import { getCustomRepository } from "typeorm";
import Campanha from "../typeorm/entities/Campanha";
import CampanhaRepository from "../typeorm/repositories/CampanhasRepository";
import AppError from "@shared/errors/AppError";

interface IRequest{
    id: string;
}

export default class ShowCampanhaService{
    public async execute({id} : IRequest): Promise<Campanha>{
        const campanhasRepository = getCustomRepository(CampanhaRepository);

        const campanha = await campanhasRepository.findById(id);
        if(!campanha){
            throw new AppError('Campanha não encontrada.');
        }
        return campanha;
    }
}