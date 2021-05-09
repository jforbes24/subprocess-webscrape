import os
import subprocess
import multiprocessing
import time

# start timer
startTime = time.time()

# full directory
workflows = ["C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\Bathroom\\bs4 webScrape DIY Bathroom.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\BuildingSupplies\\bs4 webScrape DIY BuildSupplies.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\ElecSecur\\bs4 webScrape DIY elecSecur.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\Flooring\\bs4 webScrape DIY floorsTiles.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\Hardware\\bs4 webScrape DIY hardware.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\HeatPlumb\\bs4 webScrape DIY heatPlumb.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\HomeBed\\bs4 webScrape DIY homeBed.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\Kitchen\\bs4 webScrape DIY Kitchen.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\Lighting\\bs4 webScrape DIY lighting.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\OutdoorGarden\\bs4 webScrape DIY outdoorGarden.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\PaintDeco\\bs4 webScrape DIY paintDeco.py",
             "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\ToolsEquip\\bs4 webScrape DIY toolsEquip.py"
             ]

processes = []
for file in workflows:
    p = subprocess.Popen(['python', file])
    processes.append(p)

while processes:
    for p in processes:
        if p.poll() is not None:
            processes.remove(p)
            print('{} done, status {}'.format(p.args, p.returncode))
            break
    

print('DIY categories complete')
endTime = time.time()
print('Took %s seconds to run.' % round(endTime - startTime))


"""

# scrapeList
directory = "C:\\Users\\forbej06\\OneDrive - Kingfisher PLC\\dev\\Range\\B&Q\\"

scrapes = ["Bathroom\\bs4 webScrape DIY Bathroom.py",
           "BuildingSupplies\\bs4 webScrape DIY BuildSupplies.py",
           "ElecSecur\\bs4 webScrape DIY elecSecur.py",
           "Flooring\\bs4 webScrape DIY floorsTiles.py"]


# partial directory

scrapes = ["Bathroom\\bs4 webScrape DIY Bathroom.py",
           "BuildingSupplies\\bs4 webScrape DIY BuildSupplies.py",
           "ElecSecur\\bs4 webScrape DIY elecSecur.py",
           "Flooring\\bs4 webScrape DIY floorsTiles.py",
           "Hardware\\bs4 webScrape DIY hardware.py",
           "HeatPlumb\\bs4 webScrape DIY heatPlumb.py",
           "HomeBed\\bs4 webScrape DIY homeBed.py",
           "Kitchen\\bs4 webScrape DIY Kitchen.py",
           "Lighting\\bs4 webScrape DIY lighting.py",
           "OutdoorGarden\\bs4 webScrape DIY outdoorGarden.py",
           "PaintDeco\\bs4 webScrape DIY paintDeco.py",
           "ToolsEquip\\bs4 webScrape DIY toolsEquip.py"
           ]
"""

