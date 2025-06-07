import { getCustomRepository } from "typeorm";
import Campanha from "../typeorm/entities/Campanha";
import CampanhaRepository from "../typeorm/repositories/CampanhasRepository";

export default class ListCampanhaService{
    public async execute(): Promise<Campanha[]>{
        const campanhasRepository = getCustomRepository(CampanhaRepository);
        const campanhas = await campanhasRepository.find();
        return campanhas;
    }
}