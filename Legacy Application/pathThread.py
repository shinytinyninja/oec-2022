import threading
import math

class pathThread(threading.Thread):
    def __init__(self, threadID, current, listOfDests):
        super(pathThread, self).__init__()
        self.threadID = threadID
        self.current = current
        self.listOfDests = listOfDests
        self.bestQOR = ()
        
    def run(self): 
        x1_lat, y1_lon = self.current.getLatCord(), self.current.getLongCord()
        
        for dest in self.listOfDests:  
            x2_lat, y2_lon = dest.getLatCord(), dest.getLongCord()
        
            R = 6371
            
            latavg = (int(x1_lat) + int(x2_lat))/2

            x1 = R * int(y1_lon) * math.cos(latavg)
            y1 = R * int(x1_lat)

            x2 = R * int(y2_lon) * math.cos(latavg)
            y2 = R * int(x2_lat)

            hypo = math.hypot(abs(x1-x2), abs(y1-y2))/1000
            
            riskLevel = float(dest.getRisk()) if float(dest.getRisk()) > 0 else 1
            QOR = float(hypo) * riskLevel
            
            if len(self.bestQOR) == 0:
                self.bestQOR = (dest, QOR)
            elif (QOR < self.bestQOR[1]):
                self.bestQOR = (dest, QOR)
    
    def getWinner(self):
        return self.bestQOR[0]
    
        
        