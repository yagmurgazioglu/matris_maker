
import turtle
def matriskutusu(sayi1,sayi2):
    ilkmatris = []
    yüzeysayisi=sayi1
    yüzeybölüm=sayi2
    a = np.zeros(shape=(yüzeysayisi, yüzeybölüm), dtype = int )
    z=0
    for i in  range(yüzeysayisi*yüzeybölüm):
       girilensayi= int(input(f"{i+1}. sayınızı giriniz: "))
       ilkmatris.append(girilensayi)
    for n in range(yüzeysayisi):
        for f in range(yüzeybölüm):
            a[n,f]=ilkmatris[z]
            z=z+1
            if z > (yüzeybölüm*yüzeysayisi)-1:
                break
    return a  
def emrehoca():
    t = turtle.Turtle()
    s = turtle.Screen()

    s.bgcolor('black')
    t.hideturtle()
    t.goto(0,-10)

    t.pensize(3)
    t.color('red')
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90,200)
    t.setheading(60)
    t.circle(-90,200)
    t.forward(178)
    t.end_fill()

    t.penup()
    t.goto(-100,130)
    t.pendown()
    t.color('white')
    t.write("EMRE HOCA",font=("Verdana",25,"bold"))

    t.penup()
    t.goto(-220,-180)
    t.pendown()
    t.color('white')
    t.write("",font=("Verdana",30,"bold"))

    turtle.done()
sayi1 = int(input("yüzey sayısı : "))
sayi2 = int(input("yüzey bölüm sayısı : "))
matris=matriskutusu(sayi1,sayi2)
print(matris.shape)
print("---MATRİSİNİZ HAZIR---")
while(1):
    cevap=input("1- Matrisinzi Görmek için\n2- Matris üzerinde arama yapmak için\n3- Süpriz için\n4- Çıkmak için\nTUŞLARINI KULLANINIZ: ")
    if cevap == "1":
        print("Matrisiniz Aşağdaki Gibidir")
        print("___________________________\n")
        print(matris)
        print("___________________________")
        continue
    
    elif cevap =="2" :
        sütun=int(input("SÜTUN: "))
        satır=int(input("SATIR:  "))
        print(f"--------------------  {sütun}.sütun {satır}.satırdaki sayınız: {matris[satır-1,sütun-1]}  --------------------")
        continue
    elif cevap=="3":
        emrehoca()
        continue
    elif cevap== "4":
        print("******************İYİ DERSLER******************")
        break

