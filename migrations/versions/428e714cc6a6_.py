"""empty message

Revision ID: 428e714cc6a6
Revises: b48fc795cefb
Create Date: 2024-01-18 11:35:27.485661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '428e714cc6a6'
down_revision = 'b48fc795cefb'
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
