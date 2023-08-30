class musicNode:
    def __init__(self,SongName,artist,releaseDate,tags):
        self.SongName=SongName
        self.artist=artist
        self.releasedDate=releaseDate
        self.tags=tags
        self.next=None

class musicList:
    def __init__(self):
        self.head=None
    
    def InsertSong(self,SongName,artist,releaseDate,tags):
        newSong=musicNode(SongName,artist,releaseDate,tags)
        if self.head is None:
            self.head=newSong
            print(f"inserted {newSong.SongName} successfully to head")
            return
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newSong
            print(f"inserted {newSong.SongName} successfully to the end of list")
            return
    
    def displaySong(self):
        if self.head is None:
            print("empty")
            return
        n=self.head
        while n is not None:
            print({
                "songName":n.SongName,
                "artist": n.artist,
                "releaseDate":n.releasedDate,
                "tags":n.tags
            })
            n=n.next
        return
    def DeleteSong(self,songToDelete):
        if self.head is None:
            print("your List is empty! \n please add music before deleting")
            return
        elif self.head.songName is songToDelete:
            self.head=self.head.next

        else:
            n=self.head
            prevNode=None
            while n is not None:
                
                if n.SongName==songToDelete:
                    nextNode=n.next
                    break
                prevNode=n
                n=n.next
            prevNode.next=nextNode
            print(f"{songToDelete} is deleted")
            return
            

mysongList=musicList()
mysongList.InsertSong("Blinding Light","The Weekend",2020,["gym song","cool", "the weekend"])
mysongList.InsertSong("Faded","Alan Walker",2017,["cool","favorite","alone","memory"])
mysongList.InsertSong("Alone","Alan Walker",2017,["cool","favorite","alone","memory"])
mysongList.displaySong()
mysongList.DeleteSong("Faded")
mysongList.displaySong()
