from locust import HttpUser, task, between

class MiUsuario(HttpUser):
    wait_time = between(1, 5)

    @task
    def cargar_pagina(self):
        self.client.get("/")
