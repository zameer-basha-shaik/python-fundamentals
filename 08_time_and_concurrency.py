import datetime
import threading
import time

# Date/time example recovered and preserved
current_datetime = datetime.datetime.now()
print(current_datetime)

# Threading example from earlier practice

def walk_dog(first, last):
    time.sleep(1)
    print(f"Walking dog {first} {last} is done")


def taking_trash():
    time.sleep(0.5)
    print("Trash was dumped")


def collect_mail():
    time.sleep(0.2)
    print("Mail has been collected")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore2 = threading.Thread(target=taking_trash)
chore3 = threading.Thread(target=collect_mail)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")
