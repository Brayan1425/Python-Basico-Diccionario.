menu = dict {
 "Pan Salados":
   "Producto":list:[
    list{"nombre": "Baguette tradicional", "valor":"$" 3.50}
    list {"nombre": "Pan de molde integral", "valor":"$" 5.50 }
    list{"nombre": "Focaccia con romero y aceite de oliva", "valor":"$" 4.76 }
    list{"nombre": "Chapata", "valor":"$" 2.56   }
    list{"nombre": "Pan de centeno","valor":"$"  2.13  }
    list{"nombre": "Pan de cebolla","valor":"$" 1.90  }
    list{"nombre": "Pretzels","valor":"$" 1.85  }
    list{"nombre": "Pan de ajo","valor":"$" 1.77}  #datos del diccionario.
    list{"nombre": "Pan de maíz","valor":"$" 2.33 }
    list{"nombre": "Bollos de pan con semillas","valor":"$" 2,89}
],

"Promociones":[
  {"codigo":3, "nombre", "compre 7", "valor": "$" 26,6}
     {"codigo":8,"nombre","compre 9","valor": "$": 15,92}
  ]
}

"Pan Azucar":
"Producto":list :[
        list{"nombre": "Rosquillas", "valor":"$" 2.50}
        list{"nombre": "Croissants", "valor":"$" 4.50 }
        list{"nombre": "Napolitanas", "valor":"$" 6.76 }
        list{"nombre": "Dónutso", "valor":"$" 1.56   }
        list{"nombre": "Magdalenas","valor":"$"  1.13  }
        list{"nombre": "Tartaletas de frutas","valor":"$" 3.90  }
        list{"nombre": "Bizcochos","valor":"$" 4.85  }
        list{"nombre": "Ensaimadas","valor":"$" 3.77}
        list{"nombre": "Galletas","valor":"$" 4.33 }
        list{"nombre": "Crepes","valor":"$" 4,89}
    ]),
"Promociones2":{
    {"codigo":3, "nombre","compre 7","valor": "$" 26,6}
     {"codigo":8,"nombre","compre 9","valor": "$": 15,92}
  },
"Postres": {
"Producto":list : [
    list{"nombre": "Tiramisú", "valor":"$" 5.50}
    list {"nombre": "Cheesecake de fresa", "valor":"$" 3.50 }
    list{"nombre": "Coulant de chocolate", "valor":"$" 5.76 }
    list{"nombre": "Crème brûlée", "valor":"$" 3.56   }
    list{"nombre": "Magdalenas","valor":"$"  5.13  }
    list{"nombre": "Tartaletas de frutas","valor":"$" 8.90  }
    list{"nombre": "Bizcochos","valor":"$" 6.85  }
    list{"nombre": "Ensaimadas","valor":"$" 9.77}
    list{"nombre": "Galletas","valor":"$" 3.33 }
    list{"nombre": "Crepes","valor":"$" 2,89}
    ]
"Promociones3":({
    {"codigo":3, "nombre","compre 7","valor": "$" 26,6}
     {"codigo":8,"nombre","compre 9","valor": "$": 15,92}
  })
},

Print(f"""______  _                                   _      _                  _                                          _              _          _____  _       _____  _____ ______ ______  _____
| ___ \(_)                                 (_)    | |                | |                                        | |            (_)        |  ___|| |     |  __ \|  _  || ___ \|  _  \|  _  |
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _  | |  __ _   _ __    __ _  _ __    __ _   __| |  ___  _ __  _   __ _  | |__  | |     | |  \/| | | || |_/ /| | | || | | |
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` | | | / _` | | '_ \  / _` || '_ \  / _` | / _` | / _ \| '__|| | / _` | |  __| | |     | | __ | | | ||    / | | | || | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| | | || (_| | | |_) || (_| || | | || (_| || (_| ||  __/| |   | || (_| | | |___ | |____ | |_\ \\ \_/ /| |\ \ | |/ / \ \_/ /
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_| |_| \__,_| | .__/  \__,_||_| |_| \__,_| \__,_| \___||_|   |_| \__,_| \____/ \_____/  \____/ \___/ \_| \_||___/   \___/
                                                                                | |
                                                                                |_|
 """)
#mensaje de bienvenida y lo imprimimos con un print
Print("Seleccion la categoria")

def imprimir_productos_categorizados(productos):
    for categoria, lista_productos in productos.items():
        print(f"Categoría: {categoria.capitalize()}")
        print("------------------------------")
        for producto in lista_productos:
            print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']}")
        print()
