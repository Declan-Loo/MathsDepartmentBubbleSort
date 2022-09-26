import random
import string
import urllib.request

def InitiailiseNames():
    #Inlitalise name array
    name_array= []
    # First names information
    url = 'https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt'
    for line in urllib.request.urlopen(url):
        line.decode('utf-8')
        if line != '\n':
            name_array.append(line.strip())
    return name_array

# Main bubble sort algorithm involving two parameters: the text file and the parameter
def MainBubbleSortAlgorithm(AccessData, Order):
    try:
        pre_sort_data = []
        #Checks if the data provided is a text-file
        print(AccessData[-3:])
        if AccessData[-3:] == 'txt':
            with open(AccessData,'r') as file:
                for line in file:
                    if line != '\n':
                        if (isinstance(line,int)) == True:
                            pre_sort_data.append(int(line.strip()))
                        elif (isinstance(line,float)) == True:
                            pre_sort_data.append(float(line.strip()))
                        else:
                            pre_sort_data.append(line.strip())
        else:
            for element in AccessData:
                if element.isdigit() == True: 
                    pre_sort_data.append(int(element))
                elif (isinstance(line,float)) == True:
                    pre_sort_data.append(float(element))
                else:
                    pre_sort_data.append(element)
                
        if Order.lower() in ['asc','ascending']:
            for i in range(len(pre_sort_data)):
                for j in range(len(pre_sort_data)-1):
                    if pre_sort_data[j] > pre_sort_data[j+1]:
                        temp = pre_sort_data[j+1]
                        pre_sort_data[j+1] = pre_sort_data[j]
                        pre_sort_data[j] = temp
                print(pre_sort_data)
            post_sort_data = [i for i in pre_sort_data]
        elif Order.lower() in ['desc','descending','dsc']:
            for i in range(len(pre_sort_data)):
                for j in range(len(pre_sort_data)-1):
                    if pre_sort_data[j] < pre_sort_data[j+1]:
                        temp = pre_sort_data[j+1]
                        pre_sort_data[j+1] = pre_sort_data[j]
                        pre_sort_data[j] = temp
                print(pre_sort_data)
            post_sort_data = [i for i in pre_sort_data]
        with open('Result.txt','w') as file:
            file.write('\n'.join(str(data) for data in post_sort_data))
            
        return post_sort_data
    except:
        print("Please re-run the code again.")


#EntryFile = input("Please enter text-file: ")
#Order = input("Please enter order (asc or desc) for the data to be sorted into: ")
#while Order not in ['asc','desc', 'ascending', 'descending']:
#    Order = input("Please enter order (asc or desc) for the data to be sorted into: ")
#print(MainBubbleSortAlgorithm(EntryFile,Order))

def GenerateData():
    generated_array = []
    #Asks user if user wants data generated to be numbers or characters?
    choice = input("Numbers or Characters?: ")
    while choice.lower() not in ['numbers','n','number','num','characters','character','char','c']:
        choice = input("Numbers or Characters?: ")
    if choice.lower() in ["numbers","n","number","num"]:
        num_array = []
        numrange = int(input("Please input your range (0 to n): "))
        count = int(input("Please indicate the amount of numbers in your data: "))
        for i in range(count):
            num_array.append(random.randint(0,numrange))
        with open('GeneratedData.txt','w') as file:
            file.write('\n'.join(str(data) for data in num_array))
        generated_array = num_array
    else:
        names_or_random = input("Do you want names, letters or random characters? (n/l/r): ")
        while names_or_random.lower() not in ['n','l','r','numbers','number','letter','letters','random','random characters']:
            names_or_random = input("Do you want names, letters or random characters? (n/l/r): ")
        #Adds random characters into Generated Data file
        if names_or_random in ['r','random','random characters']:
            char_array = []
            charrange = int(input("Please input the max number of characters per element in data: "))
            count = int(input("Please indicate the number of characters in your data: "))
            for i in range(count):
                char_array.append(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(charrange)))
            with open('GeneratedData.txt','w') as file:
                file.write('\n'.join(str(data) for data in char_array))
            generated_array = char_array
        #Alternatively, adds letters into Generated Data
        elif names_or_random in ['l','letter','letters']:
            letter_array = []
            letter_range = int(input("Please input the number of letters in your data: "))
            for i in range(letter_range):
                letter_array.append(''.join(random.choice(string.ascii_uppercase)))
            with open('GeneratedData.txt','w') as file:
                file.write('\n'.join(str(data) for data in letter_array))
            generated_array = letter_array
        #Otherwise, adds names into generated data
        else:
            no_names = int(input("Please input the number of names in your data: "))
            full_name_list = InitiailiseNames()
            name_array=[]
            count = 1
            while count <= no_names:
                name = random.choice(full_name_list)
                if name not in full_name_list:
                    name_array.append(name)
                    count += 1
            with open('GeneratedData.txt','w') as file:
                file.write('\n'.join(str(data) for data in name_array))
            generated_array = name_array
    return generated_array

def ExercisesAndSolutions(*args):
    # The exercise_dict will have the key as the question and the value as pre-sorted data (index 0) and the result of the bubble sort/merge sort (index 1)
    questions = int(input("How many questions do you want to generate?: "))
    files_or_random_generated = input("Do you want to use files or random generated data?: ")
    exercise_dict = {}
    order = ['ASC','DESC']
    if files_or_random_generated in ['files','f']:
        for num ,count in enumerate(args):
            exercise_data = []
            with open(count,'r') as file:
                for line in file:
                    if line != '\n':
                        exercise_data.append(line.strip())
            choice = random.choice(order).lower()
            exercise_dict[num+1] = [exercise_data,MainBubbleSortAlgorithm(exercise_data,choice),choice]
    
    elif files_or_random_generated in ['random_generated','random','random generated','generate','r']:
        for i in range(questions):
            exercise
        
    with open('Questions.txt','w') as file:
        for key, value in exercise_dict.items():
            if value[2] == 'desc':
                file.write('Question '+str(key)+':\nPlease sort the following data in descending order:\n'+str(value[0])+'\nSolution:\n\n')
            else:
                file.write('Question '+str(key)+':\nPlease sort the following data in ascending order:\n'+str(value[0])+'\nSolution:\n\n')
    

    return exercise_dict

GenerateData()
print(ExercisesAndSolutions('GeneratedData.txt'))

def SaveSolutions():
    pass

def main():
    pass

def QuickSortAlgorithm():
    pass
