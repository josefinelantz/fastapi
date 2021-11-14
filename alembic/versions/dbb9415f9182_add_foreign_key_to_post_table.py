"""add foreign key to post table

Revision ID: dbb9415f9182
Revises: 238bce86f520
Create Date: 2021-11-14 13:46:46.509154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbb9415f9182'
down_revision = '238bce86f520'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users",local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass

def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
