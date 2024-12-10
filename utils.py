def read_help():
    with open('routine/help.md', 'r') as f:
        content = f.read()
    return content

def calculate_day(day_text:str):
    days = [ "sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    day_text = day_text.lower().strip()
    for i, day in enumerate(days):
        if day_text.startswith(day):
            return i+1

    import datetime
    if day_text.startswith('tm') or day_text.startswith('tm'):
        return datetime.datetime.today().weekday() + 3
    if day_text.startswith('y'):
        return datetime.datetime.today().weekday() + 1
    # default is today
    return datetime.datetime.today().weekday() + 2
        
    
if __name__ == "__main__":
    print(calculate_day('tue'))
    print(calculate_day('tm'))
    print(calculate_day('y'))
    print(calculate_day(''))
    