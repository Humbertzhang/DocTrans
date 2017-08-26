##filename1

####API描述:POST,PUT示例

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/api1/ |adminHeader|POST|    adminHeader 生成@admin_required

**POST(PUT) DATA**
```
{
    "key1":Type,
    "key2":Type
}

```

**RESPONSE DATA**
```
{
    "key1":Type,
    "key2":Type
}

```

####API 描述:GET示例
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/api2/?arg1=type&arg2=type&arg3=type |NONE| GET|   #NONE,无,none为没有

**RESPONSE DATA**
```
{
    "key1":Type,  #It will ignore comment like this
    "key2":Type     
}

```

##filename2

####API描述:POST,
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/api3/ |editHeader|PUT|

**PUT DATA**
```
{
    "key1":Type,
    "key2":Type
}

```

**RESPONSE DATA**
```
{
    "key1":Type,
    "key2":Type
}

```

##filename3


####API描述:POST,PUT示例
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/api4/ |loginHeader|POST|


**PUT DATA**
``` 
{   
    "key1":Type,
    "key2":Type
}

```

**RESPONSE DATA**
``` 
{
    "key1":Type,
    "key2":Type
}

```

##filename4

####其他API示例
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/api5/ |loginHeader|DELETE|


######### Other API will only generate wrapper and func


