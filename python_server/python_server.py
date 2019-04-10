
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

    def do_GET(self):

        if self.path.endswith("/"):
            restaurants_list = session.query(Restaurant).all()
            self.respond_200(mytemplates.index(restaurants_list))
        else:
            self.send_response(404)


    def respond_200(self, content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode())



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
