
# add parent directory to python modules path.
import sys
sys.path.append("..")

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, unquote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_setup import Base, Restaurant, MenuItem
import mytemplates
import re


# connect to DB and DB tables
engine = create_engine('sqlite:///../database/restaurantmenu.db')
Base.metadata.bind = engine
# establish 'session' connection for CRUD executions
DBSession = sessionmaker(bind=engine)
session = DBSession()


class server_handler(BaseHTTPRequestHandler):

    def do_GET(self): self.check_routes('GET')
    def do_POST(self): self.check_routes('POST')

    def check_routes(self, method):
        route = self.route

        if route('/'):
            self.index()
        elif route('/restaurants/add/'):
            self.add_restaurant(method)
        elif route('/restaurants/<int:restaurant_id>/edit/'):
            self.edit_restaurant(method)
        elif route('/restaurants/<int:restaurant_id>/delete/'):
            self.delete_restaurant(method)
        elif route('/restaurants/<int:restaurant_id>/menu/'):
            self.restaurant_menu()

        else: self.send_response(404)
    
    # ~~~~~~~~~~~~  ROUTE FUNCTIONS:
    
    def index(self):
        restaurants_list = session.query(Restaurant).all()
        self.respond_200(mytemplates.index(restaurants_list))

    def add_restaurant(self, method):
        if method == 'POST':
            restaurant_name = self.form_inputs('restaurant_name')
            if restaurant_name:
                new_restaurant = Restaurant(name=restaurant_name)
                session.add(new_restaurant)
                session.commit()
                self.respond_303('/')
            else:
                self.respond_200("Name field is empty!")

        else:
            self.respond_200(mytemplates.add_restaurant())

    def edit_restaurant(self, method):
        restaurant_id = self.path.split('/')[2]
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        
        if method == 'POST':
            
            restaurant_new_name = self.form_inputs('restaurant_new_name')
            if restaurant_new_name:
                restaurant.name = restaurant_new_name
                session.add(restaurant)
                session.commit()
                self.respond_303('/')
            else:
                self.respond_200("You haven't entered a name!")

        else:
            self.respond_200(mytemplates.edit_restaurant(restaurant))

    def delete_restaurant(self, method):
        restaurant_id = self.path.split('/')[2]
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

        if method == 'POST':
            answer = self.form_inputs('answer')
            if answer == 'yes':
                session.delete(restaurant)
                session.commit()
            self.respond_303('/')

        else:
            self.respond_200(mytemplates.delete_restaurant(restaurant))

    def restaurant_menu(self):
        restaurant_id = self.path.split('/')[2]
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        menu_items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()

        self.respond_200(mytemplates.restaurant_menu(restaurant, menu_items))

    # ~~~~~~~~~~~~  HELPER FUNCTIONS:

    def form_inputs(self, key):
        data_byte_length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(data_byte_length).decode()
        params = parse_qs(data)
        value = params.get(key)
        return value[0] if value else False

    def route(self, path):
        path = path.replace('<int:restaurant_id>', '[0-9]+').replace('<int:item_id>', '[0-9]+')
        path1 = f"^{path}$"
        path2 = f"^{path[:-1]}$"

        if bool(re.match(path1, self.path)): return True
        elif bool(re.match(path2, self.path)): return True
        else: return False

    def respond_200(self, content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode())

    def respond_303(self, path):
        self.send_response(303)
        self.send_header('Location', path)
        self.end_headers()



if __name__ == '__main__':
    try:
        port = 8080
        host = '' # Serve on all addresses
        server_address = (host, port)
        server = HTTPServer(server_address, server_handler)
        
        print(f"Web server running on port {port}")
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()
