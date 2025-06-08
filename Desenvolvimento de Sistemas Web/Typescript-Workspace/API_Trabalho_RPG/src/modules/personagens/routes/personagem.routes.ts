import { Router } from "express";
import PersonagensController from "../controllers/PersonagensController";
import { celebrate, Joi, Segments } from "celebrate";
import isAuthenticated from "@shared/http/middlewares/isAuthenticated";

const personagensRouter = Router();
const personagensController = new PersonagensController();

personagensRouter.get('/', async (req, res, next) => {
    try {
        await personagensController.index(req, res, next);
    } catch (err) {
        next(err);
    }
});
personagensRouter.get('/meus', isAuthenticated, async (req, res, next) => {
    try {
        await personagensController.usuarioPersonagens(req, res, next);
    } catch (err) {
        next(err);
    }
});
personagensRouter.get('/campanha/:campanha_id', celebrate({
    [Segments.PARAMS]: {
        campanha_id: Joi.string().uuid().required()
    }
}), async (req, res, next) => {
    try {
        await personagensController.campanhaPersonagens(req, res, next);
    } catch (err) {
        next(err);
    }
});
personagensRouter.get('/:id', celebrate({
    [Segments.PARAMS]: {
        id: Joi.string().uuid().required()
    }
}), async (req, res, next) => {
    try {
        await personagensController.show(req, res, next);
    } catch (err) {
        next(err);
    }
});
personagensRouter.post('/', isAuthenticated, celebrate({
    [Segments.BODY]: {
        nome: Joi.string().required(),
        classe: Joi.string().required(),
        raca: Joi.string().required(),
        nivel: Joi.number().integer().min(1).required(),
        atributos: Joi.object().required(),
        campanha_id: Joi.string().uuid().required()
    }
}), async (req, res, next) => {
    try {
        await personagensController.create(req, res, next);
    } catch (err) {
        next(err);
    }
});
personagensRouter.put('/:id', isAuthenticated, celebrate({
    [Segments.PARAMS]: {
        id: Joi.string().uuid().required()
    },
    [Segments.BODY]: {
        nome: Joi.string().optional(),
        classe: Joi.string().optional(),
        raca: Joi.string().optional(),
        nivel: Joi.number().integer().min(1).optional(),
        atributos: Joi.object().optional()
    }
}), async (req, res, next) => {
    try {
        await personagensController.update(req, res, next);
    } catch (err) {
        next(err);
    }
});

personagensRouter.delete('/:id', isAuthenticated, celebrate({
    [Segments.PARAMS]: {
        id: Joi.string().uuid().required()
    }
}), async (req, res, next) => {
    try {
        await personagensController.delete(req, res, next);
    } catch (err) {
        next(err);
    }
});

export default personagensRouter;