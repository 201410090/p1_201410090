song=["When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be "
"And in my hour of darkness " 
"She is standing right in front of me " 
"Speaking words of wisdom let it be " 

"Let it be let it be " 
"Let it be let it be " 
"Whisper words of wisdom let it be " 
 
"And when the broken-hearted people " 
"Living in the world agree " 
"There will be an answer let it be " 
"For though they may be parted " 
"There is still a chance that they will see " 
"There will be an answer let it be " 

"Let it be let it be " 
"Let it be let it be " 
"Yeah there will be an answer let it be " 
"Let it be let it be " 
"Let it be let it be " 
"Whisper words of wisdom let it be " 

"Let it be let it be " 
"Ah let it be yeah let it be " 
"Whisper words of wisdom let it be " 

"And when the night is cloudy " 
"There is still a light that shines on me " 
"Shine on until tomorrow let it be " 
"I wake up to the sound of music " 
"Mother Mary comes to me " 
"Speaking words of wisdom let it be " 

"Let it be let it be " 
"Let it be yeah let it be " 
"Oh there will be an answer let it be " 
"Let it be let it be " 
"Let it be yeah let it be " 
"Whisper words of wisdom let it be "]

print song
print ''

mydict=dict()

for i in song[0].split():
    if i not in mydict:
        mydict[i]= 1
    else:
        mydict[i]= mydict[i]+1
        
print mydict
print ''
print len(mydict)
print ''

list_keys = mydict.keys()
list_values = mydict.values()

for i in range(len(list_values)):
    if list_values[i]>=20:
        print list_keys[i]

raw_input()