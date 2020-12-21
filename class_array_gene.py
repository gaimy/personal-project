from PIL import Image, ImageDraw
import random
import time

test_classes = 200
cls_image = list(range(test_classes))
cls_chairs = list(range(test_classes))

max_gen=99999
count=0

def draw(cls_chairs):
    for chairs in cls_chairs:
        i = cls_chairs.index(chairs)
        ImageDraw.Draw(cls_image[i]).rectangle((0,0,150,150),fill='white')
        for chair in chairs:
            ImageDraw.Draw(cls_image[i]).rectangle((chair[0]-10,chair[1]-5,chair[0]+10,chair[1]+5),fill='red')
        cls_image[i].save('genes\cl'+str(i)+'.gif')

def fitness(chairs):
    score = 0
    for chair in chairs:
        # print(chair)
        dist = 9999999
        other_chairs = chairs[:]
        other_chairs.remove(chair)
        for other_chair in other_chairs:
            disti = (other_chair[0]-chair[0])**2+(other_chair[1]-chair[1])**2
            if disti<dist:
                dist=disti
            
        score += dist
        if dist<500:
            score -=500

    return score

def crossover(chairs1,chairs2,count):
    homo_chairs=[]
    schairs1=[]
    schairs2=[]
    cro_chairs=[]
    cro_cls_chairs=[]
    #relative x,y order
    for i in range(5):
        schairs1.append(sorted(chairs1, key=lambda x: x[0])[6*i:6*i+6])
        schairs1[i]=sorted(schairs1[i], key=lambda x: x[1])
        schairs2.append(sorted(chairs2, key=lambda x: x[0])[6*i:6*i+6])
        schairs2[i]=sorted(schairs2[i], key=lambda x: x[1])
    #homologous gene combi
    for i in range(5):
        for j in range(6):
            homo_chairs.insert(6*i+j,[schairs1[i][j],schairs2[i][j]])

    #crossover
    for i in range(count):
        cro_chairs=[]
        for j in range(len(homo_chairs)):
            cro_chairs.insert(j,random.sample(homo_chairs[j],1)[0])
        cro_cls_chairs.append(cro_chairs)

    return cro_cls_chairs

def mutate(chairs,mutation_count,option):
    mutation_chairs = chairs[:]
    # print(len(chairs))
    if mutation_count>len(chairs):
        mutation_count=len(chairs)
    for i in random.sample(chairs,mutation_count):
        j=chairs.index(i)
        if type(option)==int:
            i = [i[0]+random.randint(-option,option),i[1]+random.randint(-option,option)]
            i[0] = 10 if i[0]<10 else i[0]
            i[1] = 10 if i[1]<10 else i[1]
            i[0] = 139 if i[0]>139 else i[0]
            i[1] = 139 if i[1]>139 else i[1]
        elif option=='random':
            i = [random.randint(10,139),random.randint(10,139)]
        mutation_chairs[j]=i

    
    return mutation_chairs

#initialize
for i in range(test_classes):
    chairs = list(range(30))
    chairs = mutate(chairs,30,'random')
    cls_chairs[i]=chairs

    cls_image[i]=Image.new('RGBA',(150,150),'white')

draw(cls_chairs)

while count<max_gen:
    
    fittest=[]
    #oder best fitness
    for chairs in cls_chairs:
        fittest.append([chairs,fitness(chairs)])
    sfittest = sorted(fittest, key=lambda x: x[1], reverse=True)
    print("fittest score : "+str(sfittest[0][1]))

    #target score : 15000
    # if sfittest[0][1]>15000:
        # max_gen=0
    
    #draw
    for chairs_fitness_fair in sfittest:
        i=sfittest.index(chairs_fitness_fair)
        cls_chairs[i]=chairs_fitness_fair[0]
    print(cls_chairs[0])
    draw(cls_chairs)
    
    #crossover next gen 100
    fittest = cls_chairs[:50]
    cls_chairs = crossover(fittest[0],fittest[1],120)

    #just old gen 50
    for i in fittest:
        cls_chairs.append(i)
    
    #randomize some
    for i in range(30):
        cls_chairs.append(mutate(cls_chairs[0],30,'random'))

    #mutation
    for chairs in cls_chairs[50:120]:
        j= cls_chairs.index(chairs)
        cls_chairs[j]=mutate(chairs,random.randint(0,30),40)

    print('gen '+str(count+1)+' finished')
    count +=1







