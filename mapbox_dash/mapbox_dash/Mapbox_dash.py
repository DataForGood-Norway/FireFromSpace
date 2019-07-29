# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Mapbox_dash(Component):
    """A Mapbox_dash component.


Keyword arguments:
- id (string; optional)
- mouse_position (dict; optional): mouse_position has the following type: dict containing keys 'x_prop', 'y_prop'.
Those keys have the following types:
  - x_prop (number; optional)
  - y_prop (number; optional)
- viewport (dict; default {width: 800,
      height: 800,
      latitude: 37.7577,
      longitude: -122.4376,
      zoom: 8}): viewport has the following type: dict containing keys 'width', 'height', 'latitude', 'longitude', 'zoom'.
Those keys have the following types:
  - width (number; optional)
  - height (number; optional)
  - latitude (number; optional)
  - longitude (number; optional)
  - zoom (number; optional)
- MAPBOX_TOKEN (string; default "pk.eyJ1IjoiYWxpc2hvYmVpcmkiLCJhIjoiY2ozYnM3YTUxMDAxeDMzcGNjbmZyMmplZiJ9.ZjmQ0C2MNs1AzEBC_Syadg")"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, mouse_position=Component.UNDEFINED, viewport=Component.UNDEFINED, MAPBOX_TOKEN=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'mouse_position', 'viewport', 'MAPBOX_TOKEN']
        self._type = 'Mapbox_dash'
        self._namespace = 'mapbox_dash'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'mouse_position', 'viewport', 'MAPBOX_TOKEN']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Mapbox_dash, self).__init__(**args)
