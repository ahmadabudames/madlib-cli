import re

print("welcome to play the game")


def read_template(path: str)->str:
    with open(path,'r') as file:
        inside_file = file.read()
    return  inside_file.strip()

def parse_template(inside_file):
    analyze = re.findall(r'\{(.*?)\}',inside_file)
    for obj in analyze:
        inside_file = inside_file.replace(obj,'',1)
        # print(inside_file)
    return inside_file,tuple(analyze)

def question(asking):
    answers=[]
    for index in asking:
        result=input(f"can i ask you to know about me {index} ?")
        answers.append(result)
    return answers    

def merge(assert_answer,answers):
    print(assert_answer)
    fresh_txt=assert_answer.format(*answers)
    print(fresh_txt)
    return fresh_txt
     


         

  
