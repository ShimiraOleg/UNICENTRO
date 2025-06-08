import Campanha from "@modules/campanhas/typeorm/entities/Campanha";
import Usuario from "@modules/usuarios/typeorm/entities/Usuario";
import { Column, CreateDateColumn, Entity, JoinColumn, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";

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
    @ManyToOne(() => Usuario)
    @JoinColumn({name : 'jogador_id'})
    jogador: Usuario;
    @ManyToOne(() => Campanha)
    @JoinColumn({name : 'campanha_id'})
    campanha: Campanha;
    @CreateDateColumn()
    created_at: Date;
    @UpdateDateColumn()
    updated_at: Date;
}