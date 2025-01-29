from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

def scrape_mercado_libre(search_term):
    encoded_search_term = quote(search_term)
    url = f"https://listado.mercadolibre.com.co/{encoded_search_term}#D[A:{encoded_search_term}]"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all('li', class_='ui-search-layout__item shops__layout-item'):
        name = item.find('a', class_='poly-component__title').text
        price_element = item.find('span', class_='andes-money-amount__fraction')
        price = float(price_element.text.replace('.', '').replace(',', '.')) if price_element else None
        discount_element = item.find('span', class_='andes-money-amount__discount')
        discount = float(discount_element.text.replace('%', '').replace(' OFF', '')) if discount_element else None
        seller = item.find('span', class_='poly-component__seller').text if item.find('span', class_='ui-search-official-store-label') else 'Unknown'
        rating_element = item.find('span', class_='poly-reviews__rating')
        rating = float(rating_element.text) if rating_element else None
        image_url = item.find('img')['src'] if item.find('img').has_attr('src') else item.find('img')['src']
        product_url = item.find('a', class_='poly-component__title')['href']

        products.append({
            'name': name,
            'price': price,
            'discount': discount,
            'seller': seller,
            'rating': rating,
            'image_url': image_url,
            'product_url': product_url
        })

    return products

def FiltroArticulos(products):
    if not products:
        return {}

    articulo_precio_mas_bajo = min(products, key=lambda x: x['price'])
    articulo_precio_mas_alto = max(products, key=lambda x: x['price'])
    articulo_descuento_mas_alto = max(products, key=lambda x: x['discount'] if x['discount'] is not None else 0)
    precio_promedio = sum(p['price'] for p in products if p['price'] is not None) / len(products)
    articulo_mejor_calificacion = max(products, key=lambda x: x['rating'] if x['rating'] is not None else 0)

    return {
        'articulo_precio_mas_bajo': articulo_precio_mas_bajo,
        'articulo_precio_mas_alto': articulo_precio_mas_alto,
        'articulo_descuento_mas_alto': articulo_descuento_mas_alto,
        'precio_promedio': precio_promedio,
        'articulo_mejor_calificacion': articulo_mejor_calificacion
    }