import uuid

def gid(df,v1=None,v2=None,v3=None,v4=None,v5=None):
    list_unique_id = []
    for i in range(0, len(df)):
        if v1 == None and v2 == None and v3== None and v4== None and v5== None:
            uid = str(uuid.uuid4())
        elif v1 != None and v2 == None and v3== None and v4== None and v5== None:
            uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, (str(df[v1][i])))) 
        elif v1 != None and v2 != None and v3== None and v4== None and v5== None:
            uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, (str(df[v1][i]) +str(df[v2][i]))))          
        elif v1 != None and v2 != None and v3!= None and v4== None and v5== None:
            uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, (str(df[v1][i]) +str(df[v2][i]) +str(df[v3][i]))))
        elif v1 != None and v2 != None and v3!= None and v4!= None and v5== None:
            uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, (str(df[v1][i]) +str(df[v2][i]) +str(df[v3][i]) + str(df[v4][i]))))
        else:
            uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, (str(df[v1][i])+ str(df[v2][i]) +str(df[v3][i]) + str(df[v4][i]) + str(df[v5][i]))))
        list_unique_id.append(uid)
    return list_unique_id
