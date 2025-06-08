import AppError from "@shared/errors/AppError";
import { getCustomRepository } from "typeorm";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";
import Personagem from "../typeorm/entities/Personagem";


interface IRequest{
    personagem_id: string;
    usuario_id: string;
    nome: string;
    classe: string;
    raca: string;
    nivel: number;
    atributos: object;
}

export default class UpdatePersonagemService{
    public async execute({personagem_id, usuario_id, nome, classe, raca, nivel, atributos}: IRequest): Promise<Personagem>{
        const personagensRepository = getCustomRepository(PersonagensRepository);

        const personagem = await personagensRepository.findByIdWithPermissions(personagem_id);
        if(!personagem){
            throw new AppError('Personagem não encontrado.');
        }
        const isDono = personagem.jogador_id === usuario_id;
        const isMestre = personagem.campanha?.mestre_id === usuario_id;
        if(!isDono && !isMestre){
            throw new AppError('Você não tem permissão para editar este personagem.', 403);
        }
        if (nivel !== undefined && nivel > personagem.campanha.nivel_max) {
            throw new AppError(`O nível máximo permitido nesta campanha é ${personagem.campanha.nivel_max}.`);
        }
        if(nome && nome !== personagem.nome){
            const personagemNomeIgual = await personagensRepository.createQueryBuilder('personagem')
                                            .where('personagem.nome = :nome', { nome })
                                            .andWhere('personagem.campanha_id = :campanha_id', {campanha_id: personagem.campanha_id})
                                            .andWhere('personagem.id != :id', {id: personagem_id})
                                            .getOne();
            if(personagemNomeIgual){
                throw new AppError('Já existe uma personagem com esse nome nesta campanha.');
            }
        }
        personagem.nome = nome;
        personagem.classe = classe;
        personagem.raca = raca;
        personagem.nivel = nivel;
        personagem.atributos = atributos;
        await personagensRepository.save(personagem);
        return personagem;
    }
}