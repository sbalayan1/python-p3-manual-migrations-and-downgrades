"""change name column to rename

Revision ID: 0fe787703cb4
Revises: 791279dd0760
Create Date: 2023-01-21 14:14:53.920598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fe787703cb4'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    op.alter_column('students', 'name', new_column_name='rename')


def downgrade() -> None:
    pass
    op.alter_column('students', 'rename', new_column_name='name')
