{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
    <div class="alert alert-{{category}}" role="alert">
    {{message }}
</div>
    {% endfor %}
  {% endif %}
{% endwith %}
