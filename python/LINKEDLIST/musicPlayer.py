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
        if self.searchSong(songToDelete):
            if self.head is None:
                print("your List is empty! \n please add music before deleting")
                return
            elif self.head.SongName is songToDelete:
                self.head=self.head.next
                print(f"{songToDelete} is deleted")
                return

            elif self.head.SongName is not songToDelete:
                n=self.head
                prevNode=None
                nextNode=None
                while n is not None:
                
                    if n.SongName==songToDelete:
                        nextNode=n.next
                        print(f"{songToDelete} is deleted")
                        break
                    prevNode=n
                    n=n.next
                prevNode.next=nextNode
            
                return
            else:
                print(f"{songToDelete} not found in list")
                return
    def searchSong(self,data):
        n=self.head
        if self.head is None:
            print("list is  empty")
            return False
        else:
            while n is not None:
                if n.SongName==data:
                    print(f"{data} found in the list")
                    return True
                else:
                    n=n.next
            print(f"{data} not found")
        
            

mysongList=musicList()
mysongList.InsertSong("Blinding Light","The Weekend",2020,["gym song","cool", "the weekend"])
mysongList.InsertSong("Faded","Alan Walker",2017,["cool","favorite","alone","memory"])
mysongList.InsertSong("Alone","Alan Walker",2017,["cool","favorite","alone","memory"])
mysongList.displaySong()

