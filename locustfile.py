import time
from locust import HttpUser, task


class WebsiteUser(HttpUser):
    
    
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    # @task
    # def index(self):
    #     self.client.get("/")
    #     self.client.get("/static/assets.js")
        
    # @task
    # def about(self):
    #     self.client.get("/about/")

    
    @task
    def makepredict(self):
        self.client.post('/predict', json={"CHAS":{  
          "0":0.0
       },
       "RM":{  
          "0":6.575
       },
       "TAX":{  
          "0":296.0
       },
       "PTRATIO":{  
          "0":15.3
       },
       "B":{  
          "0":396.9
       },
       "LSTAT":{  
          "0":4.98
       }})
