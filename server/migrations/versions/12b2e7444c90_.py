"""empty message

Revision ID: 12b2e7444c90
Revises: f5eb321930be
Create Date: 2023-10-04 13:04:02.817389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12b2e7444c90'
down_revision = 'f5eb321930be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_history',
    sa.Column('product_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('product_id', 'user_id')
    )
    # ### end Alembic commands ###
