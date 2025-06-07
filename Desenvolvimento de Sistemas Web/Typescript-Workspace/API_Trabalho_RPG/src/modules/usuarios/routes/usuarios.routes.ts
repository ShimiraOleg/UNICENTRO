import { Router } from "express";
import UsuariosController from "../controllers/UsuariosController";
import { celebrate, Joi, Segments } from "celebrate";
import isAuthenticated from "../../../shared/http/middlewares/isAuthenticated";
import multer from 'multer';
import uploadConfig from '@config/upload';
import UsuarioAvatarController from "../controllers/UsuarioAvatarController";

const usuariosRouter = Router();
const usuariosController = new UsuariosController();
const usuarioAvatarController = new UsuarioAvatarController();
const upload = multer(uploadConfig)

usuariosRouter.get('/', isAuthenticated, async (req, res, next) =>{
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

usuariosRouter.patch('/avatar', isAuthenticated, upload.single('avatar'), async (req, res, next) =>{
    try{
        await usuarioAvatarController.update(req, res, next);
    }catch(err){
        next(err);
    }
})

export default usuariosRouter