# -*- coding: utf-8 -*-

from server import create_app

app = create_app()


def main():
    """Entrypoint for finding fires from satellite."""
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()