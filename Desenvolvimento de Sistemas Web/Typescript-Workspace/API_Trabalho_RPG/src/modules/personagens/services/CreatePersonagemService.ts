import { getCustomRepository } from "typeorm";
import PersonagensRepository from "../typeorm/repositories/PersonagensRepository";
import CampanhasRepository from "@modules/campanhas/typeorm/repositories/CampanhasRepository";
import UsuariosRepository from "@modules/usuarios/typeorm/repositories/UsuariosRepository";
import AppError from "@shared/errors/AppError";
import Personagem from "../typeorm/entities/Personagem";

interface IRequest{
    nome: string;
    classe: string;
    raca: string;
    nivel: number;
    atributos: object;
    jogador_id: string;
    campanha_id: string;
}

export default class CreatePersonagemService{
    public async execute({nome, classe, raca, nivel, atributos, jogador_id, campanha_id}: IRequest): Promise<Personagem>{
        const personagensRepository = getCustomRepository(PersonagensRepository)
        const campanhasRepository = getCustomRepository(CampanhasRepository);
        const usuariosRepository = getCustomRepository(UsuariosRepository);

        const jogadorExists = await usuariosRepository.findById(jogador_id);
        if(!jogadorExists){
            throw new AppError('Usuario não encontrado.');
        }

        const campanhaExists = await campanhasRepository.findById(campanha_id);
        if(!campanhaExists){
            throw new AppError('Campanha não encontrada.');
        }
        const nivelPersonagem = nivel;
        if(nivelPersonagem > campanhaExists.nivel_max){
            throw new AppError(`O nível máximo permitido nesta campanha é ${campanhaExists.nivel_max}.`);
        }
        const personagemExists = await personagensRepository.findByName(nome);
        console.log(personagemExists)
        if(personagemExists){
            throw new AppError('Já existe um personagem com esse nome nesta campanha.');
        }
        const personagem = personagensRepository.create({nome, classe, raca, nivel, atributos , jogador_id, campanha_id});
        await personagensRepository.save(personagem);
        return personagem;
    }

}