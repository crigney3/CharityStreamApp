from flask import Flask, render_template, request, redirect, url_for
import csv
application = Flask(__name__)

JG_FUNDRAISING_PAGE_ID = '11779935';

class item:
    def __init__(self, name, cost, code):
        self.name = name
        self.cost = cost
        self.code = code;

@application.route("/", methods=['GET', 'POST'])
def hello():
    items = []
    if request.method == 'POST':
        itemName = request.form.get('item').replace(" ", "%20")
        cost = request.form.get('cost')
        code = request.form.get('code')
        return redirect(url_for('donation') + '?item=' + str(itemName) + "&cost=" + str(cost) + "&code=" + str(code))
    with open('./items/items.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            newItem = item(row[0], row[1], row[2])
            items.append(newItem)
    return render_template('home.html', Items=items)

@application.route("/donate", methods=['GET', 'POST'])
def donation():
    itemName = request.args.get('item')
    if request.method == 'POST':
        itemName = request.form.get('item')
        return redirect(url_for('donation') + '?item=' + str(itemName))


    return render_template('store.html', item=itemName)



if __name__ == "__main__":
    application.run()
