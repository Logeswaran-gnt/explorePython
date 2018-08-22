import requests,json
url = "http://bugzilla5.tintri.com/rest/bug"
headers = {
        'cache-control': "no-cache",
        'postman-token': "ca17895a-4a46-8b7d-0de4-e42695d2a83e"
        }

def retrieveNewAssigned(login_name):
    #Will retrieve the bug id's of login_name which having status NEW or ASSIGNED
    newAssigned=[]
    response = requests.request("GET", url, headers=headers, params={"assigned_to":login_name,"include_fields":"assigned_to,status,id","api_key":"DP2P2Et6dILcO3GcRu3eqKHk0PkmCMqOBHf2yanL","status":["NEW","ASSIGNED"]})
    json_data = json.loads(response.text)
    for bug in (dict(json_data))['bugs']:
        newAssigned.append(str(bug['id']))
    print '-------------------------------------------------------------------------------------'
    print 'Status New and Assignee==>',newAssigned
    print '-------------------------------------------------------------------------------------'
    return newAssigned

def updateAssignedTo():
    bugsAffected=[]
    url = "http://bugzilla5.tintri.com/rest/bug/54106"
    assignedNow = 'akjain@tintri.com'         #set the login_name of the assignee to be removed
    assignedNew ='vagarwal@tintri.com'     #set the login_name of the assignee to be replaced
    idAll=('&ids=').join(retrieveNewAssigned(assignedNow))
    putData = "ids="+idAll+"&api_key=DP2P2Et6dILcO3GcRu3eqKHk0PkmCMqOBHf2yanL&assigned_to="+assignedNew   #kaviarasank%40tintri.com"
    response = requests.request("PUT", url, data=putData, headers={'content-type': "application/x-www-form-urlencoded"})
    json_data = json.loads(response.text)
    count=0
    for bug in (dict(json_data))['bugs']:
        bugsAffected.append(bug['id'])
        count+=1
    print count,bugsAffected

#retrieveNewAssigned()
#retrieveMultiState()
updateAssignedTo()
