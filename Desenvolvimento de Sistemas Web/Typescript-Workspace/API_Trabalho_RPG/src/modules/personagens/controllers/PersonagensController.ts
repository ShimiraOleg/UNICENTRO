import { NextFunction, Request, Response } from "express";
import ListPersonagemService from "../services/ListPersonagemService";
import ListCampanhaPersonagensService from "../services/ListCampanhaPersonagensService";
import ShowPersonagemService from "../services/ShowPersonagemService";
import CreatePersonagemService from "../services/CreatePersonagemService";
import UpdatePersonagemService from "../services/UpdatePersonagemService";
import DeletePersonagemService from "../services/DeletePersonagemService";

export default class PersonagensController{
    public async index(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const listPersonagens = new ListPersonagemService();
            const personagens = await listPersonagens.execute();
            return response.json(personagens);
        }catch(err){
            next(err);
        }
    }
    
    public async campanhaPersonagens(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const { campanha_id } = request.params;
            const listCampanhaPersonagens = new ListCampanhaPersonagensService();
            const personagens = await listCampanhaPersonagens.execute({ campanha_id });
            return response.json(personagens);
        }catch(err){
            next(err);
        }
    }

    public async show(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const { id } = request.params
            const showPersonagem = new ShowPersonagemService();
            const personagem = await showPersonagem.execute({personagem_id: id});
            return response.json(personagem);
        }catch(err){
            next(err);
        }
    }
    public async create(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { nome, classe, raca, nivel, atributos, campanha_id } = request.body;
            const jogador_id = request.usuario.id;
            const createPersonagem = new CreatePersonagemService();
            const personagem = await createPersonagem.execute({ nome, classe, raca, nivel, atributos, jogador_id, campanha_id });
            return response.status(201).json(personagem);
        } catch (err) {
            next(err);
        }
    }
    public async update(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { id } = request.params;
            const { nome, classe, raca, nivel, atributos } = request.body;
            const usuario_id = request.usuario.id;
            const updatePersonagem = new UpdatePersonagemService();
            const personagem = await updatePersonagem.execute({personagem_id: id, usuario_id, nome, classe, raca, nivel, atributos });
            return response.json(personagem);
        } catch (err) {
            next(err);
        }
    }
        public async delete(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { id } = request.params;
            const usuario_id = request.usuario.id;
            const deletePersonagem = new DeletePersonagemService();
            await deletePersonagem.execute({ personagem_id: id, usuario_id });
            return response.status(204).json();
        } catch (err) {
            next(err);
        }
    }
}