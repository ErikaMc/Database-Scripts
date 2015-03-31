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

def popSongs(a, art_mbid, tracks, cursor):
        for track in tracks[:25]:
                try:
                        tname  = track.item.get_name()
                        t = network.get_track(a, tname)
                        tid = t.get_id()
                        tdur = t.get_duration()
                        tcount = t.get_playcount()
                        commander2 = ("REPLACE INTO music_song_no_album \n"
                                    "VALUES ('%s',\"%s\",'%s','%s','%s');" % (tid, tname, tdur, tcount, art_mbid))
                        print("Executing " + tname)
                        cursor.execute(commander2)
                except:
                        pass

for a in args:
        art = network.get_artist(a)
        art_mbid = art.get_mbid()
        tracks = art.get_top_tracks()
        popSongs(a, art_mbid, tracks, cursor)

db.commit()
db.close()
