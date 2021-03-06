"""add new column for user activate

Revision ID: e7a7488a2b55
Revises: bb92ce39cd49
Create Date: 2020-11-07 14:32:19.654231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7a7488a2b55'
down_revision = 'bb92ce39cd49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_activated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_activated')
    # ### end Alembic commands ###
