"""adiciona imagem a pizza

Revision ID: 8d3f5b9a2e41
Revises: 7c2f4a8e1d90
Create Date: 2026-09-03

"""
from alembic import op
import sqlalchemy as sa


revision = "8d3f5b9a2e41"
down_revision = "7c2f4a8e1d90"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("pizza", sa.Column("imagem", sa.String(length=500), nullable=True))


def downgrade():
    op.drop_column("pizza", "imagem")