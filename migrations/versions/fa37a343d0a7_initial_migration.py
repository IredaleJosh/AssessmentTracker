"""Initial migration

Revision ID: fa37a343d0a7
Revises: 
Create Date: 2024-10-25 10:38:12.630490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa37a343d0a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('module_code', sa.String(length=8), nullable=True),
    sa.Column('assess_title', sa.String(length=15), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('progress', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assessments')
    # ### end Alembic commands ###
