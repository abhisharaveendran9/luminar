class editor:
    def functionalities(self):
        self.funcs=["createnewfile","execute","save"]
        return self.funcs

class pycharm(editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["debug","versoncontrolling"])
        return funcs
class vscode(editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["more extension support"])
        return funcs

vsc=vscode()
print(vsc.functionalities())

pyc=pycharm()
print(pyc.functionalities())