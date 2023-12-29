import g4f

def gpt():

    while True:

        msg={"role": "user", "content": "me"+str(input())}

        if msg["content"]=="exit()":
             break
        
        msgs=[]
        msgs.append(msg)

        res=g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msgs,
                stream=True
            )
        
        print("AI:",flush=True,end="")

        for message in res:
                print(message, flush=True, end='')

        print()

gpt()