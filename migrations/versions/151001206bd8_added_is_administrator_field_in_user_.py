"""added is_administrator field in User model

Revision ID: 151001206bd8
Revises: 9ba665a40a12
Create Date: 2020-12-05 15:59:37.183874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151001206bd8'
down_revision = '9ba665a40a12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_administrator', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_administrator')
    # ### end Alembic commands ###
