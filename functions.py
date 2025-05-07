def price_to_probability(price):
    
    if price > 0:
        probability = 100 / (price + 100)
    else:
        probability = abs(price) / (abs(price) + 100)
    
    return probability * 100

def edge(price_probabliity, model_probablity):
    return model_probablity - price_probabliity


