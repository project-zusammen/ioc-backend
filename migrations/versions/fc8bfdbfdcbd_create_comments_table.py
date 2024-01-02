"""create comments table

Revision ID: fc8bfdbfdcbd
Revises: cc618b7d10c7
Create Date: 2024-01-01 13:48:02.344464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8bfdbfdcbd'
down_revision = 'cc618b7d10c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('replyTo', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_comments_id'), ['id'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_comments_id'))

    op.drop_table('comments')
    # ### end Alembic commands ###
