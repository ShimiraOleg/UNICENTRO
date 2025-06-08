import { getCustomRepository } from "typeorm";
import Personagem from "../typeorm/entities/Personagem";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";
import { console } from "inspector";

interface IRequest {
    campanha_id: string;
}

export default class ListCampanhaPersonagensService {
    public async execute({ campanha_id }: IRequest): Promise<Personagem[]> {
        const personagensRepository = getCustomRepository(PersonagensRepository);
        const personagens = await personagensRepository.findByCampanhaId(campanha_id);
        return personagens;
    }
}