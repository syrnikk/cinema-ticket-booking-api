"""Fix nullable fields

Revision ID: fea0862084db
Revises: 1766e39adf1c
Create Date: 2023-06-15 22:16:37.696545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fea0862084db'
down_revision = '1766e39adf1c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('repertoire', 'cinema_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('repertoire', 'movie_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('repertoire', 'movie_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('repertoire', 'cinema_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###