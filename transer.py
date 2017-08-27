import os
from api_part import _init_ , static_content
from test_part import static_test_content

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
                with open("apis/"+filename+".py","w") as f:
                    f.close()
            rememberlines.append(i)
            docnames.append(filename+".py")

    with open('test/test.py', "w+") as ftest:
        ftest.writelines(static_test_content)
        ftest.close()

    #Get the file content block in the markdown file.
    for number in range(len(rememberlines)):
        if number != len(rememberlines)-1:
            numa = rememberlines[number]
            numb = rememberlines[number+1]
            block = mdlines[numa:numb]
        else:
            block = mdlines[rememberlines[number]:]
        print("generating:----------------- " + docnames[number] + "    --------------------------")
        generate_apis_with_tests(block,docnames[number])



def generate_apis_with_tests(block,filename): #generate list of file
    """
    generate api files and uncomplete api functions.
    use generate_init() function generate __init__.py file.
    Every Block is A file's content.It may contain many apis.
    """
    with open('apis/'+ filename,"w+") as f:
        f.writelines(static_content)
        f.close()

    apilines = []
    for i in range(len(block)):
        if block[i].count("#") == 4:
            apilines.append(i)
    
    for number in range(len(apilines)):
        if number != len(apilines)-1:
            small_block = block[apilines[number]:apilines[number+1]]
        else:
            small_block = block[apilines[number]:]

        generate_one_api_with_test(small_block,filename)


def generate_one_api_with_test(small_block,filename):
    """
    Use the content of the api to create api's static content.
    """


    dic = {}
    dic["give"] = None
    dic["ret"] = None
    dic["header"] = None

    find(small_block,dic)

    method = dic["method"]
    apiname = dic["apiname"]
    wrapper = dic["header"]
    urlargs = dic["urlargs"]
    givecontent = dic["give"]
    retcontent = dic["ret"]

    filename = "apis/" + filename


    file = open(filename,"a")
    file.writelines(['\n'])

    #@wrapper
    if wrapper != None:
        wrappercontent = ["#@" + wrapper + "_required\n"]
        file.writelines(wrappercontent)


    #@api.route content and methods
    headcontent = [
        "@api.route('/" + apiname + "/"
    ]
    if urlargs != None:
        headcontent.append('?')
        keys = list(urlargs.keys())
        values = list(urlargs.values())
        for v in range(len(urlargs)):
            if v != len(urlargs)-1:
                headcontent.append(keys[v]+"=")
                headcontent.append(values[v]+"&")
            else:
                headcontent.append(keys[v]+"=")
                headcontent.append(values[v])
    file.writelines(headcontent)

    if method == None:
        print("Can't find leagle Content")
    elif 'GET' in method:
        methodcontent = ["',methods = ['GET'])\n"]
    elif 'POST' in method :
        methodcontent = ["',methods = ['POST'])\n"]
    elif 'PUT' in method:
        methodcontent = ["',methods = ['PUT'])\n"]
    else:
        methodcontent = ["',methods = ['OTHER'])\n" ]
    file.writelines(methodcontent)


    funccontent = [
        "def "+apiname+"("
    ]
    if urlargs != None:
        for v in range(len(urlargs)):
            if v != len(urlargs)-1:
                funccontent.append(keys[v]+",")
            else:
                funccontent.append(keys[v])
    funccontent.append("):\n")
    file.writelines(funccontent)

    

    if givecontent != None:

        keys , values = list(givecontent.keys()),list(givecontent.values())
        bodygetcontent = []
        for v in range(len(givecontent)):
            bodygetcontent.append(" "*4 + keys[v] + "=request.get_json().get('" + keys[v] + "')\n" )
        
        file.writelines(bodygetcontent)

    if retcontent != None:
        keys,values = list(retcontent.keys()),list(retcontent.values())
        bodyrescontent=[]
        bodyrescontent.append(" "*4 + "return Response(json.dumps({\n")
        for v in range(len(retcontent)):
            bodyrescontent.append(" "*8 + '"' + keys[v].strip(' ').strip(",") + '":"content",\n')
        bodyrescontent.append(" "*8 + "}))\n")

        file.writelines(bodyrescontent)

    file.writelines([" "*4 + "pass\n"])
    file.close()

    with open("test/test.py","a") as file:
        write_one_test(dic,file)


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
            if "None" in dic["header"] or "无" in dic["header"] or "NONE" in dic["header"]:
                dic["header"] = None


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


    for i in range(len(small_block)):

        if 'DATA' in small_block[i]:
            line1 = i
            for x in range(len(small_block[:])):

                #print(small_block[x])
                if '}' in small_block[x] and x > line1:

                    line2 = x
                    datablock = small_block[line1:line2]

                    if 'POST' in small_block[i] or 'PUT' in small_block[i]:
                        giveout = {}
                        for p in range(len(datablock)):
                            if ':' in datablock[p]:
                                flagindex = datablock[p].find(':')
                                keyindex = datablock[p].find('"')
                                key = datablock[p][keyindex:flagindex-1].strip('"').strip("'").strip("\n").rstrip(',')
                                value = datablock[p][flagindex+1:].strip(',').strip('"').strip("'").strip("\n").rstrip(',')
                                giveout[key] = value
                                dic["give"] = giveout



                    elif 'RESPONSE' in small_block[i]:
                        retback = {}
                        for p in range(len(datablock)):
                            if ':' in datablock[p]:
                                flagindex = datablock[p].find(':')
                                keyindex = datablock[p].find('"')
                                key = datablock[p][keyindex:flagindex-1].strip('"').strip("'").strip("\n")
                                value = datablock[p][flagindex+1:].strip(',').strip('"').strip("'").strip("\n")
                                retback[key] = value
                                dic["ret"] = retback

                    break

def write_one_test(dic,file):

    method = dic["method"]
    apiname = dic["apiname"]
    wrapper = dic["header"]
    urlargs = dic["urlargs"]
    givecontent = dic["give"]
    retcontent = dic["ret"]

    test_content = [
        " "*4 + "def test_rank_" + apiname + "(self):\n",
        " "*8 + "response = self.client." + method.lower().lstrip(' ').rstrip(' ') +"(",
    ]

    if urlargs != None:
        keys = list(urlargs.keys())
        for p in range(len(urlargs)):
            if p != len(urlargs)-1:
                test_content.append(keys[p]+"=value,")
            else:
                test_content.append(keys[p]+"=value),\n")
    else:
        test_content.append("),\n")
    test_content.append(" "*12 + "url_for('api." + apiname + "',_external=True),\n",)

    if wrapper != None:
        test_content.append(" "*12+"headers = { },\n")

    if givecontent != None:
        keys = list(givecontent.keys())
        test_content.append(" "*12 + "data=json.dumps({\n")
        for o in range(len(givecontent)):
            if o == len(givecontent)-1:
                test_content.append(' '*16 + '"' +  keys[o]+'":"content",\n')
            else:
                test_content.append(' '*16 + '"' + keys[o]+'":"content"\n')
        test_content.append(" "*12 + "}),\n")

    test_content.append(" "*12 + "content_type = 'application/json')\n")


    file.writelines(test_content)

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