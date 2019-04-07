from flask import Flask, render_template, request, redirect, url_for
import csv
application = Flask(__name__)

JG_FUNDRAISING_PAGE_ID = '11779935';

items = []
buffs = []
misc = []

class item:
    def __init__(self, name, cost, code):
        self.name = name
        self.cost = cost
        self.code = code

with open('./items/items.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        newItem = item(row[0], row[1], row[2])
        items.append(newItem)

with open('./items/buffs.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        newItem = item(row[0], row[1], row[2])
        buffs.append(newItem)

with open('./items/misc.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        newItem = item(row[0], row[1], row[2])
        misc.append(newItem)

@application.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if request.args.get('cost') != None:
            cost = float(request.form.get('cost').replace("/", "")) + float(request.args.get('cost'))
        else:
            cost = float(request.form.get('cost').replace("/", ""))
        print(cost)
        code = str(request.form.get('code')).replace("/", "")

        send = request.form.get('send')
        print(send)
        if request.args.get('message') != None:
            message = request.args.get('message') + '{item:' + code + '}'
        else:
            message = '{item:' + code + '}'
        print(message)
        if send == 'true':
            #Send the url to JustGiving for Checkout
            return redirect('http://link.justgiving.com/v1/fundraisingpage/donate/pageId/' + JG_FUNDRAISING_PAGE_ID +
                        '?amount=' + str(cost) + '&currency=USD&reference=bbcsh&message=' + message + '&send=' + str(send))
        else:
            return redirect(url_for('index') + "?cost=" + str(cost) + "&message=" + str(message) + "&send=" + str(send))
    return render_template('home.html', Items=items, Buffs=buffs, Misc=misc)

#The below route is no longer needed. With the new changes, all the info
#needed for the JustGiving app can be found at the index.
@application.route("/donate", methods=['GET', 'POST'])
def donation():
    itemName = request.args.get('item')
    if request.method == 'POST':
        cost = request.args.get('cost')
        code = request.args.get('code')
        return redirect(url_for('donation') + "?cost=" + str(cost) + "&code=" + str(code))


    return render_template('store.html', item=itemName)



if __name__ == "__main__":
    application.run()
