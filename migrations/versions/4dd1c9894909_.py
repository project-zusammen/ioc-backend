"""empty message

Revision ID: 4dd1c9894909
Revises: fafaacac33c1
Create Date: 2024-01-18 01:43:01.975145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4dd1c9894909'
down_revision = 'fafaacac33c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matery', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.BigInteger(), nullable=False))
        batch_op.add_column(sa.Column('category_id', sa.BigInteger(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'category', ['category_id'], ['id'])
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matery', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', mysql.VARCHAR(length=250), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')
        batch_op.drop_column('user_id')
        batch_op.drop_column('content')
        batch_op.drop_column('title')

    # ### end Alembic commands ###
