def predict_traffic_alert(city_name):
    # Example logic for demo purposes
    # In reality, you would use city_name to query a database or API for traffic data
    if city_name.lower() in ['new york', 'los angeles', 'chicago']:
        return 'Traffic Alert: High congestion expected in ' + city_name
    else:
        return 'Traffic Alert: Traffic conditions are normal in ' + city_name
