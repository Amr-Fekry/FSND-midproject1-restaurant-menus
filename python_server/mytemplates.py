
html_layout = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Restaurant Menus</title>
    </head>
    <body>
    {}
    </body>
    </html>
"""

# ------------------------------------------

def index(restaurants_list):
    """
        args: 
        restaurants_list - a list of Restaurant objects
        returns: dynamically generated html page (index) in string foramt
    """

    body = """
        <h1>Restaurants</h1>
        
        <ul>
            {}
        </ul>
        <a href="#">add new restaurant</a>
    """

    ul = []
    for restaurant in restaurants_list:
        li = f"""
            <li>
              <a href="#">{ restaurant.name }</a>
              <br>
              <a href="#">Edit</a>
              <a href="#">Delete</a>
              <hr>
            </li>
        """
        ul.append(li)

    return html_layout.format(body.format(''.join(ul)))

# ------------------------------------------

