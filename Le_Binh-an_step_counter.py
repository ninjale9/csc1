def steps_to_miles(steps):
    try :
        steps = int(steps)
        if steps < 0 :
            raise ValueError ("Exception: Negative Step Count Entered")
        else:
            miles = steps / 2000 
            return miles 
    except ValueError:
        raise ValueError("Execption: Non- Numeric Value Entered")

def main() :
    try : 
        steps = int(input("Please enter # of steps: "))
        miles_walked = steps_to_miles(steps)
        print(f"{miles_walked:.2f} miles ")
    except (ValueError,ValueError) as e: 
        print(e)
main()