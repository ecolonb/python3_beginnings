from suds.client import Client


def getMethods():
    client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
    print(client.service.Multiply(10, 11))


getMethods()
