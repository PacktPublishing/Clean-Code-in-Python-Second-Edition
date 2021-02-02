**Errata and Improvements**
========================================
If you find any mistakes in the [Clean-Code-in-Python-Second-Edition](https://www.packtpub.com/product/clean-code-in-python-second-edition/9781800560215), or if you have suggestions for improvements, then please raise an issue in this repository.

## Page 47 - Fix coordinates example to accept float

The `setter` methods for `latitude` and `longitude` are changed to accept floating values for coordinates in the `properties.py` file in `ch02` directory.

The `latitude.setter` method is changed to:
```python
    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if -90 <= lat_value <= 90:
            self._latitude = lat_value
        else:
            raise ValueError(f"{lat_value} is an invalid value for latitude")
```
The `longitude.setter` method is changed to:
```python
    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if -180 <= long_value <= 180:
            self._longitude = long_value
        else:
            raise ValueError(f"{long_value} is an invalid value for longitude")
```
