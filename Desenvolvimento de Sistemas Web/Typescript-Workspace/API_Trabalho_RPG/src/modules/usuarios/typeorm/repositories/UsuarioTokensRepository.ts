import { EntityRepository, Repository } from "typeorm";
import UsuarioToken from "../entities/UsuarioToken";

@EntityRepository(UsuarioToken)
export default class UsuarioTokensRepository extends Repository<UsuarioToken>{
    public async findByToken(token: string): Promise<UsuarioToken | undefined>{
        const usuarioToken = await this.findOne({
            where: {
                token,
            },
        });
        return usuarioToken;
    }

    public async generate(usuario_id: string): Promise<UsuarioToken>{
        const usuarioToken = await this.create({
            usuario_id,
        });
        await this.save(usuarioToken);
        return usuarioToken;
    }
}