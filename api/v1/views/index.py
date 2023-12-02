#!/usr/bin/python3
"""Prints a JSON response"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status_check():
    """Returns API status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def object_stats():
    """Retrieves the number of each object by type"""
    stats = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User'),
            }
    return jsonify(stats)
