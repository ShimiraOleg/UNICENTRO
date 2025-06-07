import { Router } from "express";
import PerfilController from "../controllers/PerfilController";
import isAuthenticadted from "@shared/http/middlewares/isAuthenticated";
import { celebrate, Joi, Segments } from "celebrate";


const perfilRouter = Router();
const perfilController = new PerfilController();
perfilRouter.use(isAuthenticadted);

perfilRouter.get('/', async(req, res, next)=>{
    try{
        await perfilController.show(req, res, next);
    }catch(err){
        next(err);
    }
});

perfilRouter.put('/', celebrate({
    [Segments.BODY]:{
        nome: Joi.string().required(),
        email: Joi.string().email().required(),
        senha_antiga: Joi.string(),
        senha: Joi.string().min(6).optional(),
        confirmacao_senha: Joi.string().valid(Joi.ref('senha')).when('senha', {is: Joi.exist(), then: Joi.required()}),
        descricao: Joi.string().optional()
    }
}), async(req, res, next) =>{
    try{
        await perfilController.update(req, res, next);
    }catch(err){
        next(err);
    }
});

export default perfilRouter;