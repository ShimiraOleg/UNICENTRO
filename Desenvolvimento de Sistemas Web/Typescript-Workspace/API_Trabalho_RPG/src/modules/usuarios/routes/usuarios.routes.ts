import { Router } from "express";
import UsuariosController from "../controllers/UsuariosController";
import { celebrate, Joi, Segments } from "celebrate";
import isAuthenticadted from "../../../shared/http/middlewares/isAuthenticated";

const usuariosRouter = Router();
const usuariosController = new UsuariosController();

usuariosRouter.get('/', isAuthenticadted, async (req, res, next) =>{
    try{
        await usuariosController.index(req, res, next)
    }catch(err){
        next(err);
    }
});

usuariosRouter.post('/', celebrate({
    [Segments.BODY]:{
        nome: Joi.string().required(),
        email:Joi.string().email().required(),
        senha: Joi.string().required(),
        descricao: Joi.string()
    }
}), async (req, res, next) => {
    try{
        await usuariosController.create(req, res, next);
    } catch(err){
        next(err);
    }
});

export default usuariosRouter