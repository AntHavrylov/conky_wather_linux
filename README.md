# Conky Weather Widget

This project provides a Conky widget that displays the current weather information for a specified city.

## Files

- `weather.conf`: The Conky configuration file.
- `script.py`: A Python script that fetches weather data from the OpenWeatherMap API.
- `config.json`: The configuration file for the Python script.
- `data.json`: A cache file for the weather data.

## Configuration

The `config.json` file is used to configure the Python script. It has the following fields:

- `api_key`: Your API key for the OpenWeatherMap API.
- `city`: The city for which you want to display the weather.

Example:

```json
{
    "api_key": "your_api_key",
    "city": "your_city"
}
```

## Usage

1.  Install Conky.
2.  Get an API key from the OpenWeatherMap API.
3.  Create a `config.json` file with your API key and city.
4.  Run Conky with the `weather.conf` file:

```bash
conky -c /home/<USERNAME>/.config/conky/weather.conf
```
## Autostart with os
create file `conky-weather.desktop` in /home/<USERNAME>/.config/autostart

Example:
!!! change `<USERNAME>` to your `user name in OS`

```
[Desktop Entry]
Type=Application
Exec=conky -c /home/<USERNAME>/.config/conky/weather.conf
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Conky_Weather
Comment=Start Conky at login
```
