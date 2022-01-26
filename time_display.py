import time


def format_total_time(total_time):
    print(total_time)
    hours, extra = divmod(total_time, 3600)
    mins, secs = divmod(extra, 60)
    message = "Process took "
    
    if total_time < 1:
        message = message + "%.0f milliseconds "%(total_time*1000)
    else:
        if hours:
            message = message + "%.0f hours "%(hours)
        if mins:
            message = message + "%.0f minutes "%(mins)
        if secs:
            message = message + "%.0f seconds "%(secs) if not hours and not mins else message + "and %.0f andseconds "%(secs)
    return message
    

def test_function(time_in_seconds):
    start = time.perf_counter()
    time.sleep(time_in_seconds)
    end = time.perf_counter()
    return end - start