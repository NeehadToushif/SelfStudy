num_sub = (input("enter number of subjects (max 12)"))
# num_sub = 3 #uncomment for testing
if not num_sub:
    print("No subjects entered")
    exit(1)
else:
    num_sub = int(num_sub)
total = num_sub * 100
passpercent = 40
if num_sub > 12:
    print("too many subjects")
    exit(1)

subject_mark = {
    # uncomment for testing
    # "a":50,
    # "b":50,
    # "c":50
}

i = 0
while i < num_sub:
    try:
        _input = input("enter subject=mark\n").replace(' ','')
        sub,mark = _input.split('=')
        if mark=='':
            mark = 0
        subject_mark[sub] = float(mark)
        i+=1
    except Exception :
        print(" enter in the format subject = mark")


print(subject_mark)
aquired_total = 0

def compute(sub_mark,aq_total):
    for sub,mark in sub_mark.items():
        aq_total = aq_total + mark
        print(f"subject : {sub} \t mark : {mark}")
    avg = aq_total / num_sub
    percent = (aq_total/total) * 100
    _pass = "PASS" if percent > passpercent  else "FAILED"
    print(f"Total : {aq_total} \t Average : {avg} \t Percentage : {percent}% \nYou {_pass}")

compute(subject_mark,aquired_total)