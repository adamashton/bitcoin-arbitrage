from .observer import Observer
import config

class CSVLogger(Observer):
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc, weighted_buyprice, weighted_sellprice):
        with open(config.csv_filename, "a") as csv:
            csv.write("%s,buy,%f,%.4f,%s,sell,%f,%.4f\n" % (kask, buyprice, volume, kbid, sellprice, volume))
