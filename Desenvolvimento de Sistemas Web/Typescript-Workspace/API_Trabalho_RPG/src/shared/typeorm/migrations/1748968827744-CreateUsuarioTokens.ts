import {MigrationInterface, QueryRunner, Table} from "typeorm";

export class CreateUsuarioTokens1748968827744 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.createTable(
            new Table({
                name: 'usuario_tokens',
                columns:[
                    {name:'id', type: 'uuid', isPrimary: true, generationStrategy: 'uuid', default: 'uuid_generate_v4()'},
                    {name:'token', type: 'uuid', generationStrategy: 'uuid', default: 'uuid_generate_v4()'},
                    {name: 'usuario_id', type:'uuid'},
                    {name: 'created_at', type: 'timestamp', default:'now()'},
                    {name: 'updated_at', type: 'timestamp', default:'now()'},
                ],
                foreignKeys:[
                    {
                    name:'TokenUsuario',
                    referencedTableName: 'usuarios',
                    referencedColumnNames: ['id'],
                    columnNames: ['usuario_id'],
                    onDelete: 'CASCADE',
                    onUpdate: 'CASCADE',
                }
                ]
            })
        )
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.dropTable('usuario_tokens')
    }

}
