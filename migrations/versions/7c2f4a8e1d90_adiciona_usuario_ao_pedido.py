"""adiciona usuario ao pedido

Revision ID: 7c2f4a8e1d90
Revises: 39e46cf72b89
Create Date: 2026-09-03

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7c2f4a8e1d90"
down_revision = "39e46cf72b89"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("pedido", sa.Column("usuario_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "fk_pedido_usuario_id",
        "pedido",
        "usuario",
        ["usuario_id"],
        ["id"],
    )


def downgrade():
    op.drop_constraint("fk_pedido_usuario_id", "pedido", type_="foreignkey")
    op.drop_column("pedido", "usuario_id")
