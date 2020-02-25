from application import init_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
app = init_app("dev")

manager = Manager(app)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()