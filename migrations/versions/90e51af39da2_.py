"""empty message

Revision ID: 90e51af39da2
Revises: 7e5a736b4fd7
Create Date: 2022-05-18 22:07:12.168322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90e51af39da2'
down_revision = '7e5a736b4fd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('homeplanet_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'people', 'planets', ['homeplanet_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'people', type_='foreignkey')
    op.drop_column('people', 'homeplanet_id')
    # ### end Alembic commands ###