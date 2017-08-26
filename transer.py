import os
from api_part import _init_ , static_content

def makedir():
    """
    generate dirs to place apis and tests
    """
    #generate api floder
    if os.path.isdir("apis"):
        pass
    else:
        os.mkdir("apis")

    #generate test floder and test.py file
    if os.path.isdir("test"):
        pass
    else:
        os.mkdir("test")
    if os.path.isfile("test/test.py"):
        pass
    else:
        with open("test/test.py","w+") as f:
            f.close()


def generate(mdfile):
    """
    Read and understand mdfile.
    Use generate_apis and generate_tests to generate apis and tests.
    """
    if not os.path.isfile(mdfile):
        print("Incorrect Address")
        return
    else:
        mdfile = open(mdfile,"r")
        
    #find a filename.
    #use this filename to generate api file
    #rememberlines is used to remember the lines which is filename
    rememberlines = []
    docnames = []
    mdlines = mdfile.readlines()
    for i in range(len(mdlines)):
        if mdlines[i].count("#") == 2:
            filename = mdlines[i].strip("#")
            if filename[-1] == '\n':
                filename = filename[:-1]
            #generate filename.py document
            if os.path.isfile("apis/"+filename+".py"):
                pass
            else:
                with open("apis/"+filename+".py","w+") as f:
                    f.close()
            rememberlines.append(i)
            docnames.append(filename+".py")

    #Get the file content block in the markdown file.
    for number in range(len(rememberlines)):
        if number != len(rememberlines)-1:
            numa = rememberlines[number]
            numb = rememberlines[number+1]
            block = mdlines[numa:numb]
        else:
            block = mdlines[rememberlines[number]:]
        print("generating: " + docnames[number] + "......")
        generate_apis(block,docnames[number])
        generate_tests(block)

def generate_apis(block,filename): #generate list of file
    """
    generate api files and uncomplete api functions.
    use generate_init() function generate __init__.py file.
    Every Block is A file's content.It may contain many apis.
    """
    apilines = []
    for i in range(len(block)):
        if block[i].count("#") == 4:
            apilines.append(i)
    
    for number in range(len(apilines)):
        if number != len(apilines) - 1:
            small_block = block[ apilines[number]:apilines[number+1]]
        else:
            small_block = block[ apilines[number]:]
        #print(small_block)
        generate_one_api(small_block,filename)

def generate_one_api(small_block,filename):
    """
    Use the content of the api to create api's static content.
    """
    dic = {}
    #dic["apiname"] = None
    #dic["method"] = None
    #dic["header"]
    find(small_block,dic)
    dic["give"] = None
    dic["ret"] = None

    method = dic["method"]
    apiname = dic["apiname"]
    header = dic["header"]
    urlargs = dic["urlargs"]
    givecontent = dic["give"]
    retcontent = dic["ret"]

    filename = "apis/" + filename
    file = open(filename,"w+")
    file.writelines(static_content)

    #@api.route content and methods
    headcontent = [
        "@api.route('/" + apiname + "/') " +",methods="
    ]
    file.writelines(headcontent)

    if method == None:
        print("Can't find leagle Content")
    elif 'GET' in method:
        methodcontent = ["['GET'])\n"]
    elif 'POST' in method :
        methodcontent = ["['POST'])\n"]
    elif 'PUT' in method:
        methodcontent = ["['PUT'])\n"]
    else:
        methodcontent = [ "['UNKONW'])\n" ]
    file.writelines(methodcontent)

    funccontent = [
        "def "+filename+"():\n"
    ]
    file.writelines(funccontent)



def find(small_block,dic):
    """
    Find method that the api use by the table used in apidoc.md file.
    GET , POST and PUT methods will be identified.
    table format:
    |URL|Header|Method|
    | :--- | :-- | :-- |
    |/api/v1.0/url/ |adminHeader| POST|
    """
    
    for i in range(len(small_block)):
        #if '/' in small_block[i], it is the info line.
        if '/' in small_block[i]:
            #print("Yoooooo2")
            symbolcounter = []          #count '|'
            #print(range(len(small_block[i])))
            for w in range(len(small_block[i])):
            #    print("W:"+ str(w),end = ' ')
                if small_block[i][w-1] == '|':
                    symbolcounter.append(w)
            
            if len(symbolcounter) != 4:
                print("Format Error!")
            dic['method'] = small_block[i][ symbolcounter[2] : symbolcounter[3]-1 ]
            #print("Method :"+ dic['method'])


            temp = small_block[i][ symbolcounter[1]:symbolcounter[2]]
            dic["header"] = temp[:(temp.find("Header"))].strip(' ')
            #print("Header:" + dic["header"])

            temp = small_block[i][symbolcounter[0]:symbolcounter[1]]

            #print("Temp:" + temp)
            symbolcounter2 = []         #count '/'
            for i in range(len(temp)):
                if temp[i] == '/':
                    symbolcounter2.append(i)
            if(len(symbolcounter2) == 0):
                print("Format Wrong In URL")
            dic["apiname"] = (temp[symbolcounter2[-2] : symbolcounter2[-1]]).strip('/')
            dic["urlargs"] = get_urlargs(temp,dic)

        elif 'DATA' in small_block[i]:
            line1 = i
            for x in range(len(small_block[i:])-1):
                #print(small_block[x])
                if '}' in small_block[x]:
                    line2 = x
                    datablock = small_block[line1:line2]
                
                    if 'POST' in small_block[i] or 'PUT' in small_block[i]:
                        giveout = {}
                        for p in range(len(datablock)-1):
                            if ':' in datablock[p]:
                                flagindex = datablock[p].find(':')
                                keyindex = datablock[p].find('"')
                                key = datablock[p][keyindex:flagindex-1]
                                key = key.strip('"').strip("'").strip("\n")
                                value = datablock[p][flagindex+1:].strip(',').strip('"').strip("'").strip("\n").rstrip(',')
                                giveout[key] = value
                                dic["give"] = giveout
                                print("Give:",giveout)

                    elif 'RESPONSE' in small_block[i]:
                        retback = {}
                        for p in range(len(datablock)-1):
                            if ':' in datablock[p]:
                                flagindex = datablock[p].find(':')
                                keyindex = datablock[p].find('"')
                                key = datablock[p][keyindex:flagindex-1].strip('"').strip("'").strip("\n")
                                value = datablock[p][flagindex+1:].strip(',').strip('"').strip("'").strip("\n")
                                retback[key] = value
                                dic["ret"] = retback
                                print("ret",retback)


def get_urlargs(temp,dic):
    argcounter = [] #count &
    args = {}
    if '?' in temp:
        temp = temp[ temp.find('?') : ]
    else:
        return None

    for i in range(len(temp)):
        if temp[i] == '&' or temp[i] == '?':
            argcounter.append(i)
    
    for j in range(len(argcounter)):
        if j != len(argcounter) -1:
            tinyblock = temp[argcounter[j]:argcounter[j+1]]
        else:
            tinyblock = temp[argcounter[j]:]
        
        args[ tinyblock[ 1: tinyblock.find('=') ] ] = (tinyblock[tinyblock.find('=')+1 : ]).strip('|').strip(' ')
    
    return args

def generate_tests(block):
    """
    generate unit tests.
    """
    pass

def generate_init():
    """
    generate __init__.py.
    Be used in generate function.     
    """
    #Use os.ls to get all the api files.
    pass



if __name__ == '__main__':
    makedir()
    mdfile = str(input(">Api document path:"))
    generate(mdfile)