import { getCustomRepository } from "typeorm";
import Campanha from "../typeorm/entities/Campanha";
import CampanhasRepository from "../typeorm/repositories/CampanhasRepository";

export default class ListCampanhaService{
    public async execute(): Promise<Campanha[]>{
        const campanhasRepository = getCustomRepository(CampanhasRepository);
        const campanhas = await campanhasRepository.find();
        return campanhas;
    }
}