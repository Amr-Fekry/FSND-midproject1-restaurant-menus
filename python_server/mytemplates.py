
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
              <a href="/restaurants/{restaurant.id}/menu/">{ restaurant.name }</a>
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

# ------------------------------------------

def edit_restaurant(restaurant):
    """
        args: 
        restaurant - the Restaurant object of interest
        returns an html edit_restaurant form in string foramt
    """

    body = f"""
        <h1>Edit { restaurant.name }</h1>
        <form action="/restaurants/{restaurant.id}/edit/" method="post">
          <input name="restaurant_new_name" type="text" placeholder="{ restaurant.name }">
          <br><br>
          <input type="submit" value="Edit">
          <a href="/">Cancel</a>
        </form>
    """

    return html_layout.format(body)

# ------------------------------------------

def delete_restaurant(restaurant):
    """
        args: 
        restaurant - the Restaurant object of interest
        returns an html delete_restaurant form in string foramt
    """

    body = f"""
        <h1>Are you sure you want to delete { restaurant.name } ?</h1>
        <form action="/restaurants/{restaurant.id}/delete/" method="post">
          <button name="answer" value="yes">YES</button>
          <button name="answer" value="no">NO</button>
        </form>
    """

    return html_layout.format(body)

def restaurant_menu(restaurant, menu_items):
    """
        args: 
        restaurant - the Restaurant object of interest
        menu_items - a list of MenuItem objects of the restaurant
        returns: dynamically generated html page (index) in string foramt
    """

    body = """
        <h1>{}</h1>
        <ul>
            {}
        </ul>
        <a href="#">add new item</a>
        <br>
        <a href="/">HOME</a>
    """

    ul = []
    for item in menu_items:
        li = f"""
            <li>
                Name: { item.name } <br>
                Course: { item.course } <br>
                Price: { item.price } <br>
                Description: { item.description } <br>
                <a href="#">Edit</a>
                <a href="#">Delete</a>
                <hr>            
            </li>
        """
        ul.append(li)

    return html_layout.format(body.format(restaurant.name, ''.join(ul)))

