import campanhasRouter from "@modules/campanhas/routes/campanha.routes";
import perfilRouter from "@modules/usuarios/routes/perfil.routes";
import senhaRouter from "@modules/usuarios/routes/senha.routes";
import sessionsRouter from "@modules/usuarios/routes/sessions.routes";
import usuariosRouter from "@modules/usuarios/routes/usuarios.routes";
import { Router } from "express";

const routes = Router();
routes.use('/usuarios', usuariosRouter);
routes.use('/sessions', sessionsRouter);
routes.use('/senha', senhaRouter);
routes.use('/perfil', perfilRouter);
routes.use('/campanhas', campanhasRouter)

export default routes;