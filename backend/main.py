from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

origins=['*']
db={}
backup=[]
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=["*"])

menu_db = [
  {
    "id": 1,
    "name": "Doro Wot",
    "price": "320 ETB",
    "image": "images/doro.png",
    "category": "menu",
    "description": "A spicy Ethiopian chicken stew made with berbere spice blend, served with injera bread. Rich in flavor and tradition.",
    "furtherDescription": "Doro Wat is one of the most popular dishes in Ethiopian cuisine. This rich and spicy chicken stew is made with berbere, a complex spice blend that gives the dish its distinctive red color and deep flavor. Each serving traditionally includes a hard-boiled egg and is served on injera, a sourdough flatbread. The dish is slow-cooked to perfection, allowing the flavors to meld together creating a truly authentic taste of Ethiopia.",
    "translations": {
      "am": {
        "description": "በበርበሬ ቅመም የተቀቀለ ቀለም ያለው የዶሮ ወጥ፣ ከእንጀራ ጋር የሚቀርብ። በጣም በርበሬ እና ታሪክ የተሞላ።",
        "furtherDescription": "ዶሮ ወጥ በኢትዮጵያ ምግብ ውስጥ በጣም የተለመደ ነው። ይህ ቀለም ያለው እና ምርኩዝ የዶሮ ወጥ በበርበሬ ቅመም የተቀቀለ ሲሆን፣ ለውዝ ቀለምና ጥራት የሚሰጥ ነው። እያንዳንዱ አግባብ ቀብር ያለ እንቁላልን ይዟል እና በእንጀራ ላይ ይቀርባል። በቀስ ቀስ እየተቀመሰ የተሰራ ሲሆን ቀላል እና ታሪካዊ የኢትዮጵያ ጣዕምን ያቀርባል።"
      },
      "ti": {
        "description": "በበርበሬ ቅመም የተዘጋጀ ቀለም ያለው የዶሮ ወጥ፣ ከእንጀራ ጋር የሚቀርብ።",
        "furtherDescription": "ዶሮ ወጥ ናይ ኢትዮጵያ ዝበለጸ መግቢ እዩ። በበርበሬ ዝተሰራ፣ ቀለምን ዘይቤን ዘይት ዘምሮ። ናይ እንቁላል ንስኻት ይበሃልና ብእንጀራ ይገብር። ብቐሊሉ ዝተቀመሰ እዩ ናብ ዝተመሰገነ ዝገብር።"
      },
      "om": {
        "description": "Mi'aa daakuu diimaa daakuu fi berbere ittiin bilchaatee kan buddeen injeraa waliin dhihaatu.",
        "furtherDescription": "Doro Wot nyaata beekamaa Itoophiyaa keessaa tokko. Foon daakuu garmalee mi’aawu kan berbereen ittiin bilchaayeefi akkasumas qorichaan daakamee. Akkuma aadaa, akaayii cimaa fi injera waliin dhihaata. Itti fufinsaan bilchaachuun dadhabina nyaataa ni mijeessa."
      }
    }
  },
  {
    "id": 2,
    "name": "Tibs",
    "price": "300 ETB",
    "image": "images/tibs.png",
    "category": "menu",
    "description": "Sautéed beef or lamb cubes prepared with onions, tomatoes, and jalapeños. A popular Ethiopian dish perfect for sharing.",
    "furtherDescription": "Tibs is a beloved Ethiopian dish that features tender pieces of meat (beef or lamb) sautéed with vegetables. The meat is cut into small cubes and cooked with onions, tomatoes, and jalapeños in a distinctive style that seals in the flavors. It can be served with injera and various side dishes. The dish can be prepared with varying levels of spiciness to suit different palates. Our version includes a special blend of Ethiopian spices that gives it an authentic and unforgettable taste.",
    "translations": {
      "am": {
        "description": "ከሽንኩርት፣ ከቲማቲም እና ከጅማት ጋር የተጠበሰ የበሬ ወይም የበግ ስጋ። በኢትዮጵያ እጅግ የተወደደ ምግብ።",
        "furtherDescription": "ቲብስ በኢትዮጵያ የተወደደ የስጋ ምግብ ነው። በሬ ወይም በግ ስጋ ከተቆረጠ በኋላ ከአትክልቶች ጋር ይበስላል። ከእንጀራ እና ከተለያዩ አቀባበሎች ጋር ይሰራል። የተለያዩ የበርበሬ ደረጃዎች መሰረት ሊቀነስ ወይም ሊጨምር ይችላል።"
      },
      "ti": {
        "description": "ናይ በሬ ወይ ናይ በግ ስጋ ብሽንኩርቲ፣ ቲማቲምን የተበሰለ።",
        "furtherDescription": "ቲብስ ናይ ኢትዮጵያ ዝበለጸ መግቢ እዩ። ስጋ ንንኡ ክንዲ ዝተቆረጸ ብሽንኩርቲ፣ ቲማቲምን የተበሰለ። ብእንጀራ እና ምርጥ ጨረሪ ይገብር።"
      },
      "om": {
        "description": "Foon loonii ykn hoolaa kan qoreen gaggabaaboo ta’aniin, qorii, xaaxessaa fi dimbilaawitiin bilchaaye.",
        "furtherDescription": "Tibs nyaata Oromoofi Itoophiyaa keessaa tokko. Foon xixiqqeen qoran, qorii, xaaxessaa fi dimbilaawitiin qophaa’a. Akkuma fedhii, mi’aawina isaa ni jijjiirama. Injera waliin dhihaata."
      }
    }
  },
  {
    "id": 3,
    "name": "Kitfo",
    "price": "400 ETB",
    "image": "images/kitfo.png",
    "category": "menu",
    "description": "Minced beef marinated in mitmita and niter kibbeh, served either leb leb (warmed) or betam leb (cooked through).",
    "furtherDescription": "Kitfo is a traditional Ethiopian dish made from high-quality minced beef marinated in mitmita (a spicy powder) and niter kibbeh (clarified butter infused with herbs and spices). This delicacy can be served at various temperatures according to preference - from completely raw (tire), to slightly warmed (leb leb), or fully cooked (betam leb). It's traditionally served with collard greens and a mild cheese called ayib. Our kitfo is prepared using the finest quality beef and authentic Ethiopian spices.",
    "translations": {
      "am": {
        "description": "በሚትሚታና በንጥር ቅቤ የተሰኘ የተቀጠመ የበሬ ስጋ፣ በሌብ ሌብ ወይም በፍጹም የተቀመሰ መልኩ የሚቀርብ።",
        "furtherDescription": "ክትፎ በእጅጉ የተወደደ የኢትዮጵያ ባህላዊ ምግብ ነው። በሚትሚታና በቅመም የተቀቀለ ቅርጽ ያለው የበሬ ስጋ ነው። እሱን ምግብ ከሙሉ ሲደር እስከ በትንሹ ተሞልቶ (ሌብ ሌብ) ወይም እስከ ፍጹም የተቀመሰ መልኩ ድረስ የሚያወጣው ነው። አብዛኛው ግምጃ በጎመን እና አይብ ጋር ይሰራል።"
      },
      "ti": {
        "description": "ብሚትሚታን ናብ ዕፅ ቅቤ ዝተቀበለ ቅጥቲ ስጋ፣ ብለብለብ ወይ ብፍጹም ዝተቀመሰ ይገብር።",
        "furtherDescription": "ክትፎ ናይ ባህላዊ ኢትዮጵያ መግቢ እዩ። ናይ ምርጥ ቅጥቲ ዝተቀበለ ስጋ ብሚትሚታን ናብ ንጥር ቅቤ ዝተሰነየ። ኣብ ምዃኑ ብፍሉይ ዓይነት ሙቀት ክገብር ይኽእል፣ ሓሳብ ናይ ነቲ ምሳን እንተተኸላኸለ። ብጎመን እና ናይ ዝሑል ፍርስራሽ አይብ ይገብር።"
      },
      "om": {
        "description": "Foon daakamee, mitmitaa fi niitir qibxee keessatti dibamee, akka lubbuqaa ykn bilchaatee dhihaatu.",
        "furtherDescription": "Kitfo nyaata Oromoo fi Itoophiyaa keessaa beekkamaa dha. Foon qulqulluu daakamee mitmitaa fi niitir qibxee keessatti dibamee. Akka fedhii namatti, lubbuqaa (tire), halkanii (leb leb), yookaan guutumaan guutuutti bilchaatee dhihaata. Ayibii fi gommenn itti dabalamee dhihaata. Akkuma aadaa, mi’aawaa fi dhuga qabeessa ta’eedha."
      }
    }
  },
  {
    "id": 4,
    "name": "Beyaynet",
    "price": "280 ETB",
    "image": "images/Beyanynet.png",
    "category": "menu",
    "description": "A colorful platter of various vegetarian dishes served on injera. Perfect for those who want to try different Ethiopian flavors.",
    "furtherDescription": "Beyaynet is a colorful assortment of vegetarian dishes served on injera. This platter typically includes various dishes such as misir wat (spiced red lentils), shiro (ground chickpea stew), gomen (collard greens), tikil gomen (cabbage and carrots), atakilt wat (spiced vegetable stew), and other seasonal vegetables. Each component is carefully prepared with its own blend of spices and herbs, creating a harmonious combination of flavors and textures. This dish is not only visually stunning but also provides a complete nutritional profile, making it perfect for vegetarians and those wanting to explore Ethiopian cuisine.",
    "translations": {
      "am": {
        "description": "በእንጀራ ላይ የተዘጋጀ ብዙ የአትክልት ምግቦችን ያካተተ ባለቀለም አንደኛ ሳህን። የተለያዩ የኢትዮጵያ ጣዕሞችን ለመሞከር በጣም ተስማሚ ነው።",
        "furtherDescription": "በያይኔት በእንጀራ ላይ የሚዘጋጁ የተለያዩ አትክልት ምግቦችን የሚያካትት ነው። እነዚህ እንደ ምስር ወጥ፣ ሺሮ፣ ጎመን፣ ትክል ጎመን፣ አታኪልት ወጥና ሌሎች የወቅቱ አትክልቶችን ያካትታሉ። እያንዳንዱ ክፍል በተለያዩ ቅመሞችና ዕፅ ተዘጋጀ ሲሆን አንድነትና ምርጥ ጣዕም ያመጣል።"
      },
      "ti": {
        "description": "በእንጀራ ላይ ዘበለቐ ዝርዝር ናይ ናብ ተቀባ ዘለዎም ኣትክልቲ መግቢ።",
        "furtherDescription": "በያይኔት በበለጸ ናይ ናብ ናትኩሉ ዝተዘጋጀ ኣትክልቲ መግቢ እዩ። እነዚ ኣትክልቲ ኣብ ዚሕተት፣ ምስር ወጥ፣ ሺሮ፣ ጎመን፣ ትክል ጎመን፣ ኣታኪልት ወጥን ይካተቱ። ኣብ ውሽጡ ብቅመምን ዕፅን ዝተሰነየ ኣብ ምርጥ ጣዕም ይሰራ።"
      },
      "om": {
        "description": "Saanii dabalataa mi’aawaa garaagaraa kan injeraan irratti dhihaatu. Nama gosa nyaataa addaddaa ittiin qoratuuf mijaa’aa dha.",
        "furtherDescription": "Beyaynet saaniin nyaataa gosa gosa ta’an kan injeraan waliin dhihaatu dha. Fakkeenyaaf: misira wotii, shiroo, gommenn, tikil gomen (kaabisii fi karotii), atakilt wot fi kanneen biroo. Hundumtuu qoricha fi urgaa addaa ofii isaanii qabu. Kun nyaata mi’aawaa fi gosa baay’ee nama hawwatu dha."
      }
    }
  },
  {
    "id": 5,
    "name": "Enkulal Firfir",
    "price": "120 ETB",
    "image": "images/enkulalFirfir.png",
    "category": "breakfast",
    "description": "Scrambled eggs sautéed with onions, green peppers, and traditional spices. Served with injera or bread.",
    "furtherDescription": "Enkulal Firfir is a popular Ethiopian breakfast dish made by scrambling eggs with finely chopped onions, green peppers, and a mild mix of traditional spices. It's light, quick to prepare, and typically served with fresh injera or wheat-based bread. It's a staple morning meal for many households across the country.",
    "translations": {
      "am": {
        "description": "በሽንኩርትና በሚስሚስ በቅመም የተበሰለ የተባበሰ እንቁላል፣ ከእንጀራ ወይም ከዳቦ ጋር የሚቀርብ።",
        "furtherDescription": "እንቁላል ፍርፍር በቅመም፣ በተቀመጠ ሽንኩርትና በሚስሚስ የሚሰራ የኢትዮጵያ የመጀመሪያ ቀን ምግብ ነው። ከእንጀራ ወይም ከዳቦ ጋር ይቀርባል። በቀላሉ የሚዘጋጅ እና ቀለል ያለ ምግብ ነው።"
      },
      "ti": {
        "description": "ብሽንኩርቲ ና ሚስሚስ ብቅመም ዝተበሰለ የተባበሰ እንቁላል፣ ምስ እንጀራ ወይ ዳቦ ይቐርብ።",
        "furtherDescription": "እንቁላል ፍርፍር ናይ ቁልዒ ናይ መግቢ እዩ። ብሽንኩርቲ፣ ሚስሚስ ናብ ቅመም ዝተሰነየ እንቁላል ይበሰል። ብእንጀራ ወይ ዳቦ ይገብር።"
      },
      "om": {
        "description": "Qaqqawaa fi qaawwaa waliin kan bilchaaye, qoree fi qamadii keessaatti gabbifame. Waliin buddeena yookiin daabboo dhihaata.",
        "furtherDescription": "Enqulal Firfir nyaata ganamaa Itiyoophiyaa keessatti beekamaa ta’ee dha. Akkuma aadaa, qorii, qamadii fi dhadhaa waliin qophaa’a. Injera yookiin daabboo waliin dhiyaata. Baay’ee salphaa fi ariifachiisa dha."
      }
    }
  },
  {
    "id": 6,
    "name": "Chechebsa",
    "price": "150 ETB",
    "image": "images/chebchebsa.png",
    "category": "breakfast",
    "description": "Shredded flatbread pan-fried with niter kibbeh and berbere spice. A warm and satisfying Ethiopian breakfast dish.",
    "furtherDescription": "Chechebsa, also known as kita firfir, is a beloved Ethiopian breakfast made from torn pieces of flatbread sautéed in spiced clarified butter (niter kibbeh) and berbere. It's often served with a side of honey or yogurt. Rich, hearty, and full of flavor, it's a great way to start the day.",
    "translations": {
      "am": {
        "description": "በቅቤና በበርበሬ የተበሰለ የተተተ ኩባያ። የማልዶ እና ከመቼ የሚዘጋጅ የኢትዮጵያ ቁርስ።",
        "furtherDescription": "ቸቸብሳ ወይም ኪታ ፍርፍር በበርበሬና በንጥር ቅቤ የተሰነዘዘ የተተተ ዳቦ ነው። ከማር ወይም ከሙቀት እንቁላል ጋር ይቀርባል። ሙሉ በሙሉ ጣዕሙ የተሞላ፣ ቀኑን በጥሩ ሁኔታ ለመጀመር ተስማሚ ነው።"
      },
      "ti": {
        "description": "ብንጥር ቅቤን በበርበሬ ዝተበሰለ ናይ ኩባያ ፍርፍር። ናይ መባል መግቢ ዘመን እዩ።",
        "furtherDescription": "ቸቸብሳ ወይ ኪታ ፍርፍር ናይ ቁልዒ መግቢ እዩ። ኩባያ ብበርበሬን ብንጥር ቅቤን ዝተተተ ይበሰል። ብማር ወይ ናይ ሮብ እንቁላል ይገብር።"
      },
      "om": {
        "description": "Buddeena daakamee kan dhadhaa ittiin bilchaaye fi bultii ganamaa tajaajilamu.",
        "furtherDescription": "Chechebsa ykn Kita Firfir nyaata ganamaa Oromoota fi Itiyoophiyaa keessatti beekamaa dha. Buddeena furamee, dhadhaa fi berbereen bilchaaye. Akkasumas, yeroo tokko tokko waan mi’aawaa ykn aannan waliin dhiyaata. Nyaata qabbanaa’aa fi gammachiisaa dha."
      }
    }
  },
  {
    "id": 7,
    "name": "Shai (Spiced Ethiopian Tea)",
    "price": "40 ETB",
    "image": "images/tea.png",
    "category": "drinks",
    "description": "A traditional black tea brewed with spices like cinnamon and cloves. Comforting, aromatic, and enjoyed hot.",
    "furtherDescription": "Shai is a beloved Ethiopian spiced tea made by brewing black tea leaves with warm spices such as cinnamon, cloves, and sometimes ginger. It’s often sweetened with sugar and served piping hot. Shai is a go-to drink in Ethiopian households, especially during breakfast or casual gatherings.",
    "translations": {
      "am": {
        "description": "በቅመም እንደ ዝንጀት እና ቅንደ አትር የተቀቀለ ባህላዊ ጥቁር ሻይ። በደስታ የሚያገለግል እና በሙቀት የሚወሰድ።",
        "furtherDescription": "ሻይ በትምች እና በቅመም ከተቀቀለ ጥቁር ሻይ ቅጥ የተዘጋጀ ነው። በተለምዶ በስኳር ይቀመሳል እና በሙቀት ይዘጋጃል። በኢትዮጵያ ቤተሰቦች ውስጥ ከብስክና ጋር ወይም በመግቢ ቅድመ ጊዜ ይጠጣል።"
      },
      "ti": {
        "description": "ባህላዊ ጥቁር ሻይ ብዝንጀት፣ ቅንደ ኣትር ዘተሰነዘዘ፣ ብምዓዲ ዝተጠገመ።",
        "furtherDescription": "ሻይ ናይ ጥቁር ባህላዊ ሻይ እዩ ። ብቅመም ከም ዝንጀት፣ ቅንደ ኣትር ኣብ ውሃ ዝተቀቀለ እዩ። ብስኳር ዝተማማነ ኣብ መእተዊ ቦታታት ይሰብስብ።"
      },
      "om": {
        "description": "Shayi aadaa Itoophiyaa kan xaa'oo diimaa fi qabeelaa akka daldala, zinjibila waliin bilchaayee. Damma yookiin shukkaarin mi'aawaa ta'a.",
        "furtherDescription": "Shayi Itoophiyaa keessatti dhugaatii beekamaa. Xaa'oo diimaa waliin makamee, yeroo baay’ee zinjibila, qabeelaa fi daldala waliin bilchaaya. Shukkaarin yookiin dammaan mi’aawaa taasifamee, yeroo qabbana'aatti ni dhugama. Nyaata dura ykn boqonnaa irratti ni fayyada."
      }
    }
  },
  {
    "id": 8,
    "name": "Ethiopian Coffee (Bunna)",
    "price": "70 ETB",
    "image": "images/buna.png",
    "category": "drinks",
    "description": "Traditional Ethiopian coffee prepared in a jebena, often brewed with cardamom. Deep, aromatic, and part of a cherished coffee ceremony.",
    "furtherDescription": "Ethiopian coffee, locally known as bunna, is an essential part of Ethiopian culture and hospitality. Prepared using a clay pot called jebena, the coffee is often lightly spiced with cardamom and served in small cups. It is usually enjoyed in a three-round ceremony known as abol, tona, and bereka. The experience is both social and spiritual.",
    "translations": {
      "am": {
        "description": "በጀበና የተዘጋጀ ባህላዊ ኢትዮጵያ ቡና፣ በአንደኛ ጊዜ ከአሎም ጋር። የበርበሬ ሽታ እና ባህላዊ ሥርዓት አካል።",
        "furtherDescription": "ቡና በኢትዮጵያ ባህልና እንክብካቤ ውስጥ በጣም አስፈላጊ ነው። በጀበና የሚዘጋጀ ቡና በአንደኛ ጊዜ ከአሎም ጋር ይቀመሳል። አቦል፣ ቶና፣ በረካ የተባሉ አሶሳስ ክፍሎች ይከተላሉ። ለማህበረሰብ መደማመጥ እና መንፈሳዊነት አንዱ ነው።"
      },
      "ti": {
        "description": "ባህላዊ ኢትዮጵያ ቡና ብጀበና ዝተዘጋጀ፣ ንአሎም ዝተኻሰተ ክንደይ እዩ። ሽታ ብምስካዕ እና መንፈሳዊ ልምዲ እዩ።",
        "furtherDescription": "ቡና ናይ ኢትዮጵያ ባህሊ እና መስተዋድዲ ብኣብ እዩ። ብጀበና ዝተሰነዘዘ፣ ንአሎም ዝተኻሰተ ይሰርሕ። ተለምዲ ምስ ኣቦል፣ ቶና፣ በረካ ዝተባሉ ሶስተ ዙርያት ይውሰዱ።"
      },
      "om": {
        "description": "Buna Itoophiyaa kan jebenaa keessatti bilchaaye, yeroo tokko tokko qabeelaa irraa foolii argatu.",
        "furtherDescription": "Buna eenyummaa fi aadaa Itoophiyaa calaqqisiisa. Jebenaa jedhamu keessatti bilcha’ee, yeroo baay’ee qabeelaa waliin tajaajilama. Sosochii hawaasummaa fi lammii walitti fidu; yeroo hedduu sadii: Abol, Tonaa fi Bireekaa jedhamanii tajaajilamu."
      }
    }
  }
]

@app.get('/menuData/')
async def menuData():
    print('huh')
    return menu_db

@app.put('/editFood/')
def editFood(id):
    return

@app.post('/addFood/')
def addFood():
    return

@app.delete('/deletefood')
def deleteFood(item, restaurant_id):
    backup.addBackup(item, restaurant_id)
    return

if __name__ == "__main__":
    uvicorn.run("main:app", host = 'localhost', port=5000, reload = True)