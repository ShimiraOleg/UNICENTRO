import { getCustomRepository } from "typeorm";
import Personagem from "../typeorm/entities/Personagem";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";

interface IRequest {
    jogador_id: string;
}

export default class ListUsuarioPersonagensService {
    public async execute({ jogador_id }: IRequest): Promise<Personagem[]> {
        const personagensRepository = getCustomRepository(PersonagensRepository);
        const personagens = await personagensRepository.findByJogadorId(jogador_id);
        return personagens;
    }
}