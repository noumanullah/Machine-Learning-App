from app import app


def test_prediction_value():
    with app.test_client() as c:
        rv = c.post('/predict', json={"CHAS":{  
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
    
        json_data = rv.get_json()['prediction'][0]

        assert json_data == 20.35373177134412



def test_prediction_keyword():
    with app.test_client() as c:
        rv = c.post('/predict', json={"CHAS":{  
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
    
        #json_data = rv.get_json()['prediction'][0]
        
        # check whether the json response contains the 'prediction' keyword
        assert rv.get_json().__contains__('prediction')


def test_prediction_list_length():
    with app.test_client() as c:
        rv = c.post('/predict', json={"CHAS":{  
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
    
        json_data = rv.get_json()['prediction']
        
        #check whether the list that is retrieved has only one value in it
        assert len(json_data) == 1

        
def test_prediction_content_type():
    with app.test_client() as c:
        rv = c.post('/predict', json={"CHAS":{  
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

        content_type = rv.headers['Content-Type']

        assert content_type == 'application/json'

def test_prediction_status():
    with app.test_client() as c:
        rv = c.post('/predict', json={"CHAS":{  
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

        status = rv.status_code
        
        assert status == 200
