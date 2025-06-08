import { Column, CreateDateColumn, Entity, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";

@Entity('personagens')
export default class Personagem{
    @PrimaryGeneratedColumn('uuid')
    id: string;
    @Column()
    nome: string;
    @Column()
    classe: string;
    @Column()
    raca: string;
    @Column('int')
    nivel: number;
    @Column('json')
    atributos: object;
    @Column()
    jogador_id: string;
    @Column()
    campanha_id: string;
    @CreateDateColumn()
    created_at: Date;
    @UpdateDateColumn()
    updated_at: Date;
}