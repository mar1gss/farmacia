class Doctor:
    def __init__(self, medico_id, nombre, especialidad):
        self.medico_id = medico_id
        self.nombre = nombre
        self.especialidad = especialidad
    def datos(self):
        return f"Doctor {self.nombre} (ID: {self.medico_id}), especialidad: {self.especialidad}"

if __name__ == "__main__":
    doc = Doctor(101, "Garcia", "Cardiologia")
    print(doc.presentar())