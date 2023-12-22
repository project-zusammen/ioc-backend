"""Initial migration.

Revision ID: 2718c8b61eba
Revises: 
Create Date: 2023-12-22 10:50:49.421850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2718c8b61eba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###