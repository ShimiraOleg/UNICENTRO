import { getCustomRepository } from "typeorm";
import Personagem from "../typeorm/entities/Personagem";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";

export default class ListPersonagemService{
    public async execute(): Promise<Personagem[]>{
        const personagensRepository = getCustomRepository(PersonagensRepository);
        const personagens = await personagensRepository.findAllJogadorCampanha();
        return personagens;
    }
}