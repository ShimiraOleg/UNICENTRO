import {MigrationInterface, QueryRunner, Table} from "typeorm";

export class CreateCampanhas1749271301970 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.createTable(
            new Table({
                name: 'campanhas',
                columns:[
                    {name: 'id', type: 'uuid', isPrimary: true, generationStrategy: 'uuid', default: 'uuid_generate_v4()'},
                    {name: 'nome', type: 'varchar'},
                    {name: 'descricao', type: 'text', isNullable: true},
                    {name: 'sistema_rpg', type: 'varchar'},
                    {name: 'nivel_max', type: 'int'},
                    {name: 'status', type: 'varchar'},
                    {name: 'mestre_id', type: 'uuid'},
                    {name: 'created_at', type: 'timestamp', default:'now()'},
                    {name: 'updated_at', type: 'timestamp', default:'now()'},
                ],
                foreignKeys:[
                    {
                    name:'CampanhaUsuario',
                    referencedTableName: 'usuarios',
                    referencedColumnNames: ['id'],
                    columnNames: ['mestre_id'],
                    onDelete: 'CASCADE',
                    onUpdate: 'CASCADE',
                }
                ]
            })
        );
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.dropTable('campanhas');
    }

}
