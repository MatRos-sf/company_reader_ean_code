"""

"""
import company_db
import datetime
import cv2
from pyzbar.pyzbar import decode
import time

def how_many_people_working_now(data):
    """
    The functions showes who works now
    :param data: data with worker
    :return:
    """
    print('Now working:')
    for key in data:
        print(f"[{key}]\t[{data[key]}]")

    print(len(data))

def payoff(salary, seconds):
    #salary / 1h - 60 min ->1 min - 60s
    return round(seconds * round(salary/60/60, 2))

def reader(con, cur, date={}):
    """
    The function reader code
    :param con:
    :param cur:
    :param date:
    :return:
    """
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # 3- Width
    cap.set(4, 480)  # 4 - Height
    camera = True
    data_with_workers = date

    while camera == True:

        success, frame = cap.read()

        for code in decode(frame):
            n = str(code.data.decode('utf-8'))
            print(n)
            cur.execute('SELECT * FROM worker WHERE code=:ean', {"ean": n})
            worker = cur.fetchone()
            # if code is in database
            if worker:
                #if worker is working now
                if n in data_with_workers.keys():
                    #exist
                    time_start = data_with_workers[n]
                    time_end = datetime.datetime.now()
                    worked_time = (time_end - time_start).seconds
                    print(f"You worked: {worked_time}s")
                    print(f"You earned: {payoff(worker[2], worked_time)} PLN")
                    del data_with_workers[n]
                    time.sleep(5)
                else:
                    #no exist
                    data_with_workers[n] = datetime.datetime.now()
                    print("Have you nice day ; )")
                    time.sleep(5)


        cv2.imshow('Comapny-worker', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return data_with_workers

def main():

    con, cur = company_db.is_database()

    data = {}
    instruction = """
        [1] Read worker
        [2] Add worker 
        [3] Who is working now? 
        [4] All 
        [5] Search
        [q] exit 
    """
    while True:
        move = input(instruction)
        if move == '1':
            data = reader(con,cur,data)
        elif move == '2':
            company_db.add_workers(con, cur)
        elif move == '3':
            how_many_people_working_now(data)
        elif move == '4':
            company_db.all_data(con, cur)
        elif move == '5':
            s = input("Key word: ")
            company_db.search(con,cur, s)
        elif move == 'q':
            break


if __name__ == "__main__":
    main()
