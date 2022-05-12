class MainController:
    def __init__(self, app) -> None:

        @app.route('/')
        def hello_word_route(): return self.hello_world()
        
    def hello_world(self):
        return "Hello World"
