
import httpx

base_url = 'https://www.canadapost-postescanada.ca/track-reperage/rs/track/json/package?pins='
def status(trackID):
    url = f'{base_url}{trackID}'
    rep2=httpx.get(url)
    if rep2.status_code == 200:
        test = rep2.json()
        if 'status' in test[0]:
            return (test[0]['status'], test[0]["expectedDlvryDateTime"]["dlvryDate"])
        else:
            return 'Post canada n a pas le num'
    else:
        return rep2.status_code
def ref(track):
    ref1 = 'https://www.canadapost-postescanada.ca/track-reperage/rs/track/json/package?refNbrs='
    
    ref1 = f'{base_url}{track}'
    rep = httpx.get(ref1)



Shopify ='https://8604f995f72d2117c1ffd153e6c3f237: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@eco-esssentials.myshopify.com/admin/api/2022-01/orders.json'

def command():
    Commande = httpx.get(Shopify)
    com = Commande.json()
    li =[]
    for a in com['orders']:
        for b in a["fulfillments"]:
            li.append((a["order_number"], b["tracking_numbers"], a['id']))
    print(li)
    return li

def achived(num):
    link = f'https://8604f995f72d2117c1ffd153e6c3f237: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@eco-esssentials.myshopify.com/admin/orders/{num}/close.json'
    return httpx.post(link)

for id in command():
    if len(id[1]) == 0:
        continue
    else:
        if status(id[1][0])[0] == 'Delivered':
            achived(id[2])
        print(id[0], status(id[1][0]))

