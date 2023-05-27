import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        port=int(os.environ.get('PORT')),
        host=os.environ.get('IP'),
        debug=os.environ.get('DEBUG')
    )
