"""create posts table

Revision ID: f9e85b2d01d4
Revises: 
Create Date: 2021-11-14 13:16:55.003427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9e85b2d01d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True)), sa.Column("title", sa.String(), nullable=False)
    pass


def downgrade():
    op.drop_table("posts")
    pass
