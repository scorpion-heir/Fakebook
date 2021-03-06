"""empty message

Revision ID: 0c106ac67243
Revises: 4afbce0221b6
Create Date: 2021-03-29 10:34:12.208423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c106ac67243'
down_revision = '4afbce0221b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_id_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_id_key', 'user', ['id'])
    # ### end Alembic commands ###
