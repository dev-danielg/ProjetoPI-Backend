from repositories import UsuarioRepository
from controllers import UsuarioController
from services import UsuarioService
from flask import Blueprint
from extensions import db


bp = Blueprint("usuario", __name__, url_prefix="/api/usuarios")


@bp.route("", methods=["POST"])
def cadastrar():
    repository = UsuarioRepository(db.session)
    service = UsuarioService(repository)
    controller = UsuarioController(repository, service)
    return controller.cadastrar()


@bp.route("", methods=["GET"])
def buscar_todos():
    repository = UsuarioRepository(db.session)
    service = UsuarioService(repository)
    controller = UsuarioController(repository, service)
    return controller.buscar_todos()


@bp.route("/<int:id_usuario>", methods=["UPDATE"])
def atualizar(id_usuario):
    repository = UsuarioRepository(db.session)
    service = UsuarioService(repository)
    controller = UsuarioController(repository, service)
    return controller.atualizar(id_usuario)


@bp.route("/<int:id_usuario>", methods=["DELETE"])
def deletar(id_usuario):
    repository = UsuarioRepository(db.session)
    service = UsuarioService(repository)
    controller = UsuarioController(repository, service)
    return controller.deletar(id_usuario)


