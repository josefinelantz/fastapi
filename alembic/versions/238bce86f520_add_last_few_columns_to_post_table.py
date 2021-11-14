"""add last few columns to post table

Revision ID: 238bce86f520
Revises: 66aa55313fb7
Create Date: 2021-11-14 13:40:13.408098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '238bce86f520'
down_revision = '66aa55313fb7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass