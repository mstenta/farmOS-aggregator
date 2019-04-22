"""Add Farms model

Revision ID: 34e07bbcbf71
Revises: e6ae69e9dcb9
Create Date: 2019-04-14 03:08:42.646150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34e07bbcbf71'
down_revision = 'e6ae69e9dcb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('farm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('farm_name', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('is_authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_farm_farm_name'), 'farm', ['farm_name'], unique=False)
    op.create_index(op.f('ix_farm_id'), 'farm', ['id'], unique=False)
    op.create_index(op.f('ix_farm_is_authenticated'), 'farm', ['is_authenticated'], unique=False)
    op.create_index(op.f('ix_farm_password'), 'farm', ['password'], unique=False)
    op.create_index(op.f('ix_farm_url'), 'farm', ['url'], unique=False)
    op.create_index(op.f('ix_farm_username'), 'farm', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_farm_username'), table_name='farm')
    op.drop_index(op.f('ix_farm_url'), table_name='farm')
    op.drop_index(op.f('ix_farm_password'), table_name='farm')
    op.drop_index(op.f('ix_farm_is_authenticated'), table_name='farm')
    op.drop_index(op.f('ix_farm_id'), table_name='farm')
    op.drop_index(op.f('ix_farm_farm_name'), table_name='farm')
    op.drop_table('farm')
    # ### end Alembic commands ###