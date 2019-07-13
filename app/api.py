from os.path import dirname, join
from logging import INFO, StreamHandler, FileHandler, getLogger, Formatter
from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required
from markdown import markdown
from .utils.serpro import serpro_response


bp_api = Blueprint('cpf_authentication', __name__)
api = Api(bp_api)


def generate_log(cpf: str, serpro_raw: str, status_code: int, file: bool):
    """function to generate logs for requests."""
    log_name = 'cpf_authentication.log'
    formatter = Formatter((f'%(asctime)s - CPF: {cpf} '
                           f'- RAW: {serpro_raw} '
                           f'- STATUS: {status_code}'))
    logger = getLogger()

    def _file_handler():
        """function to generate file handler"""
        file_handler = FileHandler(log_name)
        file_handler.setLevel(INFO)
        file_handler.setFormatter(formatter)
        return file_handler


    def _console_handler():
        """function to generate console handler"""
        console_handler = StreamHandler()
        console_handler.setLevel(INFO)
        console_handler.setFormatter(formatter)
        return console_handler

    logger.addHandler(_file_handler()) if file else None
    logger.addHandler(_console_handler())
    logger.info('')


@bp_api.route("/")
@bp_api.route("/docs")
@bp_api.route("/documentation")
def index():
    """Present some documentation."""

    readme_file = join(dirname(bp_api.root_path), 'README.md')

    with open(readme_file, 'r') as markdown_file:
        content = markdown_file.read()
        return markdown(content)


class SituationCPF(Resource):
    @jwt_required
    def get(self, cpf: str):
        """get method to get the cadastral status of the cpf."""
        response, status_code = serpro_response(cpf)

        if status_code == 200:
            status = response['situacao']['descricao']
            result = {'status': status}
            return jsonify(result)

        generate_log(cpf, response, status_code, True)
        return jsonify({'error': {'reason': response}})

api.add_resource(SituationCPF, '/consult/<string:cpf>')
