import { EntityRepository, Repository } from "typeorm";
import Personagem from "../entities/Personagem";

@EntityRepository(Personagem)
export default class PersonagensRepository extends Repository<Personagem>{
    
}