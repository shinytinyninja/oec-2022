self.fileName = ("../test_cases/") + self.fileName + (".csv")
            print(self.fileName)
            
            with open(self.fileName) as csv_file:
                node = [line.split(",") for line in csv_file]
                for i, info in enumerate(node):
                    temp.append(info)
            self.matrix = temp
            print("CSV Read")