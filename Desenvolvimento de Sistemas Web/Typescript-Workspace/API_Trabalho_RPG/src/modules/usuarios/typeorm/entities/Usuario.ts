import { Column, CreateDateColumn, Entity, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";

@Entity('usuarios')
export default class Usuario{
    @PrimaryGeneratedColumn('uuid')
    id: string;
    @Column()
    nome: string;
    @Column()
    email: string;
    @Column()
    senha: string;
    @Column()
    avatar?: string;
    @Column()
    descricao?: string;
    @CreateDateColumn()
    created_at: Date;
    @UpdateDateColumn()
    updated_at: Date;
}