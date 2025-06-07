import { Column, CreateDateColumn, Entity, Generated, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";

@Entity('usuario_tokens')
export default class UsuarioToken{
    @PrimaryGeneratedColumn('uuid')
    id: string;
    @Column()
    @Generated('uuid')
    token: string;
    @Column()
    usuario_id: string;
    @CreateDateColumn()
    created_at: Date;
    @UpdateDateColumn()
    updated_at: Date;
}