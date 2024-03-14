import json

data = {
  "electronic_store": {
    "name": "Tech Haven",
    "slogan": "Your one-stop shop for all things tech!",
    "departments": {
      "laptops": {
        "brands": ["Apple", "Dell", "Lenovo", "HP", "Asus"],
        "featured_product": {
          "name": "MacBook Air M2",
          "price": 1299.00,
          "specs": {
            "cpu": "Apple M2 chip",
            "memory": "8GB",
            "storage": "512GB SSD",
            "display": "13.6-inch Retina display"
          }
        },
        "stock": [
          {
            "brand": "Dell",
            "model": "XPS 13",
            "price": 999.99,
            "quantity": 10
          },
          {
            "brand": "Lenovo",
            "model": "IdeaPad Flex 5",
            "price": 649.99,
            "quantity": 5
          }
        ]
      },
      "smartphones": {
        "brands": ["Apple", "Samsung", "Google", "OnePlus"],
        "on_sale": [
          {
            "brand": "Samsung",
            "model": "Galaxy S23 Ultra",
            "price": 1188.00,
            "discount": 10,
            "original_price": 1320.00
          },
          {
            "brand": "Google",
            "model": "Pixel 7 Pro",
            "price": 899.00,
            "discount": 5,
            "original_price": 949.00
          }
        ],
        "accessories": {
          "cases": ["Clear Case", "Leather Case", "Silicone Case"],
          "chargers": ["Wireless Charger", "Car Charger", "Power Bank"]
        }
      }
    },
    "customer_reviews": [
      {
        "name": "Alice Johnson",
        "rating": 5,
        "comment": "Great selection of products and knowledgeable staff!"
      },
      {
        "name": "Bob Smith",
        "rating": 4,
        "comment": "Competitive prices and fast shipping."
      }
    ]
  }
}


with open("practice_file.json", "w") as f:
    json.dump(data, f, indent=4)