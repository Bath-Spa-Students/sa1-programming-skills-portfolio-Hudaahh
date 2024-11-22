dictionary = { 'Name' : 'huda' , 'roll no ' : '2846' , 'fathers name ': 'shamsudheen' }
print(dictionary.items())
# in out put small braces because they are tuples , key value pair is in tuple form ---- there is a list
#  ('name ', 'sinan') -this is element  -to secure our data not to change



# to check keyes in our dictionary


dictionary  = {'name' : 'huda' , 'roll no' : '2846 ' , 'fathers name': 'shamsudheen' }
print(dictionary.keys())

#output - in list form we get keys in our dict


#delet method


dictionary = {'name' : 'huda' , 'roll no' : '2846' , 'fathers name' : 'shamshudheen'}
del dictionary ["roll no"]
print(dictionary.items())
