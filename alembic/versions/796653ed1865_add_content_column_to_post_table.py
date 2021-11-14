"""add content column to post table

Revision ID: 796653ed1865
Revises: f9e85b2d01d4
Create Date: 2021-11-14 13:31:46.658639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '796653ed1865'
down_revision = 'f9e85b2d01d4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
