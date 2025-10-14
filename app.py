import flaskr as f
from flaskr.database.operation_manager import OperationManager

def main():
    app = f.create_app()
    db_manager = OperationManager()

    app.run(debug=True)


if __name__=='__main__':
    main()