import lyrics_scraper

class Gatherer():

    def __init__(self):
        self.file_list = []

    def setup(self):
        ending = "_songlist.txt"
        with open("master_list.txt") as f:
            for line in f:
                print(f.readlines())
                  #base = f.readline()
        #         file_name = base + ending
        #         self.file_list.append(file_name)
        # print(self.file_list)






if __name__ == "__main__":
    gatherer = Gatherer()
    gatherer.setup()
