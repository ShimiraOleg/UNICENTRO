import {MigrationInterface, QueryRunner, Table} from "typeorm";

export class CreatePersonagens1749392902987 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.createTable(
            new Table({
                name: 'personagens',
                columns:[
                    {name: 'id', type: 'uuid', isPrimary: true, generationStrategy: 'uuid', default: 'uuid_generate_v4()'},
                    {name: 'nome', type: 'varchar'},
                    {name: 'classe', type: 'varchar'},
                    {name: 'raca', type: 'varchar'},
                    {name: 'nivel', type: 'int'},
                    {name: 'atributos', type: 'json'},
                    {name: 'jogador_id', type: 'uuid'},
                    {name: 'campanha_id', type: 'uuid'},
                    {name: 'created_at', type: 'timestamp', default:'now()'},
                    {name: 'updated_at', type: 'timestamp', default:'now()'},
                ],
                foreignKeys:[
                    {
                        name:'PersonagemJogador',
                        referencedTableName: 'usuarios',
                        referencedColumnNames: ['id'],
                        columnNames: ['jogador_id'],
                        onDelete: 'CASCADE',
                        onUpdate: 'CASCADE',
                    },
                    {
                        name:'PersonagemCampanha',
                        referencedTableName: 'campanhas',
                        referencedColumnNames: ['id'],
                        columnNames: ['campanha_id'],
                        onDelete: 'CASCADE',
                        onUpdate: 'CASCADE',
                    }
                ]
            })
        );
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.dropTable('personagens')
    }

}
