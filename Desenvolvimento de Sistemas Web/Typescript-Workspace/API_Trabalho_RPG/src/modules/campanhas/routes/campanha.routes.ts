import { Router } from "express";
import CampanhasController from "../controllers/CampanhasController";
import isAuthenticated from "@shared/http/middlewares/isAuthenticated";
import { celebrate, Joi, Segments } from "celebrate";

const campanhasRouter = Router();
const campanhasController = new CampanhasController();

campanhasRouter.get('/', async (req, res, next) =>{
    try{
        await campanhasController.index(req, res, next);
    }catch(err){
        next(err);
    }
});

campanhasRouter.get('/minhas', isAuthenticated, async (req, res, next) =>{
    try{
        await campanhasController.UsuarioCampanhas(req, res, next);
    }catch(err){
        next(err);
    }
});

campanhasRouter.get('/:id', celebrate({
    [Segments.PARAMS]:{
        id: Joi.string().uuid().required()
    }
}), async (req, res, next) => {
    try{
        await campanhasController.show(req, res, next);
    }catch(err){
        next(err);
    }
})

campanhasRouter.post('/', isAuthenticated, celebrate({
    [Segments.BODY]: {
        nome: Joi.string().required(),
        descricao: Joi.string().optional(),
        sistema_rpg: Joi.string().required(),
        nivel_max: Joi.number().integer().min(1).required(),
        status: Joi.string().valid('ativa', 'pausada', 'concluida', 'cancelada').required()
    }
}), async (req, res, next) =>{
    try{
        await campanhasController.create(req, res, next);
    }catch(err){
        next(err);
    }
});

campanhasRouter.put('/:id', isAuthenticated, celebrate({
    [Segments.PARAMS]: {
        id: Joi.string().uuid().required()
    },
    [Segments.BODY]: {
        nome: Joi.string().optional(),
        descricao: Joi.string().optional(),
        sistema_rpg: Joi.string().optional(),
        nivel_max: Joi.number().integer().min(1).optional(),
        status: Joi.string().valid('ativa', 'pausada', 'concluida', 'cancelada').optional()
    }
}), async (req, res, next) => {
    try {
        await campanhasController.update(req, res, next);
    } catch (err) {
        next(err);
    }
});

campanhasRouter.delete('/:id', isAuthenticated, celebrate({
    [Segments.PARAMS]: {
        id: Joi.string().uuid().required()
    }
}), async (req, res, next) => {
    try {
        await campanhasController.delete(req, res, next);
    } catch (err) {
        next(err);
    }
});

export default campanhasRouter;