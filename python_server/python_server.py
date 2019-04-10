
# add parent directory to python modules path.
import sys
sys.path.append("..")

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_setup import Base, Restaurant, MenuItem
import mytemplates


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
        
        else: self.send_response(404)
    
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


    def form_inputs(self, key):
        data_byte_length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(data_byte_length).decode()
        params = parse_qs(data)
        value = params.get(key)
        return value[0] if value else False

    def route(self, path):
        if self.path in [path, path[:-1]]:
            return True
        return False

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
