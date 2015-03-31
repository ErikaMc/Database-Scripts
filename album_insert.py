import pylast
import MySQLdb


API_KEY = "f5ea3878617633c9b4dff93668a4bf5a"
API_SECRET = " b69f90e31587a4c2552542c81b33ae84"

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
    API_SECRET)

db = MySQLdb.connect(host="localhost", user="gsmp", passwd="gamera@1234", db="gsmp")
db.set_character_set('utf8mb4')
cursor = db.cursor()
cursor.execute('SET CHARACTER SET utf8mb4;')


args = ['Justin Bieber', 'Lady Gaga', 'Katy Perry', 'Rihanna', 'Taylor Swift', 'Britney Spears', 'Shakira', \
        'Justin Timberlake', 'Jennifer Lopez', 'Nicki Minaj', 'Bruno Mars', 'P!ink', 'Selena Gomez', 'Eminem', \
        'Deme Lovato', 'Adele', 'Alicia Keys', 'Chris Brown', 'One Direction', 'Miley Cyrus', 'Lil Wayne', \
        'Niall Horan', 'Snoop Dogg', 'Louis Tomlinson', 'Mariah Carey', 'Liam Payne', 'Coldplay', 'Wiz Khalifa', \
        'Pitbull', 'Avril Lavigne', 'Ashley Tisdale', 'Kanye West', 'Alejandro Sanz', 'Ricky Martin', 'David Guetta', \
        '50Cent', 'Beyonce', 'Ludacris', 'Usher', 'will.i.am', 'Paulina Rubio', 'Jessie J', 'Jessica Simpson', \
        'Trey Songz', 'Ed Sheeran', 'Jonas Brothers', 'Carly Rae Jepsen', 'Soulja Boy', 'Jason Mraz', 'Kelly Rowland', \
        'David Bisbal', 'Calle 13', 'Queen Latifah', 'LMFAO', 'Christina Aguilera', 'Cher', 'Lenny Kravitz', 'John Legend', \
        'Lily Allen', 'Run DMC', 'Adam Levine', 'Mary J. Blige', 'Sean Kingston', 'Big Sean', 'Cheryl Cole', 'T.I.', \
        'Kelly Clarkson', 'Mac Miller', 'LL COOL J', 'Chayanne', 'Ne-Yo', 'J. Cole', 'Miranada Cosgrove', 'Enrique Iglesias', \
        'Ke$ha']


#artist = network.get_artist("Taylor Swift")

def popAlbum(artist, art_mbid, albums, cursor):
        for album in albums:
                try:
                        name = album.item.get_name()
                        newa = network.get_album(name, artist)
                        id = newa.get_id()
                        commander = ("REPLACE INTO music_api_album \n"
                                   "VALUES ('%s','%s','%s','%s');" % (id, name, art_mbid, artist))
                        print("Executing " + commander)
                        cursor.execute(commander)
                        tracks = newa.get_tracks()
                        popSongs(art_mbid, id, tracks)
                except:
                        pass
                        
def popSongs(art_mbid, al_id, tracks):
        for track in tracks:
                try:
                        tname = track.get_name()
                        tid = track.get_id()
                        tdur = track.get_duration()
                        tcount = track.get_playcount()
                        commander2 = ("REPLACE INTO music_api_songs \n"
                                    "VALUES ('%s',\"%s\",'%s','%s','%s','%s');" % (tid, tname, tdur, tcount, al_id, art_mbid))
                        print("Executing " + commander2)
                        cursor.execute(commander2)
                except:
                        pass

for a in args:
        artist = network.get_artist(a)
        art_mbid = artist.get_mbid()
        albums = artist.get_top_albums()
        popAlbum(artist, art_mbid, albums, cursor)

db.commit()
db.close()
                        

