# -*- coding: utf-8 -*-

import sys
import os

from server import create_app

app = create_app()


def main():
    """Entrypoint for finding fires from satellite."""
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
