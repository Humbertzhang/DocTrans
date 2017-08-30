## DocTrans
A api and test generate program of flask.
Support python2 together with python3.
####MarkDown file format
+ You should use '##' to identify a filename.
+ You should use '####' to identify an api of a file.
+ You have to give out the api,header and url like that :

  |URL|Header|Method|
  | :--- | :-- | :-- |
  |/api/v1.0/test/ |adminHeader|POST|
  
  URL:You can write that with or without '/api/v1.0'.It determines the `api's name`.And It can identify the url arguments.
  
  Header:You can wirte testHeader to generate '@test_required' decorator above your api.
  
  POST:DocTrans can distinguish 'GET','POST','PUT' methods.Others will generate 'OTHER' sentence.
  
+ You should give out the POST OR PUT DATA like that: `**POST DATA**` or `**PUT DATA**` while giving the response data like that `**RESPONSE DATA**`
+ You have to use that format to give out post/put data or response data
>``` 
>{
>    "key1":Anything you want to write,
>    "key2":Life is Short,you need Python,
>}
>```

More details you can see that gif:
![doctrans.gif](http://upload-images.jianshu.io/upload_images/5195759-495068f5c7508552.gif?imageMogr2/auto-orient/strip)

or git clone and try it : )

## Welcome to use,issue,fork and contribute!
