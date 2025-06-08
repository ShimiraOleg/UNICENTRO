import { getCustomRepository } from "typeorm";
import Personagem from "../typeorm/entities/Personagem";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";
import AppError from "@shared/errors/AppError";

interface IRequest {
    personagem_id: string;
}

export default class ShowPersonagemService {
    public async execute({ personagem_id }: IRequest): Promise<Personagem> {
        const personagensRepository = getCustomRepository(PersonagensRepository);
        const personagem = await personagensRepository.findById(personagem_id);
        if (!personagem) {
            throw new AppError('Personagem não encontrado.');
        }
        return personagem;
    }
}