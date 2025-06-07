import { getCustomRepository } from "typeorm";
import UsuariosRepository from "../typeorm/repositories/UsuariosRepository";
import UsuarioTokensRepository from "../typeorm/repositories/UsuarioTokensRepository";
import AppError from "@shared/errors/AppError";
import EtherealMail from "@config/mail/EtherealMail";
import path from "path";

interface IRequest{
    email: string;
}

export default class SendSenhaEsquecidaEmailService{
    public async execute({email}: IRequest): Promise<void>{
        const usuariosRepository = getCustomRepository(UsuariosRepository);
        const usuariosTokensRepository = getCustomRepository(UsuarioTokensRepository);
        const senhaEsquecidaTemplate = path.resolve(__dirname, '..', 'views', 'esqueceu_senha.hbs');
        const usuario = await usuariosRepository.findByEmail(email);
        if(!usuario){
            throw new AppError('O usuário não existe.')
        }
        const {token} = await usuariosTokensRepository.generate(usuario.id);
        console.log(token);
        await EtherealMail.sendMail({
            to: {name: usuario.nome, email: usuario.email},
            subject: '[API RPG] Recuperação de Senha',
            templateData: {
                file: senhaEsquecidaTemplate,
                variables: {
                    name: usuario.nome,
                    link: `http://localhost:3000/reset_password?token=${token}`
                },
            },
        });
    }
}