"""empty message

Revision ID: 3755a8869094
Revises: 058d0922aeb7
Create Date: 2024-01-18 11:45:36.110117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3755a8869094'
down_revision = '058d0922aeb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('material', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'category', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('material', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
