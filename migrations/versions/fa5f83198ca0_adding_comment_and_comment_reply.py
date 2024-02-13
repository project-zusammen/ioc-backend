"""Adding comment and comment reply

Revision ID: fa5f83198ca0
Revises: 1c3debcde2bc
Create Date: 2024-02-12 17:06:59.786743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa5f83198ca0'
down_revision = '1c3debcde2bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.Text(), nullable=False))
        batch_op.drop_column('text')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', mysql.TEXT(), nullable=False))
        batch_op.drop_column('comment')

    # ### end Alembic commands ###