import { NextFunction, Request, Response } from "express";
import ListCampanhaService from "../services/ListCampanhaService";
import ListUsuarioCampanhasService from "../services/ListUsuarioCampanhasService";
import ShowCampanhaService from "../services/ShowCampanhaService";
import CreateCampanhaService from "../services/CreateCampanhaService";
import UpdateCampanhaService from "../services/UpdateCampanhaService";
import DeleteCampanhaService from "../services/DeleteCampanhaService";

export default class CampanhasController{
    public async index(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const listCampanhas = new ListCampanhaService();
            const campanhas = await listCampanhas.execute();
            return response.json(campanhas);
        }catch(err){
            next(err);
        }
    }

    public async usuarioCampanhas(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const mestre_id = request.usuario.id
            const listUsuarioCampanhas = new ListUsuarioCampanhasService();
            const campanhas = await listUsuarioCampanhas.execute({ mestre_id });
            return response.json(campanhas);
        }catch(err){
            next(err);
        }
    }

    public async show(request: Request, response: Response, next: NextFunction): Promise<Response | void>{
        try{
            const { id } = request.params
            const showCampanha = new ShowCampanhaService();
            const campanhas = await showCampanha.execute({id});
            return response.json(campanhas);
        }catch(err){
            next(err);
        }
    }
    public async create(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { nome, descricao, sistema_rpg, nivel_max, status } = request.body;
            const mestre_id = request.usuario.id;
            const createCampanha = new CreateCampanhaService();
            const campanha = await createCampanha.execute({ nome, descricao, sistema_rpg, nivel_max, status, mestre_id });
            return response.status(201).json(campanha);
        } catch (err) {
            next(err);
        }
    }
    public async update(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { id } = request.params;
            const { nome, descricao, sistema_rpg, nivel_max, status } = request.body;
            const mestre_id = request.usuario.id;
            const updateCampanha = new UpdateCampanhaService();
            const campanha = await updateCampanha.execute({campanha_id: id, nome, descricao, sistema_rpg, nivel_max, status, mestre_id });
            return response.json(campanha);
        } catch (err) {
            next(err);
        }
    }
        public async delete(request: Request, response: Response, next: NextFunction): Promise<Response | void> {
        try {
            const { id } = request.params;
            const mestre_id = request.usuario.id;
            const deleteCampanha = new DeleteCampanhaService();
            await deleteCampanha.execute({ campanha_id: id, mestre_id });
            return response.status(204).json();
        } catch (err) {
            next(err);
        }
    }
}