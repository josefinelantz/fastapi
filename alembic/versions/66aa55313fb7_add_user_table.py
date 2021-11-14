"""add user table

Revision ID: 66aa55313fb7
Revises: 796653ed1865
Create Date: 2021-11-14 13:36:04.025967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66aa55313fb7'
down_revision = '796653ed1865'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer(), nullable=False), sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
    server_default=sa.text("now()"), nullable=False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email"))
    pass

def downgrade():
    op.drop_table("users")
    pass