import {MigrationInterface, QueryRunner, Table} from "typeorm";

export class CreateUsuarios1748531212487 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.createTable(
            new Table({
                name: 'usuarios',
                columns:[
                    {name: 'id', type: 'uuid', isPrimary: true, generationStrategy: 'uuid', default: 'uuid_generate_v4()'},
                    {name: 'nome', type: 'varchar'},
                    {name: 'email', type: 'varchar', isUnique: true},
                    {name: 'senha', type: 'varchar'},
                    {name: 'avatar', type: 'varchar', isNullable: true},
                    {name: 'descricao', type: 'text', isNullable: true},
                    {name: 'created_at', type: 'timestamp', default:'now()'},
                    {name: 'updated_at', type: 'timestamp', default:'now()'},
                ],
            })
        );
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.dropTable('usuarios')
    }
}
