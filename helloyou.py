

from asyncio import sleep
from multiprocessing.context import set_spawning_popen


def intro(): 
    print("je word wakker van een kleine middag dutje... is wat je dacht het is al avond\n")
    print("je besluit een nachtwandeling te maken maar komt een anderman tegen\n")
    enderman = input("Kijk je de anderman aan? Ja of Nee\n")
    if enderman== "ja":
        print("warp sounds")
        stukje2()
    elif enderman== "nee":
        print("je gaat verder met je wandeling en je komt veilig thuis")
        einde1()
    
    else:
        print("non valid option")
        intro()

def stukje2():
    print("je keek de anderman aan en werd zo duizelig dat je vlouw viel...\nje belanden in een trans en kreeg allemaal visioenen van andere werelden sommige 2d sommige 3d soms lijkt het echt en soms lijkt het wel pixel achtig...?\n")
    portaal = input("Je word wakker voor een paarse portaal en bent nieuwschierig wat er aan de andere kant is\n stap je er in ja of nee?\n")
    
    if portaal== "ja":
        stukje4()
    elif portaal== "nee":
        print("je bent erg in de war maar ongedierd, je besluit naar huis te gaan om te avond eten...\n")
    else:
        print("non valid option\n")
        stukje2()

def stukje3():
    poging = input("je komt thuis en doet de deur open.\nOpeens staat de anderman er en hij probeerd je te ontvoeren\nblijf je in shol of vecht je terug?\n")
    if poging== "shok":
        failed()
    elif poging== "vecht":
        failed()
    else:
        print("non valid option")
        stukje3()

def eind2():
    eindkeuz = input("dit is het einde wil je stoppen of opieuw?\n")
    if eindkeuz== "stoppen":
        quit()
    elif eindkeuz== "opnieuw":
        intro()
    else:
        print("non valid option")
        eind2()

def stukje4():
    print("gaat het portal in en weer krijg je visioenen maar deze keer van je eigen wereld...\nje ziet een soort draak maar paarse ogen die naar je toe vliegt\vlak voordat hij je te pakken heb schrik je wakker door een luide brul...\n")
    print("je ziet een hele grote schildpad met allemaal stekels op zijn rug en een man in een groene pak die mario roept.\nheeft hij het tegen jou?\n'MARIO HELP SNEL SPRING NU OP DIE KNOP NUUU'\n")
    mario = input("je weet niet wat er gaande is. spring je op de knop of niet?\n")
    if mario== "ja":
        print("je springt op de knop en de vloer onder de schildpad verdwijnt\nluige bedankt je maar jij vraagt waar je bent en wat het allemaal is\n luigi weet dat jij de uitverkorne bent en zegt\n'volg mij'")
        stukje6()
    elif mario== "nee":
        print("Je springt niet in de knop maar daardoor wint bowser en verbrand hij jou en luigi levend\n")
        eind2
    
    else:
        print("non valid option")
        stukje4()

def monk1():
    print("oh nee de monk is boos en gaat je vermorden je hebt de verkeerde keuze gemaakt\n")
    eind2()


def stukje6():
    print("je gaat samen met luigi en krijgt de complete mario lore uitgelegt in een visieon en je hoort een vage stem zeggen\n'je hebt je eerste wereld gered'\n")
    print("je word wakker maar deze keer in een hele andere wereld. je probeert naar link of rechts te lopen maar dat lukt niet...\n je bent in een 2d wereld beland, netzoals de game die je thuis hebt terraria.\n")
    print("je ziet een oude man staan hij lijkt op een soort monk, hij vraagt om een gunst.'wil jij 20 hout en 5 vissen voor mij halen op de markt?\n'")
    monk = input("wil jij de quest doen?")
    if monk== "ja":
        print("je haalt de spullen en brengt alles naar die monk.\n'bedankt steve, ik heb ook iets voor jou'")
        print("*steve? hoe weet hij mijn echte naam? die heb ik nooit tegen heb gezegt...*\n")
        stukje7()

    elif monk== "nee": 
        print("'JIJ DWAAS WAAROM WIL JE MIJ NIET HELPEN'")
        monk1()
    else:
        print("non valid option")
        stukje6()

def stukje7():
    print("de monk opent een portaal")
    portaal = input("ga je in het portaal ja of nee?\n")
    if portaal== "ja":
        print("weer krijg je visieoenen over de zelfde draak maar nu maakt hij chaos in andere werelden en maakt hij alles kapot en dood\n")
        print("ook weer kijg je de hele lore van terarria uitgelegt\n")
        stukje13()
    elif portaal== "nee":
        print("je wilt dit niet meer en hebt de hoop opgegeven je accepteerd je lot en blijft in terraria leven voor altijd")
        innerpeace()
    else:
        print("non valid option")
        stukje7()

def innerpeace():
    print("10 jaar later...")
    print("je komt het portaal weer tegen toen je een nachtwandeling ging maken je twijfelt of je er in gaat of niet\n je hoort de stem van de monk weer\n'DIT IS JE LAATSTE KANSSSS' ")
    tochwel = input("ga je toch te portal in of niet?")
    if tochwel== "ja":
        print("weer krijg je visieoenen over de zelfde draak maar nu maakt hij chaos in andere werelden en maakt hij alles kapot en dood\n")
        print("ook weer kijg je de hele lore van terarria uitgelegt\n")
        stukje13()
    elif tochwel== "nee":
        print("je hoort de monk weer\n'DIT ZAL DE WERELD JOU NIET VERGEVEN'")
        eind2()
    else:
        print("non valid option")
        innerpeace()

def stukje13():
    print("opeens zie je een soort zombie voor je staan. je schrikt wakker en kijkt om je heen")
    print("je bent in fps game beland met allemaal zombies om je heen.")
    zombie = input("je bent omringt door zombies ga je vechten of rennen?")
    if zombie== "vechten":
        print("de zombies waren met teveel en je word levend opgegeten")
        eind2()
    elif zombie== "rennen":
        print("je worstelt je door de zombies heen, valt een paar keer maar het lukt je om weg te komen.\nje ziet een garage,rent erin en en doet de deur dicht.")

    else:
        print("non valid option")
        stukje13()
    
def stukje14():
    print("je bent voor nu veilig in de garage, maar opeens hoor je de monk weer.\n'uitverkorne... ik zie dat je de goede keuze hebt gemaakt om het portaal in te gaan.\nik snap dat dit veel is om te begrijpen en daarom zal ik je helpen. kies en wapen en vermoord alle zombies.\n EN SCHIET OP MINECRAFT HEEFT JE NODIG'")
    wapen = input("je hebt de keuzen tussen en pistool en een shotgun wat kies je?")
    if wapen== "shotgun":
        print("je gaat naar buiten en probeert alle zombies te vermoorden")
        print("het gaat goed! nog maar een paar te gaan.")
        print("ohnee je shotgun had teweinig kogels en je bent out of ammo. de zombies hebben je te pakken en je word levend opgegeten")
        eind2()
    elif wapen== "pistool":
        print("je gaat naar buiten en probeert all gaan.")
        print("oe zombies te vermoorden")
        print("het gaat goed! nog maar een paar temdat je het pistool hebt gekozen heb je net genoeg kogels om alle zombies te vermoorden en weer hoor je de monk")
        print("'GOED BEZIG... weer een wereld gered. je bent bijna klaar voor de eindstrijd'")
        print("*eindstrijd? zeg mij niet dat ik de draak moet verslaan? dat kan ik toch nooit...*")
        stukje15()
    else:
        print("non valid option")
        stukje14()

def stukje15():
    print("je krijgt meer en meer visioenen")
    print("choose your character, healer or tank")
    choose = input("speel je tank of healer?")
    if choose== "tank":
        print("je kiest de tank reinhard maar je weet niet wat je moet doen en hoe alles werkt... weer hoor je de monk\n")
        print("GEBRUIK JE SHIELD")
        print("je bent in de war maar weet niet hoe je het moet gebruiken\n je team vote kickd je en je bent voor altijd in een zwart gat")
        eind2()
    elif choose== "healer":
        print("je wilt safe spelen en kiest healer, je weet alleen niet welke, weer hoor je de monk....")
        print("KIES LUCIO ")
        print("je kiest lucio maar je weet niet wat je moet doen, je rent achter een muur en blijft wachte tot het schieten voorbij is\n gelukkig door lucio zijn passive ability om te healen word je niet gekicked.")
    else:
        print("non valid option")
        stukje15()


def stukje16():
    print("het potje overwatch is klaar en weer heb je een wereld gered")
    print("je ziet een portaal en besluit in er in de tegaan, weer kijg je visioenen maar voor de gevoel duurt dit langer")
    print("de draak zit op een eiland te slapen met allemaal enderman om zich heen, ook zijn er meerdere pilaren met soort crystalen er op,")
    sleep(5)
    print("WAKKER  WORDEN SNELLLLLL")
    print("je word wakker\n")
    kist = input("je spawned voor een kist, pak je de boog en bijl. of zwaard en schild\n")
    if kist== "boog en bijl":
        print("je vecht hard maar je weet niet wat je moet doen, de draak krijgt steeds zijn HP terug.")
        stukje17()
    elif kist== "zwaard en schild":
        print("je vecht hard maar omdat je geen range aanvallen hebt ren je terug nnaar de kist om nieuwe dingen te pakken")
        stukje16()
    else:
        print("non valid option")
        stukje16()

def stukje17():
    print("'SCHIET DE CRYSTALEN'")
    print("je luistert naar de monk en probeerd de crystalen stuk te schieten")
    print("het gaat goed tot de draak een vuurbal op je afschiet, je leven schiet voorbij je denkt dat je dood gaat maar dan...")
    sleep(5)
    print("de monk komt terug niet als geest maar als persoon, hij springt voor de vuurbal en red je leven... ")
    print("'hoest bloed'.... ik ga dood, dat is een feit. maar jij kan het universum redden. doe je best en versla de draak")
    print("Uit woede schiet je alle crystallen in 1x kapot schit de draak in zijn vleugels en hij zit nu voor voor je op de grond")

def stukjelast():
    print("hij zit voor je wat ga je met hem doen")
    print("je weet dat hij de kracht om door universums te reisen net zoals jij dus je kan veel van hem leren")
    draak = input("1: tem de draak\n2:dood de draak")
    if draak=="1":
        eind3()
    elif draak=="2":
        eind4
    else:
        print("non valid option")
        stukjelast()
def eind3():
    print("je temt de draak en nu gaan jullie samen op reis om meer werelden te reden van het kwaad")
    sleep(5)
    print("je hebt de game uit gespeeld met een goed einde, je keert terug naar je huis met de draak en gaat samen trainen om het universum te redden")
    tem = input("wil je opnieuw spelen of stoppen")
    if tem== "opnieuw":
        intro()
    elif tem== "stoppen":
        print("bedank voor het spelen")
        sleep(3)
        quit()
def eind4():
    print("je vermoord de draak uit woede, zijn kop hak je af in 1 slag en neem je mee")
    print("je hebt de game uit gespeeld met een goed einde, je keert terug naar je huis om vredig te leven")
    sleep(5)
    tem = input("wil je opnieuw spelen of stoppen?")
    if tem== "opnieuw":
        intro()
    elif tem== "stoppen":
        print("bedank voor het spelen")
        sleep(3)
        quit()





    

    
    
    
def failed():
        print("het is je niet gelukt\nde enderman pakt je en gooid je het portaal in")
        stukje4()

        
def einde1():
    print("je komt thuis en gaat verder met je normalen leven\n ")
    eindkeuze = input("dit is het einde wil je stoppen of opieuw?\n")
    if eindkeuze== "stoppen":
        print("bedankt voor het spelen")
        quit()
    
    elif eindkeuze== "opnieuw":
        intro()
    else:
        print("non valid option")


        


        

while True:
    startgame = input("kan jij alle games verslaan en terug keren naar je eigen wereld?\n")
    if startgame== "ja":
        print("Oke let's go\n")
        intro()
    elif startgame== "nee":
        print("Dan niet")
        quit()
    else:
        print("non valid option")
