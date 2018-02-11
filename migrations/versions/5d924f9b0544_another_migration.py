"""another Migration

Revision ID: 5d924f9b0544
Revises: 333bd3ff96a3
Create Date: 2018-02-10 13:01:44.594154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d924f9b0544'
down_revision = '333bd3ff96a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('votes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'votes')
    # ### end Alembic commands ###
