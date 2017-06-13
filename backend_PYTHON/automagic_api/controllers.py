from automagic_api import app, s, manager
from automagic_api.models\
    import Book, Author



def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Credentials']='true'
    response.headers['Access-Control-Allow-Headers']='Content-Type'
    return response


author_api_blueprint = manager.create_api_blueprint(Author,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])
book_api_blueprint = manager.create_api_blueprint(Book,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])

author_api_blueprint.after_request(add_cors_headers)
book_api_blueprint.after_request(add_cors_headers)
