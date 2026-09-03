"""adiciona tipo de usuario

Revision ID: 9e4c6b1a3f72
Revises: 8d3f5b9a2e41
Create Date: 2026-09-03

"""
from alembic import op
import sqlalchemy as sa


revision = "9e4c6b1a3f72"
down_revision = "8d3f5b9a2e41"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("usuario", sa.Column("administrador", sa.Boolean(), nullable=True))
    op.execute("UPDATE usuario SET administrador = 0 WHERE administrador IS NULL")
    op.alter_column(
        "usuario",
        "administrador",
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=sa.false(),
    )


def downgrade():
    op.drop_column("usuario", "administrador")