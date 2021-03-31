"""changed id to uuid in User

Revision ID: 1bae5acfb326
Revises: fbda4a6a296e
Create Date: 2021-03-28 22:48:25.327872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bae5acfb326'
down_revision = 'fbda4a6a296e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###