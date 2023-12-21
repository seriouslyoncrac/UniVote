""" 
https://www.w3schools.com/python/gloss_python_date.asp
Threading allows the program to perform multiple functions at the same time
Similar to queuing in real life, queue dictates what action the program does first
"""
import time
import threading
import queue

def get_user_input(input_queue):
    try:
        user_input = input("\nEnter 1, 2, or 3: ")
        input_queue.put(user_input)
    except EOFError:
        pass

def run_timer():
    print("\nInputs won't be saved until after the wait period.")

    input_queue = queue.Queue()

    def timer_thread():
        for _ in range(30):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\nSignup timer expired.")
        input_queue.put(None)  # End of the input thread

    # Start the timer thread
    timer = threading.Thread(target=timer_thread)
    timer.start()

    try:
        # Get user input within the specified timeout
        user_input = None
        input_thread = threading.Thread(target=get_user_input, args=(input_queue,))
        input_thread.start()

        while timer.is_alive() and user_input not in ['1', '2', '3']:
            try:
                user_input = input_queue.get(timeout=1)
            except queue.Empty:
                pass

        # Check if the timer expired without valid input
        if not timer.is_alive():
            print("\nSignup timer expired. No valid input received.")
            # You can add your desired action when the timer expires without valid input here
        elif user_input in ['1', '2', '3']:
            print(f"\nUser input: {user_input}")
            # You can add your desired action when valid input is received here

    except KeyboardInterrupt:
        print("\nTimer stopped manually.")

    # Wait for the timer thread to finish
    timer.join()

# Run the timer
run_timer()
