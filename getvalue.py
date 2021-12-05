#The below inputs have been given as part of challenge
object = {"x":{"y":{"z":"d"}}}
#key = a/b/c(converting this given key to string as below)
key ='x/y/z'
#defining a function to convert above string to list
def Convert(string):
    list1 = list(string.split("/"))
    return list1

  key1 =Convert(key)

#defining a function to get value from nested object
def get_value(object, keys):
    internal_dict_value = object
    for k in keys:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value

print(get_value(object,key1))
