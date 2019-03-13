# -*- coding: utf-8 -*-

"""
A Flask app to trigger some image processing from a webapp.
"""

from flask import Flask, jsonify

from processing.image_processing import ImageProcess


def create_app():
    """Create app-server to trigger application from an api."""
    # app initiliazation
    app = Flask(__name__)

    # initialize app
    path_to_images = ""
    process = ImageProcess(path_to_images)

    @app.route('/locate_fire')
    def locate_fire():
        fires = process.locate_fire_from_image(path_to_images)
        response = {
            'statuses': statuses,
            'status': 'ok'
        }
        return jsonify(response)

    @app.route('/xmts_statuses')
    def test_persist():
        statuses = xmts_statuses.get_statuses()
        xmts_statuses.persist_statuses(statuses)
        response = {
            'statuses': statuses,
            'status': 'ok'
        }
        return jsonify(response)

    return app
