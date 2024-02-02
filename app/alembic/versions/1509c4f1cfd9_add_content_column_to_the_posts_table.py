"""add content column to the posts table

Revision ID: 1509c4f1cfd9
Revises: adc23cff3896
Create Date: 2024-02-02 12:57:20.255553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1509c4f1cfd9'
down_revision: Union[str, None] = 'adc23cff3896'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
