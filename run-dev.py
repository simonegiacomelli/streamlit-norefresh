#!/usr/bin/env python3
import subprocess
import sys
from multiprocessing import Pool
import tornado.web
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
print('script_dir', script_dir)
os.chdir(script_dir)


class TrudyHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self):
        """/OPTIONS handler for preflight CORS checks."""
        self.set_status(204)
        self.finish()

    def get(self) -> None:
        self.write('hello')
        self.set_header("Content-Type", "text/plain")
        self.set_status(200)


def run_command(command: str, working_dir):
    if not command.startswith('streamlit'):
        process = subprocess.Popen(command, cwd=working_dir, shell=True)
        process.wait()
    else:
        import tornado.web
        import streamlit.server.server as server
        original_start_listening = server.start_listening

        def start_listening(app: tornado.web.Application) -> None:
            print('got you')
            app.add_handlers(r".*", [('/trudy', TrudyHandler)])
            original_start_listening(app)

        server.start_listening = start_listening
        import streamlit.cli as cli
        os.chdir(working_dir)
        sys.argv = ['x', 'run', 'app.py']
        cli.main(prog_name="streamlit")


def run_in_pool(commands):
    pool = Pool(len(commands))
    pool.starmap(run_command, commands)


def test_streamlit():
    try:
        import streamlit
    except Exception as ex:
        print(f'Exception `{ex}` ')
        sys.exit(1)


test_streamlit()

print('hehe')

run_in_pool(
    [
        # ('npm start', './example_component/frontend'),
        # ('npm start', './foobar_component/frontend'),
        ('streamlit run app.py', '.')
    ]
)
