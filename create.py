
from models import *

from app import *
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ckpmkviyipnrkv:638918855a3518e0de25e8567a139a277cf066fc368f1ad5c57d08fa2f1ebdf9@ec2-44-194-112-166.compute-1.amazonaws.com:5432/dnjsmsrhl5qqm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()
