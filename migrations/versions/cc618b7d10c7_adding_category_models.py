"""adding Category models

Revision ID: cc618b7d10c7
Revises: 9f0571c4a355
Create Date: 2023-12-29 08:59:55.447898

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision = "cc618b7d10c7"
down_revision = "9f0571c4a355"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column(
            "grade", existing_type=mysql.VARCHAR(length=250), nullable=True
        )
        batch_op.alter_column(
            "school", existing_type=mysql.VARCHAR(length=250), nullable=True
        )
        batch_op.alter_column(
            "dob",
            existing_type=mysql.VARCHAR(length=250),
            type_=sa.DateTime(timezone=250),
            nullable=True,
        )


def downgrade():
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column(
            "dob",
            existing_type=sa.DateTime(timezone=250),
            type_=mysql.VARCHAR(length=250),
            nullable=False,
        )
        batch_op.alter_column(
            "school", existing_type=mysql.VARCHAR(length=250), nullable=False
        )
        batch_op.alter_column(
            "grade", existing_type=mysql.VARCHAR(length=250), nullable=False
        )

    op.drop_table("category")
