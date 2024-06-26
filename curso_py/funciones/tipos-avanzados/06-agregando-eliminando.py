mascotas = ["Sere",
            "Luna",
            "Dimitry",
            "Miluni",
            "Yoni",
            "Canuto"]


mascotas.insert(0, "PerritaRubia")
mascotas.append("Perrita Triste")
print(mascotas)

mascotas.remove("Perrita Triste")
print(mascotas)

mascotas.pop(1)
print(mascotas)

del mascotas[0]
mascotas.clear()
print(mascotas)
