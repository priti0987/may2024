import time

def stopwatch():
    input("Press Enter to start stopwatch")
    start_time = time.time()

    try:
        while True:
            elapse_time = time.time()-start_time
            mins, secs = divmod(elapse_time,60)
            hours, mins =divmod(mins,60)
            time_format = "{:02}:{:02}:{:02}".format(int(hours),int(mins),int(secs))

            print("\rTime Elapsed:{}".format(time_format),end="")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    #catch ctrl +c to stop

    finally:
        print("\n Stopwatch stopped. TOtal time elapsed : {}",format(time_format))

stopwatch()