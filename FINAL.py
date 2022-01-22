from router import *

#INPUT FROM THE USER
file = "test_10_equal.csv"

#MODE: JUST LEAVE AS N
mode = "N"
rout = router(file, mode)

#CALLS ON THE ROUTER TO DO PARRALEMISM
rout.routeCalc()

# ==============================================================================
# CODE FOR EXTRACTING Local Sorting Facilites [plasticObjects]
# ==============================================================================
rout.getLocalSort()

# ==============================================================================
# CODE OF EXTRACTING Regional Sorting Facilities [plasticObjects]
# ==============================================================================
rout.getRegionalSort()

# ==============================================================================
# Code FOR EXTRACTING Regional Recycling Facilities [plasticObjects]
# ==============================================================================
rout.getRegionalRec()

# ==============================================================================
# CODE FOR EXTRACTING FINAL DESTINATION ROUTE. [plasticObjects]
# ==============================================================================
master = rout.getMaster()
for item in master:
    print(item.getObjectType(), item.getLatCord(), item.getLongCord())