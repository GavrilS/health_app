import flaskr as f

def main():
    app = f.create_app()

    app.run(debug=True)


if __name__=='__main__':
    main()