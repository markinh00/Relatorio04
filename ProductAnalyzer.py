from database import Database


class ProductAnalyzer:
    db = Database(database="relatorio04", collection="data")
    db.resetDatabase()

#--------------------------------------------------questao 01-----------------------------------------------------------
    def questao01(self, id):
        foundClient = self.db.collection.find_one({"cliente_id": {"$eq": id}})

        if not foundClient:
            print("Client not Found!!")
            return None

        total = 0
        for product in foundClient["produtos"]:
            total = total + product["preco"]

        return total

#--------------------------------------------------questao 02-----------------------------------------------------------
    def questao02(self):
        foundSale = self.db.collection.find()

        if not foundSale:
            print("Could not Find any sale!!")
            return None

        disorderedProducts = []
        for sale in foundSale:
            for product in sale['produtos']:
                disorderedProducts.append(product)

        orderedProducts = {}
        for product in disorderedProducts:
            if not orderedProducts.get(product["nome"], False):
                orderedProducts.update({product["nome"]: product})
            else:
                orderedProducts[product["nome"]]["quantidade"] += product["quantidade"]

        leastSoldProduct = {}
        for product in orderedProducts:
            if not bool(leastSoldProduct):
                leastSoldProduct = orderedProducts[product]

            if orderedProducts[product]['quantidade'] < leastSoldProduct["quantidade"]:
                leastSoldProduct = orderedProducts[product]

        return leastSoldProduct

#--------------------------------------------------questao 03-----------------------------------------------------------
    def questao03(self):
        foundSale = self.db.collection.find()

        if not foundSale:
            print("Could not Find any sale!!")
            return None

        disorderedClients = []
        for client in foundSale:
            spent = 0
            for product in client['produtos']:
                spent += product["quantidade"] * product["preco"]

            disorderedClients.append({"cliente_id": client["cliente_id"], "gasto": spent})

        orderedClients = {}
        for client in disorderedClients:
            if not orderedClients.get(client["cliente_id"], False):
                orderedClients.update({client["cliente_id"]: client})
            else:
                orderedClients[client["cliente_id"]]["gasto"] += client["gasto"]

        leastSpentClient = {}
        for client in orderedClients:
            if not bool(leastSpentClient):
                leastSpentClient = orderedClients[client]

            if orderedClients[client]["gasto"] < leastSpentClient["gasto"]:
                leastSpentClient = orderedClients[client]

        return leastSpentClient
#--------------------------------------------------questao 04-----------------------------------------------------------
    def questao04(self):
        foundProducts = self.db.collection.find({"produtos.quantidade": {"$gt": 2}}, {"_id": 0, 'produtos': 1})

        if not foundProducts:
            print("Could not Find any sale!!")
            return None

        products = []
        for product in foundProducts:
            products.append(product)
        return products