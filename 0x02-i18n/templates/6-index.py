<!DOCTYPE html>
<html lang="{{ request.locale }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('home_title') }}</title>
</head>
<body>
    {% if g.user %}
    <p>{{ _('logged_in_as', username=g.user["name"]) }}</p>
    {% else %}
    <p>{{ _('not_logged_in') }}</p>
    {% endif %}
</body>
</html>
