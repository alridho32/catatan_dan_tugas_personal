from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()
df = pd.read_csv('clean_df.csv')
df['id'] = df.index + 1

@app.get("/")
def root():
  return "This is the main endpoint of this API"

@app.get("/data")
def get_data():
    return df.to_dict(orient='records')

@app.delete("/data/{id}")
def remove_row(id:int):
    if id not in df['id'].values:
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    i = df[df['id']==id].index
    df.drop(i, inplace=True)
    df.to_csv('clean_df.csv', index=False)
    return {"message": f"Item with ID {id} has been deleted successfully."}