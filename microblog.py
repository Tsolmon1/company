from app import create_app, db, cli
from app.models import Company_list

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Company_list': Company_list}
