from django.shortcuts import render
from django.http import HttpResponse
import time
from datetime import datetime as dt

# Create your views here.
def hello_world(request):
    response = '''
                        <button onclick="http_req()">Start</button>
                        <div id="responses"></div>
                        <script>
                            var id = 1
                            function http_req(){
                                ch = document.createElement('div')
                                ch.id = id
                                ch.innerHTML='Waiting...'
                                document.getElementById('responses').appendChild(ch)
                                fetch("/timer").then(x=>x.text()).then(t=>{
                                    ch = document.getElementById(id)
                                    ch.innerHTML=t
                                    document.getElementById('responses').appendChild(ch)
                                })
                                id++
                            }       
                        </script>
        '''
    return HttpResponse(response)

def timer(request):
    start_time = str(dt.now())
    time.sleep(3)
    end_time = str(dt.now())
    return HttpResponse(f'{start_time} - {end_time}')
