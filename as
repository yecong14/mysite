{% extends "base.html" %}
{% load staticfile %}
{% block title %}change password{% endblock %}
{% block contain %}
<h1>Change password</h1>
<div class="breadcrumbs">
<p>Password change</p>

<form method="post">{% csrf_token %}

<p>Please enter your old password, for security's sake, and then enter your new password twice so we can verify you typed it in correctly.</p>

<fieldset class="module aligned wide">

<div class="form-row">
    {{ form.old_password.errors }}
    {{ form.old_password.label_tag }} {{ form.old_password }}
</div>

<div class="form-row">
    {{ form.new_password1.errors }}
    {{ form.new_password1.label_tag }} {{ form.new_password1 }}
    {% if form.new_password1.help_text %}
    <div class="help">{{ form.new_password1.help_text|safe }}</div>
    {% endif %}
</div>

<div class="form-row">
{{ form.new_password2.errors }}
    {{ form.new_password2.label_tag }} {{ form.new_password2 }}
    {% if form.new_password2.help_text %}
    <div class="help">{{ form.new_password2.help_text|safe }}</div>
    {% endif %}
</div>

</fieldset>

<div class="submit-row">
    <input type="submit" value="{% trans 'Change my password' %}" class="default" />
</div>

</div>
</form></div>

{% endblock %}