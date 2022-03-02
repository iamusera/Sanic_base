from app import creat_app


if __name__ == '__main__':
    app = creat_app()
    app.run(host=app.config.get('HOST', '0.0.0.0'),
            port=app.config.get('PORT', 8090),
            access_log=True,
            debug=True)