def add_custom_errors(form):
    code_data = form.data.get('code')
    if form.is_valid():
        if not code_data.startswith(current_year):
            form.add_error('code', 'promo code is expired')
        if not code_data.endswith('django'):
            form.add_error('code', 'checksum is invalid')
