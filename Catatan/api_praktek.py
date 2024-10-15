from fastapi import FastAPI, HTTPException, Header, Response
import pandas as pd

app = FastAPI()

# define api_key
apiKey = "secret123"

# base_url/domain
# http://www.google.com -> endpoint /
# http://127.0.0.1:8000 -> localhost:8000

# define url -> endpoint
@app.get("/")
def root():
    return {"message": "Selamat datang di Vercel!"}

@app.get("/protected")
def root(key: str = Header(None)):
    # cek api_key
    if key == None or key != apiKey:
        raise HTTPException(status_code=401, detail="invalid API key!")

    # get all data from dataframe
    df = pd.read_csv('data.csv')

    return df.to_dict(orient='records')

@app.get("/detail/{id}")
def root(id: int):
    # get all data from dataframe
    df = pd.read_csv('data.csv')

    # filter berdasarkan id
    filter = df[df.id == id]

    # cek filter apakah kosong?
    if len(filter) == 0:
        # return pesan error
        raise HTTPException(status_code=404, detail="data tidak ditemukan")
    else: 
        # return data nya
        # menampilkan filter sbg response 
        return filter.to_dict(orient='records')

# matiin server yang sedang running
# ctrl + c