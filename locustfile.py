from locust import HttpUser, task

class Boycott_Japanese_Language(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/")