import sessionsRouter from "@modules/usuarios/routes/sessions.routes";
import usuariosRouter from "@modules/usuarios/routes/usuarios.routes";
import { Router } from "express";

const routes = Router();
routes.use('/usuarios', usuariosRouter);
routes.use('/sessions', sessionsRouter);

export default routes;