"""empty message

Revision ID: e7f141bbe46c
Revises: 53b9ffc2b4d1
Create Date: 2024-01-18 11:00:26.900278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7f141bbe46c'
down_revision = '53b9ffc2b4d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exam',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(length=250), nullable=False),
    sa.Column('correct_option', sa.String(length=250), nullable=False),
    sa.Column('option_a', sa.String(length=250), nullable=False),
    sa.Column('option_b', sa.String(length=250), nullable=False),
    sa.Column('option_c', sa.String(length=250), nullable=False),
    sa.Column('option_d', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exam')
    # ### end Alembic commands ###
