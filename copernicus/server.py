# -*- coding: utf-8 -*-

"""
A Flask app to trigger some image processing from a webapp.
"""

from flask import Flask, jsonify
from pathlib import Path
from processing.satellite_image import MonitoredRegion


def create_app():
    """Create app-server to trigger application from an api."""
    # app initiliazation
    app = Flask(__name__)

    # initialize app
    path_to_images = Path(".")
    region = MonitoredRegion(path_to_images)

    @app.route('/')
    def locate_fire():
        fires = region.image.locate_fire_from_image()

        response = {
            'fires_detected': fires,
            'status': 'ok'
        }
        return jsonify(response)


    return app
