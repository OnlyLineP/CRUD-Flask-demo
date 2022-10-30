"""entries table

Revision ID: 1191fd8adec8
Revises: 
Create Date: 2022-10-22 19:26:49.968395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1191fd8adec8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entry_description'), 'entry', ['description'], unique=False)
    op.create_index(op.f('ix_entry_title'), 'entry', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entry_title'), table_name='entry')
    op.drop_index(op.f('ix_entry_description'), table_name='entry')
    op.drop_table('entry')
    # ### end Alembic commands ###
