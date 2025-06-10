import { getCustomRepository } from "typeorm";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";
import AppError from "@shared/errors/AppError";
import { debug } from "console";

interface IRequest{
    personagem_id: string;
    usuario_id: string;
}

export default class DeletePersonagemService{
    public async execute({personagem_id, usuario_id}: IRequest): Promise<void>{
        const personagensRepository = getCustomRepository(PersonagensRepository);

        const personagem = await personagensRepository.findByIdWithRelations(personagem_id);
        if(!personagem){
            throw new AppError('Personagem não encontrado.');
        }
        const isDono = personagem.jogador_id === usuario_id;
        const isMestre = personagem.campanha?.mestre_id === usuario_id;
        if(!isDono && !isMestre){
            throw new AppError('Você não tem permissão para editar este personagem.', 403);
        }
        await personagensRepository.remove(personagem);
    }
}