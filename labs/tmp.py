
prod = 1
sigmoid = self.activation
for x_i, y_i in zip(X, self.y):
    prod = (sigmoid(x_i)**y_i) * (1 - sigmoid(x_i))**(1 - y_i)
return prod
