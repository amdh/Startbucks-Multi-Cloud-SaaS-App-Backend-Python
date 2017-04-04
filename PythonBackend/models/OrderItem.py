
class OrderItem(db.Model, Serializer):

	name = db.Column(db.String(20))
    milk = db.Column(db.String(20))
    size = db.Column(db.String(30))
	qty = db.Column(db.Integer)


	def __init__(self, name, milk, size, qty):
        self.name = name;
        self.milk = milk
        self.size = size
        self.qty = qty


	def serialize(self):
        ser_obj = Serializer.serialize(self)        
        return ser_obj


