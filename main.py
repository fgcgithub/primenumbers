from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Primzahlen-API",
    description="Eine einfache API-App zur Berechnung von Primzahlen.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def ist_primzahl(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.get("/api/primes")
def get_primes(start: int, end: int):
    if end - start > 100000:
        return {"error": "Der Bereich ist zu groß (maximal 100.000 Zahlen)."}
    primes = [x for x in range(start, end + 1) if ist_primzahl(x)]
    return {
        "start": start,
        "end": end,
        "count": len(primes),
        "primes": primes
    }
@app.get("/")
def home():
    base_url = "[https://primeapp-hwfwbehndfffajds.canadaeast-01.azurewebsites.net](https://primeapp-hwfwbehndfffajds.canadaeast-01.azurewebsites.net)"
    return {
        "message": "Willkommen bei deiner Azure Primzahlen-API!",
        "status": "Online und betriebsbereit 🚀",
        "description": "Dieser Microservice berechnet alle Primzahlen in einem von dir definierten Bereich.",
        "interactive_swagger_documentation": f"{base_url}/docs",
        "example_api_call": {
            "description": "Berechne alle Primzahlen von 1 bis 100",
            "url": f"{base_url}/api/primes?start=1&end=100"
        }
    }

