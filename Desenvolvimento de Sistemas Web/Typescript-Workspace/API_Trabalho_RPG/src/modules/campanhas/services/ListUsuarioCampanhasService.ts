import { getCustomRepository } from "typeorm";
import Campanha from "../typeorm/entities/Campanha";
import CampanhasRepository from "../typeorm/repositories/CampanhasRepository";

interface IRequest{
    mestre_id: string;
}

export default class ListUsuarioCampanhasService{
    public async execute({mestre_id}: IRequest): Promise<Campanha[]>{
        const campanhasRepository = getCustomRepository(CampanhasRepository)
        const campanhas = await campanhasRepository.findByMestreId(mestre_id);
        return campanhas;
    }
}