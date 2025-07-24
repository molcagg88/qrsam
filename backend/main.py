from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
import uvicorn
from datetime import timedelta, datetime, timezone
from pydantic import BaseModel, RootModel
from typing import Optional
import copy
from typing import Dict, List
from jose import jwt, JWTError


menu_db = {"usr":{
  1: {
    "name": "Doro Wot",
    "price": "320 ETB",
    "image": "images/doro.png",
    "category": "menu",
    "ingredients": {
      "en": "chicken, berbere spice, niter kibbeh, onion, boiled egg, injera",
      "am": "ዶሮ, በርበሬ, ንጥር ቅቤ, ሽንኩርት, በደምብ የተቀቀለ እንቁላል, እንጀራ",
      "ti": "ዶሮ, በርበሬ, ንጥር ቅቤ, ሽንኩርቲ, እንቁላል, እንጀራ",
      "om": "foolii daakuu, berberee, niitir qibxee, qorii, ayibii, injera"
    }
  },
  2: {
    "name": "Tibs",
    "price": "300 ETB",
    "image": "images/tibs.png",
    "category": "menu",
    "ingredients": {
      "en": "beef or lamb, onion, tomato, jalapeño, Ethiopian spices",
      "am": "የበሬ ወይም የበግ ስጋ, ሽንኩርት, ቲማቲም, ጅማት, የኢትዮጵያ ቅመም",
      "ti": "ስጋ, ሽንኩርቲ, ቲማቲም, ጅማት, ቅመም",
      "om": "foona loonii yookaan hoolaa, qoree, xaaxessaa, dimbilaawii, xaxaa Itoophiyaa"
    }
  },
  3: {
    "name": "Kitfo",
    "price": "400 ETB",
    "image": "images/kitfo.png",
    "category": "menu",
    "ingredients": {
      "en": "minced beef, mitmita, niter kibbeh, ayib cheese, gomen (collard greens)",
      "am": "ቅመም የተዘጋጀ የተቀጠመ የበሬ ስጋ, ሚትሚታ, ንጥር ቅቤ, አይብ, ጎመን",
      "ti": "ቅጥቲ ስጋ, ሚትሚታ, ንጥር ቅቤ, አይብ, ጎመን",
      "om": "foon daakamee, mitmitaa, niitir qibxee, ayibii, gommenn"
    }
  },
  4: {
    "name": "Beyaynet",
    "price": "280 ETB",
    "image": "images/Beyanynet.png",
    "category": "menu",
    "ingredients": {
      "en": "injera, misir wot, shiro, gomen, tikil gomen, atakilt wot, seasonal vegetables",
      "am": "እንጀራ, ምስር ወጥ, ሺሮ, ጎመን, ትክል ጎመን, አታኪልት ወጥ, የወቅቱ አትክልት",
      "ti": "እንጀራ, ምስር, ሺሮ, ጎመን, ትክል ጎመን, ኣታኪልት, ወትዑ አትክልቲ",
      "om": "injera, misira wotii, shiroo, gommenn, tikil gomen, atakilt wot, mudhii gosa garaagaraa"
    }
  },
  5: {
    "name": "Enkulal Firfir",
    "price": "120 ETB",
    "image": "images/enkulalFirfir.png",
    "category": "breakfast",
    "ingredients": {
      "en": "eggs, onion, green pepper, Ethiopian spices, injera or bread",
      "am": "እንቁላል, ሽንኩርት, ሚስሚስ, ቅመም, እንጀራ ወይም ዳቦ",
      "ti": "እንቁላል, ሽንኩርቲ, ሚስሚስ, ቅመም, እንጀራ ወይ ዳቦ",
      "om": "qulqulluu, qoree, qamadii, xaxaa aadaa, injera ykn daabboo"
    }
  },
  6: {
    "name": "Chechebsa",
    "price": "150 ETB",
    "image": "images/chebchebsa.png",
    "category": "breakfast",
    "ingredients": {
      "en": "flatbread, niter kibbeh, berbere, honey or yogurt (optional)",
      "am": "ኩባያ, ንጥር ቅቤ, በርበሬ, ማር ወይም ዮጎርት (አማራጭ)",
      "ti": "ኩባያ, ንጥር ቅቤ, በርበሬ, ማር ወይ ሮብ",
      "om": "buddeena, niitir qibxee, berberee, damma ykn aannan (filannoo)"
    }
  },
  7: {
    "name": "Shai (Spiced Ethiopian Tea)",
    "price": "40 ETB",
    "image": "images/tea.png",
    "category": "drinks",
    "ingredients": {
      "en": "black tea, cinnamon, cloves, ginger (optional), sugar",
      "am": "ጥቁር ሻይ, ዝንጀት, ቅንደ አትር, ዝንጅብል (አማራጭ), ስኳር",
      "ti": "ጥቁር ሻይ, ዝንጀት, ቅንደ ኣትር, ዝንጅብል, ስኳር",
      "om": "shayi gurraacha, daldala, qabeelaa, zinjibila, shukkaar"
    }
  },
  8: {
    "name": "Ethiopian Coffee (Bunna)",
    "price": "70 ETB",
    "image": "images/buna.png",
    "category": "drinks",
    "ingredients": {
      "en": "Ethiopian coffee beans, cardamom, served in jebena",
      "am": "የኢትዮጵያ ቡና, አሎም, በጀበና የተዘጋጀ",
      "ti": "ቡና, አሎም, ጀበና",
      "om": "buna Itoophiyaa, qabeelaa, jebenaa keessatti bilchaaye"
    }
  }}
}

user_db = {
    "usr":{
    "restaurant_id":1,
    "password": "pwd"}
}
origins=['*']
db={}
backup=[]
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=["*"])

secret_key='esrom'
algo='HS256'
oauth2scheme = OAuth2PasswordBearer(tokenUrl='/token')

class LoginReq(BaseModel):
    username:str
    password:str
  
class TokenRes(BaseModel):
    access_token: str
    usr: str
    token_type: str = "bearer"

class MenuRequest(BaseModel):
  restaurant_id: str

class MenuItem(BaseModel):
    name: str
    price: str
    category: str
    ingredients: str

class MenuData(RootModel[Dict[int, MenuItem]]):
    pass

def create_accessToken(data: dict, exp: Optional[timedelta] = None):
  to_encode=copy.deepcopy(data)
  expiry = datetime.now(timezone.utc) + (exp or timedelta(minutes=60))
  to_encode.update({"exp": int(expiry.timestamp())})
  encoded = jwt.encode(to_encode, secret_key, algorithm=algo)

  return encoded

def decode_token(token: str):
    try:
      payload=jwt.decode(token, secret_key, algorithms=[algo])
      print(f"{payload.get('restaurant_id')}")
      return (payload.get('restaurant_id'))
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

async def get_current_user(token: str = Depends(oauth2scheme)):
    return decode_token(token)

def authenticate_user(uname, pwd):
    user = user_db.get(uname)
    if user and user['password']==pwd:
        return uname
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong credentials")



@app.get('/')
def home():
    return 


@app.post('/menuData/')
async def menuData(data: MenuRequest):
    return menu_db[data.restaurant_id]


@app.put('/editData/')
def editData(data: MenuData, restaurant_id: str = Depends(get_current_user)):
    print("edit request recieved")
    item_id, item = next(iter(data.root.items()))
    print(item_id)
    if item_id in menu_db[restaurant_id]:
        print("item to be edited found!")
        try:
          temporary_edit = copy.deepcopy(menu_db[restaurant_id][item_id])
          full_edit = menu_db[restaurant_id]
          temporary_edit["name"]=item.name
          temporary_edit["price"]=item.price
          temporary_edit["category"]=item.category
          temporary_edit["ingredients"]=item.ingredients
          
          full_edit[item_id] = temporary_edit
          print(full_edit)
          return True
        except Exception as e:
            print(f"error:{e}")
            return e

@app.post('/login/', response_model=TokenRes)
def login(login_data: LoginReq):
    user = authenticate_user(login_data.username, login_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username or password")
    access_token = create_accessToken(data={'sub':user, "restaurant_id":login_data.username})
    return {"access_token":access_token, "usr":user}
    

# @app.put('/editFood/')
# def editFood(edits):
    
#     return

# @app.post('/addFood/')
# def addFood():
#     return

# @app.delete('/deletefood')
# def deleteFood(item, restaurant_id):
#     backup.addBackup(item, restaurant_id)
#     return

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)