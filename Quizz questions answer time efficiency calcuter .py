import sqlite3
from datetime import datetime
import time
import sys
import msvcrt

def stopwatch():
    print("Press Space to pause/resume the stopwatch, and Enter to stop.")
    start_time = time.time()
    paused_time = 0
    paused = False
    total_elapsed_time = 0

    while True:
        if not paused:
            elapsed_time = int(time.time() - start_time - paused_time)
            sys.stdout.write(f"\rElapsed time: {elapsed_time} seconds")
            sys.stdout.flush()

        # Check for key press
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':  # Space key to pause/resume
                paused = not paused
                if paused:
                    pause_start = time.time()
                    total_elapsed_time = elapsed_time
                    sys.stdout.write(f"\rStopwatch paused at {total_elapsed_time} seconds.            ")
                else:
                    paused_time += time.time() - pause_start
                    sys.stdout.write("\rStopwatch resumed.           ")
            elif key == b'\r':  # Enter key to stop
                total_elapsed_time = elapsed_time
                print(f"\rStopwatch stopped at {total_elapsed_time} seconds.           ")
                return total_elapsed_time
                # break

        time.sleep(0.1)  # Small delay to reduce CPU usage



def create_score_table():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    
    # Create the table
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    score_seconds INTEGER,
                    datetime TEXT)''')
    
    conn.commit()
    conn.close()

# Function to insert a score into the table
def insert_score(score_seconds):
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    
    # Get current date-time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Insert data into the table
    cursor.execute('''INSERT INTO scores (score_seconds, datetime)
                    VALUES (?, ?)''', (score_seconds, current_datetime))
    
    conn.commit()
    conn.close()
def output():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    Query = "SELECT * FROM SCORES ORDER BY id DESC LIMIT 7"
    cursor.execute(Query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Data does not exist: Note - first solve some qestions.\n")
        exit()
    avg = 0
    for i in range(len(rows)):
        avg = rows[i][1] + avg
    avg = avg/len(rows)
    print(f"Average time taken by last total {len(rows)} question is : {avg} seconds.\n")

    conn.close()
def deletedb():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scores")
    print("[[ ALL ROWS DATA DELETED... ]]\n")
    # cursor.execute("SELECT * FroM SCORES")
    # rows = cursor.fetchall()
    # print(rows)
    conn.commit()



if __name__ == "__main__":
    # Create the score table (run only once)
    create_score_table()
    
    while True:
        usrinp = int(input("""What do you want to do:
            1. solve questions
            2. clean old database
            3. Exit   """))
        if usrinp == 1:
            print("Press 'ESC' to get Main Menu and 'Enter' to start Timer. \n-> ",end='')
            while True:
                
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    # Decode the byte string to a string representation for easier handling
                    # key_str = key.decode('utf-8', errors='ignore')
                
                
                    # Check for specific keys
                    if key == b'\x1b':  # Escape key
                        print("Escape key pressed. Exiting.")
                        # usrinp = 3
                        break
                    total_elapsed_time = stopwatch()
                    insert_score(total_elapsed_time)
                    print(f"-> {total_elapsed_time} Score saved...")
                    print()
                    output()
                    print("Press 'ESC' to get Main Menu and 'Enter' to start Timer again.\n-> ",end='')

                
        elif usrinp == 2:
            deletedb()
            usrinp = 3
        elif usrinp == 3:
            break
        else:
            print("wrong input Break")
            break
    
    # print()
    output()