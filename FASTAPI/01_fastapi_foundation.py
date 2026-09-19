from fastapi import FastAPI
from fastapi import Request
#from fastapi import str

import uvicorn

app = FastAPI(
     title="swiggy order serveric",
     description=(
        "Internal API for managingg orders"
        "Handle creation, trakcing of delivery systems"   
     ),
     version="1.2.1",
     docs_url="/docs",
     redoc_url="/redoc",
     openapi_url="/openeapi.json"

)

@app.get("/")
def read_root():
    """ROOT endpoint - Health Check"""
    # FastAPi converts this docs into JSON
    return {"message":"Welcome to swiggy Order Service",
            "Status": "healthy"}   

@app.get("/about")
def about():
    """Return API meta Data"""
    return {
        "service": "Order Service",
        "team": "black",
        "region":"south west",
        "version": "1.2.1"
    }

@app.get("/orders")
def orders():
    "List of recent orders"
    return {
        "orders":[
            {"id" : 1, "item": "Butter Chicken","status":"delivered" },
            {"id" : 2, "item": "masala Dosa","status":"delivered" },
            {"id" : 3, "item": "Panerr Tikka","status":"delivered" }
        ]
    }

@app.get("/orders/status")
def order_status():
    "Get order status"
    return {
        "today_total": 2_234_2,
        "top_city": "Bengaluru"
    }

@app.get('/debug/request-info')
async def request_info(request: Request):
    """Inspect the raw request object"""
    return {
        "method":request.method,
        "url":request.url,
        "headers": dict(request.headers),
        "path_params":  request.path_params,
        "query_params":dict(request.query_params)

    }

@app.get(
    "orders/active",
    summary ="Get Active Orders",
    description=(
        "Returns all orders that are currently being prepared"
        "or are out for delivery"
    ),
    tags=["orders"],
    response_description="list of acitve orders objects",
    deprecated=False
)

def get_active_order():
    """This docs string also appear in docs"""
    return{
        "active_orders":[
            {"id":1, "item": "Masala Dosa",
             "status": "out_for_delivery"}
        ]
    }

@app.get("/Restaurants", tags=["Restaurants"])
def list_resto():
    """list of restaurents"""
    return{
        "restaurants":[{
            "test":"test"
        }]
    }
@app.get("/Restaurants/delhi", tags=["Restaurants"])
def list_resto_delhi():
    """list of restaurents"""
    return{
        "restaurants":[{
            "test":"test"
        }]
    }