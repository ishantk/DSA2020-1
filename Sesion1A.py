"""
    DATA STRUCTURE
    Problem : Create a PlayList of Songs

    data associated with Song
    title, artist, duration

    Solution
        song1 <--> song2 <--> song3

"""
# OOPS Approach
class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.previous = None

    def showSong(self):
        print("{}\t{}\t{}".format(self.title, self.artist, self.duration))


s1 = Song("1. Ek Diamond", "Meet Bros", 3.25)
s2 = Song("2. Nindra", "Ikka", 4.25)
s3 = Song("3. Na Ja Tu", "Sukriti", 5.12)
s4 = Song("4. Suno Na", "Badhah", 4.11)
s5 = Song("5. Kamal", "Sukhvir", 6.77)

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
print("s5:", s5)

# Self Referential Linking

s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = s1

s1.previous = s5
s2.previous = s1
s3.previous = s2
s4.previous = s3
s5.previous = s4

# s1.showSong()
# s1.next.showSong()
# s1.previous.showSong()

print(">> PlayList Order -> First to Last")

temp = None
temp = s1

while temp.next != s1:
    temp.showSong()
    temp = temp.next

temp.showSong()

print(">> PlayList Order -> Last to First")

temp = s5
while temp.previous != s5:
    temp.showSong()
    temp = temp.previous
temp.showSong()

# How can this be managed in less than linear may be logarithmic






