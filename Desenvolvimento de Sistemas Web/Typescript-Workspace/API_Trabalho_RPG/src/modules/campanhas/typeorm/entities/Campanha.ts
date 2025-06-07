import { Column, CreateDateColumn, Entity, PrimaryGeneratedColumn, UpdateDateColumn } from "typeorm";

@Entity('campanhas')
export default class Campanha{
        @PrimaryGeneratedColumn('uuid')
        id: string;
        @Column()
        nome: string;
        @Column()
        descricao?: string;
        @Column()
        sistema_rpg: string;
        @Column('int')
        nivel_max: number;
        @Column()
        status: string;
        @Column()
        mestre_id: string;
        @CreateDateColumn()
        created_at: Date;
        @UpdateDateColumn()
        updated_at: Date;
}