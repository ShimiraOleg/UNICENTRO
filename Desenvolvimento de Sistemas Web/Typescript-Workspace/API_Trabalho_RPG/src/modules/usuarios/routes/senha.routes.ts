import { Router } from "express";
import EsquecerSenhaController from "../controllers/EsquecerSenhaController";
import { celebrate, Joi, Segments } from "celebrate";
import ResetarSenhaController from "../controllers/ResetarSenhaController";

const senhaRouter = Router();
const esquecerSenhaController = new EsquecerSenhaController();
const resetarSenhaController = new ResetarSenhaController();

senhaRouter.post('/esqueceu', celebrate({
    [Segments.BODY]:{email: Joi.string().email().required()}
}), async (req, res, next)=>{
    try{
        esquecerSenhaController.create(req, res, next);
    } catch(err){
        next(err);
    }
});

senhaRouter.post('/resetar', celebrate({
    [Segments.BODY]: {
        token: Joi.string().uuid().required(),
        senha: Joi.string().required(),
        senha_confirmacao: Joi.string().required().valid(Joi.ref("senha"))
    }
}), async(req, res, next)=>{
    try{
        resetarSenhaController.create(req, res, next);
    } catch(err) {
        next(err);
    }
});

export default senhaRouter;