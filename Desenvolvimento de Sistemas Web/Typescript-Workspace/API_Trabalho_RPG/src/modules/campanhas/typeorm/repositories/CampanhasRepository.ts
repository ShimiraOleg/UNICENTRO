import { EntityRepository, Repository } from "typeorm";
import Campanha from "../entities/Campanha";

@EntityRepository(Campanha)
export default class CampanhaRepository extends Repository<Campanha>{
    public async findByName(nome: string) : Promise <Campanha | undefined>{
        const campanha = this.findOne({where: {nome}});
        return campanha;
    }
    public async findById(id: string) : Promise <Campanha | undefined>{
        const campanha = this.findOne({where: {id}});
        return campanha;
    }
    public async findByMestreId(mestre_id: string) : Promise <Campanha[]>{
        const campanhas = this.find({where : {mestre_id}});
        return campanhas;
    }
}