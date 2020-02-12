import json

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def parseBusinessData():
    #read the JSON file
    with open('./yelp_CptS451_2020/yelp_business.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('./business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write(cleanStr4SQL(data['name'])+'\t') #name
            outfile.write(cleanStr4SQL(data['address'])+'\t') #full_address
            outfile.write(cleanStr4SQL(data['state'])+'\t') #state
            outfile.write(cleanStr4SQL(data['city'])+'\t') #city
            outfile.write(cleanStr4SQL(data['postal_code']) + '\t')  #zipcode
            outfile.write(str(data['latitude'])+'\t') #latitude
            outfile.write(str(data['longitude'])+'\t') #longitude
            outfile.write(str(data['stars'])+'\t') #stars
            outfile.write(str(data['review_count'])+'\t') #reviewcount
            outfile.write(str(data['is_open'])+'\t') #openstatus

            categories = data["categories"].split(', ')
            outfile.write(str(categories)+'\t')  #category list
            
            attributes = data["attributes"]
            outfile.write(str(parseRecursive(attributes)) + '\t') # write your own code to process attributes

            hours = data["hours"]
            outfile.write(str(parseRecursive(hours))) # write your own code to process hours

            outfile.write('\n')
            line = f.readline()
            count_line +=1
    # print(count_line)
    outfile.close()
    f.close()

def parseUserData():
    #read the JSON file
    with open('./yelp_CptS451_2020/yelp_user.JSON', 'r') as f:
        outfile = open('./user.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON object and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['user_id'])+'\t') #user id
            outfile.write(cleanStr4SQL(data['name'])+'\t') #name
            outfile.write(str(data['average_stars'])+'\t') #average stars
            outfile.write(str(data['cool'])+'\t') #cool
            outfile.write(str(data['funny'])+'\t') #funny
            outfile.write(str(data['useful'])+'\t') #userful
            outfile.write(str(data['tipcount'])+'\t') #tipcount
            outfile.write(str(data['fans'])+'\t') #fans

            friends = data['friends']
            outfile.write(str(friends)+'\t') #friends

            outfile.write(cleanStr4SQL(data['yelping_since'])) #yelping_since

            outfile.write('\n')
            line = f.readline()
            count_line += 1
    # print(count_line)
    outfile.close()
    f.close()

def parseCheckinData():
    #write code to parse yelp_checkin.JSON
    pass


def parseTipData():
    #write code to parse yelp_tip.JSON
    pass

def parseRecursive(passedDic):
    # print("entered parseRecursive")
    # print(passedDic)
    # code to recursively parse nested json objects

    keys = passedDic.keys()
    result = []

    for key in keys:
        result.append(key)
        if isinstance(passedDic[key], dict):
            result.append(parseRecursive(passedDic[key]))
        else:
            result.append(passedDic[key])

    return result

parseBusinessData()
parseUserData()
parseCheckinData()
parseTipData()
