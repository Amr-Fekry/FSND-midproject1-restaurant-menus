
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
        <a href="/restaurants/add/">add new restaurant</a>
    """

    ul = []
    for restaurant in restaurants_list:
        li = f"""
            <li>
              <a href="#">{ restaurant.name }</a>
              <br>
              <a href="/restaurants/{ restaurant.id }/edit/">Edit</a>
              <a href="/restaurants/{ restaurant.id }/delete/">Delete</a>
              <hr>
            </li>
        """
        ul.append(li)

    return html_layout.format(body.format(''.join(ul)))

# ------------------------------------------

def add_restaurant():
    """
        returns an html add_restaurant form in string foramt
    """

    body = """
        <h1>Add New Restaurant</h1>

        <form action="/restaurants/add/" method="post">

        <input name="restaurant_name" type="text" placeholder="Restaurant Name">

        <br><br>
        <input type="submit" value="Add">
        <a href="/">Cancel</a>

        </form>
    """

    return html_layout.format(body)
