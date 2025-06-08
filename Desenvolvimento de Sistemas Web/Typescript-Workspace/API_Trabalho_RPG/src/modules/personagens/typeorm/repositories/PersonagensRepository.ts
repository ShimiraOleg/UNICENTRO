import { EntityRepository, Repository } from "typeorm";
import Personagem from "../entities/Personagem";

@EntityRepository(Personagem)
export default class PersonagensRepository extends Repository<Personagem>{
    public async findByName(nome: string) : Promise <Personagem | undefined>{
        const personagens = this.findOne({where: {nome}});
        return personagens;
    }
    public async findById(id: string) : Promise <Personagem | undefined>{
        const personagens = this.findOne({where: {id}});
        return personagens;
    }
    public async findByIdWithPermissions(id: string): Promise<Personagem | undefined> {
        const personagem = await this.createQueryBuilder('personagem')
            .leftJoinAndSelect('personagem.jogador', 'jogador')
            .leftJoinAndSelect('personagem.campanha', 'campanha')
            .where('personagem.id = :id', { id })
            .getOne();
        return personagem;
    }
    public async findByJogadorId(jogador_id: string) : Promise <Personagem[]>{
        const personagens = this.find({where: {jogador_id}});
        return personagens;
    }
    public async findByCampanhaId(campanha_id: string) : Promise <Personagem[]>{
        const personagens = this.find({where: {campanha_id}});
        return personagens;
    }
    public async findAllJogadorCampanha() : Promise <Personagem[]>{
        const personagens = this.find({relations:['jogador', 'campanha']});
        return personagens;
    }
}