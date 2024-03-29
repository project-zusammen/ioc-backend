"""adding relation between answer and exam

Revision ID: ef748a9dcc8e
Revises: 66502c5e114e
Create Date: 2024-02-09 20:20:11.956372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef748a9dcc8e'
down_revision = '66502c5e114e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('exam_id', sa.BigInteger(), nullable=False))
        batch_op.create_foreign_key(None, 'exam', ['exam_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('exam_id')

    # ### end Alembic commands ###
